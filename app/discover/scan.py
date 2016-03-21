#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import cgi
import sys

from configuration import Configuration
from inventory_mgr import InventoryMgr
from scan_environment import ScanEnvironment

class ScanController:

  def __init__(self, ):
    self.default_env_name = "WebEX-Mirantis@Cisco"
    self.conf = Configuration()

  def get_scan_object(self, form):
    object_type = form.getvalue("type", "environment")
    module = object_type
    type_to_scan = module
    object_type= object_type.title().replace("_", "")
    env = form.getvalue("env", "WebEX-Mirantis@Cisco")
    object_id = form.getvalue("id", "WebEX-Mirantis@Cisco")
    id_field = "id"
    ret = {
        "module": "scan_" + module,
        "type_to_scan": type_to_scan,
        "scanner_class": "Scan" + object_type,
        "id": object_id,
        "id_field": id_field,
        "env": env
    }
    return ret

  def run(self):
    form = cgi.FieldStorage()
    what_to_scan = self.get_scan_object(form)
    env_name = what_to_scan["env"]
    self.conf.use_env(env_name)
    type_to_scan = what_to_scan["type_to_scan"]
    class_name = what_to_scan["scanner_class"]
    id = what_to_scan["id"]
    id_field = what_to_scan["id_field"]
    module = __import__(what_to_scan["module"])
    class_ = getattr(module, class_name)
    scanner = class_()
    scanner.set_env(env_name)
    results = scanner.scan({"type": type_to_scan, "id": id}, id_field)
    if isinstance(results, bool):
        response = {"success": False, "results": []}
        pass
    else:
        response = {"success": True, "results": results}
    return response

if __name__ == '__main__':
  scan_manager = ScanController()
  response = scan_manager.run()

  print("Content-type: application/json\n\n")
  print(response)
  print("\n")
