from inventory_mgr import InventoryMgr
from fetcher import Fetcher

class FindLinksForVconnectors(Fetcher):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()

  def add_links(self):
    vconnectors = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vconnector"
    })
    self.log.info("adding links of type: vnic-vconnector, vconnector-pnic")
    for vconnector in vconnectors:
      for interface in vconnector["interfaces"].values():
        self.add_vnic_vconnector_link(vconnector, interface)
        self.add_vconnector_pnic_link(vconnector, interface)

  def add_vnic_vconnector_link(self, vconnector, interface):
      if isinstance(interface, str):
        # interface ID for OVS
        vnic = self.inv.get_by_id(self.get_env(), interface)
      else:
        # interface ID for VPP - match interface MAC address to vNIC MAC address
        if 'mac_address' not in interface:
          return
        vnic_mac = interface['mac_address']
        vnic = self.inv.get_by_field(self.get_env(), 'vnic',
          'mac_address', vnic_mac, get_single=True)
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
      attributes = {}
      if 'network' in vnic:
        attributes = {'network': vnic['network']}
        vconnector['network'] = vnic['network']
        self.inv.set(vconnector)
      self.inv.create_link(self.get_env(), host,
        source, source_id, target, target_id,
        link_type, link_name, state, link_weight, extra_attributes=attributes)

  def add_vconnector_pnic_link(self, vconnector, interface):
    ifname = interface['name'] if isinstance(interface, dict) else interface
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
    }, get_single=True)
    if not pnic:
      return
    source = vconnector["_id"]
    source_id = vconnector["id"]
    target = pnic["_id"]
    target_id = pnic["id"]
    link_type = "vconnector-pnic"
    link_name = pnic["name"]
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), host, source, source_id, target, target_id,
      link_type, link_name, state, link_weight)
