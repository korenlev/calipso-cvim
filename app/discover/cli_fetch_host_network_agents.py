import json
import re
from cli_access import CliAccess
from network_agents_list import NetworkAgentsList

class CliFetchHostNetworkAgents(CliAccess):
  
  def __init__(self):
    super(CliFetchHostNetworkAgents, self).__init__()
    self.agents_list = NetworkAgentsList()

  def get(self, id):
    out = self.run("source openrc; neutron agent-list -D -fjson")
    out = self.binary2str(out)
    json_string = re.sub(r"\\n$", "", out)
    results = json.loads(json_string)
    for o in results:
      self.set_vservice_type(o)
    return results

  # dynamically create sub-folder for vServices by type
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
