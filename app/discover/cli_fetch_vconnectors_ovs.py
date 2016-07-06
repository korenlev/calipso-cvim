from cli_fetch_vconnectors import CliFetchVconnectors

class CliFetchVconnectorsOvs(CliFetchVconnectors):

  def __init__(self):
    super().__init__()

  def get_vconnectors(self, host):
    host_id = host['id']
    lines = self.run_fetch_lines("brctl show", host_id)
    headers = ["bridge_name", "bridge_id", "stp_enabled", "interfaces"]
    headers_count = len(headers)
    # since we hard-coded the headers list, remove the headers line
    del lines[:1]

    # intefaces can spill to next line - need to detect that and add
    # them to the end of the previous line for our procesing
    fixed_lines = self.merge_ws_spillover_lines(lines)

    results = self.parse_cmd_result_with_whitespace(fixed_lines, headers, False)
    ret = []
    for doc in results:
      doc["id"] = doc.pop("bridge_id")
      doc["name"] = doc.pop("bridge_name")
      doc["host"] = host_id
      doc["connector_type"] = "bridge"
      if "interfaces" in doc:
        doc["interfaces"] = doc["interfaces"].split(",")
        ret.append(doc)
    return ret
