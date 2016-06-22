import re
import xmltodict

from cli_access import CliAccess
from inventory_mgr import InventoryMgr

class CliFetchInstanceVnics(CliAccess):

  def __init__(self):
    super(CliFetchInstanceVnics, self).__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    instance_uuid = id[:id.rindex('-')]
    instance = self.inv.get_by_id(self.get_env(), instance_uuid)
    if not instance:
      return []
    host = self.inv.get_by_id(self.get_env(), instance["host"])
    if "Compute" not in host["host_type"]:
      return []
    lines = self.run_fetch_lines("virsh list", instance["host"])
    del lines[:2] # remove header
    virsh_ids = [l.split()[0] for l in lines if l>""]
    results = []
    # Note: there are 2 ids here of instances with local names, which are
    # not connected to the data we have thus far for the instance
    # therefore, we will decide whether the instance is the correct one based
    # on comparison of the uuid in the dumpxml output
    for id in virsh_ids:
      results.extend(self.get_vnics_from_dumpxml(id, instance))
    return results

  def get_vnics_from_dumpxml(self, id, instance):
    xml_string = self.run("virsh dumpxml " + id, instance["host"])
    if not xml_string.strip():
      return []
    response = xmltodict.parse(xml_string)
    if instance["uuid"] != response["domain"]["uuid"]:
      # this is the wrong instance - skip it
      return []
    try:
      vnics = response["domain"]["devices"]["interface"]
    except KeyError:
      return []
    if isinstance(vnics, dict):
      vnics = [vnics]
    for v in vnics:
      v["name"] = v["target"]["@dev"]
      v["id"] =  v["name"]
      v["vnic_type"] = "instance_vnic"
      v["host"] = instance["host"]
      v["instance_id"] = instance["id"]
      v["instance_db_id"] = instance["_id"]
      v["mac_address"] = v["mac"]["@address"]
      v["source_bridge"] = v["source"]["@bridge"]
    return vnics

  def add_links(self):
    self.log.info("adding links of type: instance-vnic")
    vnics = self.inv.find_items({
      "environment": self.get_env(),
      "type": "vnic",
      "vnic_type": "instance_vnic"
    })
    for v in vnics:
      self.add_link_for_vnic(v)

  def add_link_for_vnic(self, v):
    instance = self.inv.get_by_id(self.get_env(), v["instance_id"])
    if "network_info" not in instance:
      self.log.warn("add_link_for_vnic: network_info missing in instance: %s ",
        instance["id"])
      return
    host = self.inv.get_by_id(self.get_env(), instance["host"])
    host_types = host["host_type"]
    if "Network" not in host_types:
      return []
    source = instance["_id"]
    source_id = instance["id"]
    target = v["_id"]
    target_id = v["id"]
    link_type = "instance-vnic"
    # find related network
    network_name = None
    for net in instance["network_info"]:
      if net["devname"] == v["id"]:
        network_name = net["network"]["label"]
        break
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), host["name"],
      source, source_id, target, target_id,
      link_type, network_name, state, link_weight)
