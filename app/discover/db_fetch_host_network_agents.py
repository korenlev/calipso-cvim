import json

from db_access import DbAccess
from network_agents_list import NetworkAgentsList
from inventory_mgr import InventoryMgr

class DbFetchHostNetworkAgents(DbAccess):

  def __init__(self):
    self.agents_list = NetworkAgentsList()
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
      self.set_agent_type(o)
    return results

  # dynamically create sub-folder for agents by type
  # also change 'configurations' field from JSON to object
  def set_agent_type(self, o):
    o["master_parent_id"] = o["host"] + "-network_agents"
    o["master_parent_type"] = "host_object_type"
    atype = o["agent_type"]
    agent = self.agents_list.get_type(atype)
    o["parent_type"] = "network_agent_object_type"
    try:
      o["parent_id"] = o["master_parent_id"] + "-" + agent["type"] + "s"
      o["parent_text"] = agent["folder_text"]
    except KeyError:
      o["parent_id"] = o["master_parent_id"] + "-" + "miscellenaous"
      o["parent_text"] = "Misc. services"
    o["configurations"] = json.loads(o["configurations"])
