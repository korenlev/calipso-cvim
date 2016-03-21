import json

from db_access import DbAccess
from network_agents_list import NetworkAgentsList

class DbFetchHostNetworkAgents(DbAccess):

  def __init__(self):
    self.agents_list = NetworkAgentsList()

  def get(self, id):
    query = """
      SELECT * FROM neutron.agents
      WHERE host = %s
    """
    return self.get_objects_list_for_id(query, "vservice", id)
    for o in results:
      self.set_vservice_type(o)
    return results

  # dynamically create sub-folder for vServices by type
  # also change 'configurations' field from JSON to object
  def set_vservice_type(self, o):
    o["master_parent_id"] = o["host"] + "-vservices"
    o["master_parent_type"] = "host_object_type"
    atype = o["agent_type"]
    agent = self.agents_list.get_type(atype)
    o["parent_type"] = "vservice_object_type"
    try:
      o["parent_id"] = o["master_parent_id"] + "-" + agent["type"] + "s"
      o["parent_text"] = agent["folder_text"]
    except KeyError:
      o["parent_id"] = o["master_parent_id"] + "-" + "miscellenaous"
      o["parent_text"] = "Misc. services"
    o["configurations"] = json.loads(o["configurations"])
