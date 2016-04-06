import json
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
    matching_items = self.inv.get_by_field(self.get_env(), "instance", "uuid",
      instance_uuid)
    if len(matching_items) == 0:
      return []
    try:
      instance_ip_address = matching_items[0]["ip_address"]
    except KeyError:
      return []
    cmd = "ssh -o StrictHostKeyChecking=no "
    cmd += instance_ip_address + " virsh list"
    lines = self.run_fetch_lines(cmd)
    del lines[:2] # remove header
    virsh_ids = [l.split()[0] for l in lines if l>""]
    results = []
    for id in virsh_ids:
      results.extend(self.get_vnics_from_dumpxml(instance_ip_address, id))
    return results

  def get_vnics_from_dumpxml(self, ip_address, id):
    cmd = "ssh " + ip_address + " virsh dumpxml " + id
    xml_string = self.run(cmd)
    response = xmltodict.parse(xml_string)
    try:
      vnics = response["domain"]["devices"]["interface"]
    except KeyError:
      return []
    if isinstance(vnics, dict):
      vnics = [vnics]
    for v in vnics:
      v["name"] = v["target"]["@dev"]
      v["id"] =  v["name"]
      v["mac_address"] = v["mac"]["@address"]
      v["source_bridge"] = v["source"]["@bridge"]
    return vnics
