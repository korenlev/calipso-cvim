from cli_access import CliAccess
from inventory_mgr import InventoryMgr
from singleton import Singleton

class CliFetchVconnectors(CliAccess, metaclass=Singleton):

  def __init__(self):
    super(CliFetchVconnectors, self).__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    host_id = id[:id.rindex('-')]
    host = self.inv.get_by_id(self.get_env(), host_id)

    lines = self.run_fetch_lines("ssh " + host_id + " brctl show")
    headers = ["bridge_name", "bridge_id", "stp_enabled", "interfaces"]
    headers_count = len(headers)
    # since we hard-coded the headers list, remove the headers line
    del lines[:1]

    # intefaces can spill to next line - need to detect that and add
    # them to the end of the previous line for our procesing
    fixed_lines = self.merge_ws_spillover_lines(lines)

    results = self.parse_cmd_result_with_whitespace(fixed_lines, headers, False)
    for doc in results:
      doc["id"] = doc.pop("bridge_id")
      doc["name"] = doc.pop("bridge_name")
      doc["connector_type"] = "bridge"
      doc["interfaces"] = doc["interfaces"].split(",") if "interfaces" in doc \
        else []
    return results
