import json
import re
from cli_access import CliAccess

class CliFetchHostNetworkAgents(CliAccess):
  
  def get(self, id):
    out = self.run("source openrc; neutron agent-list -D -fjson")
    out = self.binary2str(out)
    json_string = re.sub(r"\\n$", "", out)
    results = json.loads(json_string)
    for o in results:
      o["parent_id"] = o["host"] + "-vservices"
      o["parent_type"] = "host_object_type"
    return results
