from inventory_mgr import InventoryMgr
from fetcher import Fetcher

class FindLinksForVserviceVnics(Fetcher):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()

  def add_links(self):
    self.log.info("adding links of type: vservice-vnic")
    vnics = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vnic",
      "vnic_type": "vservice_vnic"
    })
    for v in vnics:
      self.add_link_for_vnic(v)

  def add_link_for_vnic(self, v):
    host = self.inv.get_by_id(self.get_env(), v["host"])
    if "Network" not in host["host_type"]:
      return
    cidr = v["cidr"]
    network = self.inv.get_by_id(self.get_env(), v["network"])
    vservice_id = v["parent_id"]
    vservice_id = vservice_id[:vservice_id.rindex('-')]
    vservice = self.inv.get_by_id(self.get_env(), vservice_id)
    source = vservice["_id"]
    source_id = vservice_id
    target = v["_id"]
    target_id = v["id"]
    link_type = "vservice-vnic"
    link_name = network["name"]
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), v["host"], source, source_id,
      target, target_id, link_type, link_name, state, link_weight)

  def get_net_size(self, netmask):
    binary_str = ''
    for octet in netmask:
      binary_str += bin(int(octet))[2:].zfill(8)
    return str(len(binary_str.rstrip('0')))

  # find CIDR string by IP address and netmask
  def get_cidr_for_vnic(self, vnic):
    ipaddr = vnic["IP Address"].split('.')
    netmask = vnic["netmask"].split('.')

    # calculate network start
    net_start = []
    for pos in range(0,4):
      net_start.append(str(int(ipaddr[pos]) & int(netmask[pos])))

    cidr_string = '.'.join(net_start) + '/'
    cidr_string = cidr_string + self.get_net_size(netmask)
    return cidr_string
