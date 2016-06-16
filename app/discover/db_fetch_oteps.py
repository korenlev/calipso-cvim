from db_access import DbAccess
from singleton import Singleton
from inventory_mgr import InventoryMgr
from cli_access import CliAccess

import json
import re

class DbFetchOteps(DbAccess, CliAccess, metaclass=Singleton):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()
    self.port_re = re.compile("^\s*port (\d+): ([^(]+)( \(internal\))?$")

  def get(self, id):
    vedge = self.inv.get_by_id(self.get_env(), id)
    tunnel_type = None
    if "configurations" not in vedge:
      return []
    if "tunnel_types" not in vedge["configurations"]:
      return []
    if not vedge["configurations"]["tunnel_types"]:
      return []
    tunnel_type = vedge["configurations"]["tunnel_types"][0]
    host_id = vedge["host"]
    table_name = "neutron.ml2_" + tunnel_type + "_endpoints"
    env_config = self.config.get_env_config()
    distribution = env_config["distribution"]
    if distribution == "Canonical-icehouse":
      # for Icehouse, we only get IP address from the DB, so take the
      # host IP address and from the host data in Mongo
      host = self.inv.get_by_id(self.get_env(), host_id)
      results = [{"host": host_id, "ip_address": host["ip_address"]}]
    else:
      results = self.get_objects_list_for_id(
        """
        SELECT *
        FROM {}
        WHERE host = %s
        """.format(table_name),
        "vedge", host_id)
    for doc in results:
      doc["id"] = host_id + "-otep"
      doc["name"] = doc["id"]
      doc["host"] = host_id
      doc["overlay_type"] = tunnel_type
      doc["ports"] = vedge["tunnel_ports"] if "tunnel_ports" in vedge else []
      if "udp_port" not in doc:
        doc["udp_port"] = "67"
      self.get_vconnector(doc, host_id, vedge)

    return results

  # find matching vConnector by tunneling_ip of vEdge
  # look for that IP address in ifconfig for the host
  def get_vconnector(self, doc, host_id, vedge):
    tunneling_ip = vedge["configurations"]["tunneling_ip"]
    ifconfig_lines = self.run_fetch_lines("ifconfig", host_id)
    interface = None
    ip_string = " " * 10 + "inet addr:" + tunneling_ip + " "
    vconnector = None
    for l in ifconfig_lines:
      if l.startswith(" "):
        if interface and l.startswith(ip_string):
          vconnector = interface
          break
      else:
        if " " in l:
          interface = l[:l.index(" ")]

    if vconnector:
      doc["vconnector"] = vconnector

  def add_links(self):
    self.log.info("adding link types: vedge-otep, otep-vconnector")
    oteps = self.inv.find_items({
      "environment": self.get_env(),
      "type": "otep"
    })
    for otep in oteps:
      self.add_vedge_otep_link(otep)
      self.add_otep_vconnector_link(otep)

  def add_vedge_otep_link(self, otep):
    vedge = self.inv.get_by_id(self.get_env(), otep["parent_id"])
    source = vedge["_id"]
    source_id = vedge["id"]
    target = otep["_id"]
    target_id = otep["id"]
    link_type = "vedge-otep"
    link_name = vedge["name"] + "-otep"
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight)

  def add_otep_vconnector_link(self, otep):
    if "vconnector" not in otep:
      return
    vconnector = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vconnector",
      "host": otep["host"],
      "name": otep["vconnector"]
    }, get_single=True)
    if not vconnector:
      return
    source = otep["_id"]
    source_id = otep["id"]
    target = vconnector["_id"]
    target_id = vconnector["id"]
    link_type = "otep-vconnector"
    link_name = otep["name"] + otep["vconnector"]
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), otep["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight)

