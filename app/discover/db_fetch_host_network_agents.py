import json

from db_access import DbAccess
from inventory_mgr import InventoryMgr

class DbFetchHostNetworkAgents(DbAccess):

  def __init__(self):
    self.inv = InventoryMgr()

  def get(self, id):
    query = """
      SELECT * FROM neutron.agents
      WHERE host = %s
    """
    host_id = id[:-1*len("-network_agents")]
    host = self.inv.getSingle(self.get_env(), "host", host_id)
    results = self.get_objects_list_for_id(query, "network_agent", host_id)
    for o in results:
      o["configurations"] = json.loads(o["configurations"])
      o["name"] = o["binary"]
    return results
