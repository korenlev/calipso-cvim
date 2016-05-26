from cli_access import CliAccess
from inventory_mgr import InventoryMgr
from singleton import Singleton

class CliFetchVconnectors(CliAccess, metaclass=Singleton):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    host_id = id[:id.rindex('-')]
    host = self.inv.get_by_id(self.get_env(), host_id)
    if not host:
      print("Error: CliFetchVconnectors: host not found: " + host_id)
      return []
    if "host_type" not in host:
      print("Error: host does not have host_type: " + host_id + \
        ", host: " + str(host))
      return []
    host_types = host["host_type"]
    if "Network" not in host_types and "Compute" not in host_types:
      return []
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

  def add_links(self):
    vconnectors = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vconnector"
    })
    for vconnector in vconnectors:
      for interface in vconnector["interfaces"]:
        self.add_vnic_vconnector_link(vconnector, interface)
        self.add_vconnector_pnic_link(vconnector, interface)

  def add_vnic_vconnector_link(self, vconnector, interface):
      vnic = self.inv.get_by_id(self.get_env(), interface)
      if not vnic:
        return
      host = vnic["host"]
      source = vnic["_id"]
      source_id = vnic["id"]
      target = vconnector["_id"]
      target_id = vconnector["id"]
      link_type = "vnic-vconnector"
      link_name = vnic["mac_address"]
      state = "up" # TBD
      link_weight = 0 # TBD
      self.inv.create_link(self.get_env(), host, source, source_id, target, target_id,
        link_type, link_name, state, link_weight)

  def add_vconnector_pnic_link(self, vconnector, ifname):
    if not ifname.startswith("eth") and not ifname.startswith("eno"):
      return
    if "." in ifname:
      ifname = ifname[:ifname.index(".")]
    host = vconnector["host"]
    pnic = self.inv.find_items({
      "environment": self.get_env(),
      "type": "pnic",
      "host": vconnector["host"],
      "name": ifname
    })
    if not pnic:
      return
    pnic = pnic[0]
    source = pnic["_id"]
    source_id = pnic["id"]
    target = vconnector["_id"]
    target_id = vconnector["id"]
    link_type = "vconnector-pnic"
    link_name = pnic["name"]
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), host, source, source_id, target, target_id,
      link_type, link_name, state, link_weight)
