from db_access import DbAccess
from singleton import Singleton
from inventory_mgr import InventoryMgr

import json
import re

class DbFetchOteps(DbAccess, metaclass=Singleton):

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
    host = vedge["host"]
    table_name = "neutron.ml2_" + tunnel_type + "_endpoints"
    results = self.get_objects_list_for_id(
      """
        SELECT *
        FROM {}
        WHERE host = %s
      """.format(table_name),
      "vedge", host)
    for doc in results:
      doc["id"] = host + "otep"
      doc["name"] = doc["id"]
      doc["overlay_type"] = tunnel_type
      doc["ports"] = vedge["tunnel_ports"] if "tunnel_ports" in vedge else []
      doc["master_parent_type"] = "vedge"
      doc["master_parent_id"] = id
      doc["parent_type"]= "oteps_folder"
      doc["parent_id"] = id + "-oteps"
      doc["parent_text"] = "OTEPs"
      if "udp_port" not in doc:
        doc["udp_port"] = "67"
    return results

