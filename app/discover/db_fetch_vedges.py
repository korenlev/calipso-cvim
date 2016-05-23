from db_access import DbAccess
from cli_access import CliAccess
from singleton import Singleton
from inventory_mgr import InventoryMgr
import json
import re

class DbFetchVedges(DbAccess, CliAccess, metaclass=Singleton):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()
    self.port_re = re.compile("^\s*port (\d+): ([^(]+)( \(internal\))?$")

  def get(self, id):
    host_id = id[:id.rindex('-')]
    results = self.get_objects_list_for_id(
      """
        SELECT *
        FROM neutron.agents
        WHERE host = %s AND agent_type = 'Open vSwitch agent'
      """,
      "vedge", host_id)
    ports = self.fetch_ports(host_id)
    for doc in results:
      doc["name"] = doc["host"] + "-OVS"
      doc["configurations"] = json.loads(doc["configurations"])
      doc["ports"] = ports
    return results

  def fetch_ports(self, host):
    ports = self.fetch_ports_from_dpctl(host)
    self.fetch_port_tags_from_vsctl(host, ports)
    return ports

  def fetch_ports_from_dpctl(self, host):
    cmd = "ovs-dpctl show"
    lines = self.run_fetch_lines(cmd, host)
    ports = {}
    for l in lines:
      port_matches = self.port_re.match(l)
      if not port_matches:
        continue
      port = {}
      id = port_matches.group(1)
      name = port_matches.group(2)
      is_internal = port_matches.group(3) == " (internal)"
      port["internal"] = is_internal
      port["id"] = id
      port["name"] = name
      ports[name] = port
    return ports

  # from ovs-vsctl, fetch tags of ports
  # example format of ovs-vsctl output for a specific port:
  #        Port "tap9f94d28e-7b"
  #            tag: 5
  #            Interface "tap9f94d28e-7b"
  #                type: internal
  def fetch_port_tags_from_vsctl(self, host, ports):
    cmd = "ovs-vsctl show"
    lines = self.run_fetch_lines(cmd, host)
    port_line_header_prefix = " " * 8 + "Port "
    port = None
    for l in lines:
      if l.startswith(port_line_header_prefix):
        port = None
        port_name = l[len(port_line_header_prefix):]
        # remove quotes from port name
        if '"' in port_name:
          port_name = port_name[1:][:-1]
        if port_name in ports:
          port = ports[port_name]
        continue
      if not port:
        continue
      if l.startswith(" " * 12 + "tag: "):
        port["tag"] = l[l.index(":")+2:]
        ports[port["name"]] = port
    return ports

  def add_links(self):
    vedges = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vedge"
    })
    for vedge in vedges:
      ports = vedge["ports"]
      for p in ports.values():
        self.add_link_for_vedge(vedge, p)

  def add_link_for_vedge(self, vedge, port):
    vnic = self.inv.get_by_id(self.get_env(), port["name"])
    if not vnic:
      self.find_matching_vconnector(vedge, port)
      self.find_matching_pnic(vedge, port)
      return
    source = vnic["_id"]
    source_id = vnic["id"]
    target = vedge["_id"]
    target_id = vedge["id"]
    link_type = "vnic-vedge"
    link_name = vnic["name"] + "-" + vedge["name"]
    if "tag" in port:
      link_name += "-" + port["tag"]
    state = "up" # TBD
    link_weight = 0 # TBD
    source_label = vnic["mac_address"]
    target_label = port["id"]
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight, source_label, target_label)

  def find_matching_vconnector(self, vedge, port):
    if not port["name"].startswith("qv"):
      return
    base_id = port["name"][3:]
    vconnector_interface_name = "qvb" + base_id
    vconnector = self.inv.get_by_field(self.get_env(), "vconnector",
      "interfaces", vconnector_interface_name)
    if not vconnector:
      return
    vconnector = vconnector[0]
    source = vconnector["_id"]
    source_id = vconnector["id"]
    target = vedge["_id"]
    target_id = vedge["id"]
    link_type = "vconnector-vedge"
    link_name = "port-" + port["id"]
    if "tag" in port:
      link_name += "-" + port["tag"]
    state = "up" # TBD
    link_weight = 0 # TBD
    source_label = vconnector_interface_name
    target_label = port["name"]
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight, source_label, target_label)

  def find_matching_pnic(self, vedge, port):
    if not port["name"].startswith("eth") and not port["name"].startswith("eno"):
      return
    pnic = self.inv.find_items({
      "environment": self.get_env(),
      "type": "pnic",
      "host": vedge["host"],
      "name": port["name"]
    })
    if not pnic:
      return
    pnic = pnic[0]
    source = vedge["_id"]
    source_id = vedge["id"]
    target = pnic["_id"]
    target_id = pnic["id"]
    link_type = "vedge-pnic"
    link_name = "Port-" + port["id"]
    state = "up" if pnic["Link detected"] == "yes" else "down"
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), vedge["host"],
      source, source_id, target, target_id,
      link_type, link_name, state, link_weight)
