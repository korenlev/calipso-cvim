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
    self.instance = self.inv.get_by_id(self.get_env(), instance_uuid)
    if not self.instance:
      return []
    instance = self.instance
    lines = self.run_fetch_lines("virsh list", instance["host"])
    del lines[:2] # remove header
    virsh_ids = [l.split()[0] for l in lines if l>""]
    results = []
    # Note: there are 2 ids here of instances with local names, which are
    # not connected to the data we have thus far for the instance
    # therefore, we will decide whether the instance is the correct one based
    # on comparison of the uuid in the dumpxml output
    for id in virsh_ids:
      results.extend(self.get_vnics_from_dumpxml(id))
    return results

  def get_vnics_from_dumpxml(self, id):
    instance = self.instance
    xml_string = self.run("virsh dumpxml " + id, instance["host"])
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
      v["vnic_type"] = "instance-vnic"
      v["host"] = instance["host"]
      v["instance_id"] = instance["uuid"]
      v["mac_address"] = v["mac"]["@address"]
      v["source_bridge"] = v["source"]["@bridge"]
    return vnics

  # handle links creation after writing of vnic to DB
  def add_links(self, item, doc_id):
    self.add_instance_vnic_link(item, doc_id)

  def add_instance_vnic_link(self, item, item_mongo_id):
    instance = self.instance
    source = instance["_id"]
    source_id = instance["id"]
    target = item_mongo_id
    target_id = item["id"]
    link_type = "instance-vnic"
    # find related network
    network_name = None
    for net in instance["network_info"]:
      if net["devname"] == item["id"]:
        network_name = net["network"]["label"]
        break
    state = "up" # TBD
    link_weight = 0 # TBD
    self.inv.create_link(self.get_env(), source, source_id, target, target_id,
      link_type, network_name, state, link_weight)
