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
    lines = self.run_fetch_lines("virsh list", instance["host"])
    del lines[:2] # remove header
    virsh_ids = [l.split()[0] for l in lines if l>""]
    results = []
    # Note: there are 2 ids here of instances with local names, which are
    # not connected to the data we have thus far for the instance
    # therefore, we will decide whether the instance is the correct one based
    # on comparison of the uuid in the dumpxml output
    for id in virsh_ids:
      results.extend(self.get_vnics_from_dumpxml(instance, id))
    return results

  def get_vnics_from_dumpxml(self, instance, id):
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
      v["vnic_type"] = "instance_vnic"
      v["host"] = instance["host"]
      v["mac_address"] = v["mac"]["@address"]
      v["source_bridge"] = v["source"]["@bridge"]
    return vnics
