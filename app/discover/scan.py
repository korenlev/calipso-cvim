#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import cgi
import sys
import re

from configuration import Configuration
from inventory_mgr import InventoryMgr
from scan_environment import ScanEnvironment

class ScanController:

  default_env = "WebEX-Mirantis@Cisco"

  def __init__(self, ):
    self.conf = Configuration()
    self.inv = InventoryMgr()

  def get_scan_object(self, form):
    object_type = form.getvalue("type", "environment")
    module = object_type
    type_to_scan = module
    scan_self = form.getvalue("scan_self", "")
    if scan_self:
      scan_self = scan_self.lower() == "true"
    else:
      scan_self = object_type != "environment"      
    child_id = None
    child_type = None

    object_type = object_type.title().replace("_", "")
    env = form.getvalue("env", ScanController.default_env)
    object_id = form.getvalue("id", ScanController.default_env)
    if scan_self:
      child_id = object_id
      child_type = type_to_scan
      object_id = form.getvalue("parent_id", "")
      type_to_scan = form.getvalue("parent_type", "")
      if re.match(r'^.*_object_type$', type_to_scan):
        module = child_type + "s_root"
      else:
        module = type_to_scan
      object_type = module.title().replace("_", "")
    if module == "environment":
      obj = {"id": env}
    else:
      # fetch object from inventory
      matches = self.inv.get(env, type_to_scan, object_id)
      if len(matches) == 0:
        raise ValueError("No match for object ID: " + object_id)
      obj = matches[0]

    id_field = form.getvalue("id_field",
        "name" if module == "projects_root" else "id")
    ret = {
        "module": "scan_" + module,
        "scan_self": scan_self,
        "scanner_class": "Scan" + object_type,
        "type": type_to_scan,
        "obj": obj,
        "id_field": id_field,
        "child_type": child_type,
        "child_id": child_id,
        "env": env
    }
    return ret

  def run(self):
    form = cgi.FieldStorage()
    what_to_scan = self.get_scan_object(form)
    env_name = what_to_scan["env"]
    self.conf.use_env(env_name)
    class_name = what_to_scan["scanner_class"]
    module = __import__(what_to_scan["module"])
    class_ = getattr(module, class_name)
    scanner = class_()
    scanner.set_env(env_name)
    results = scanner.scan(
      what_to_scan["obj"],
      what_to_scan["id_field"],
      what_to_scan["child_id"],
      what_to_scan["child_type"])
    scanner.scan_from_queue()
    response = {"success": not isinstance(results, bool),
                "results": [] if isinstance(results, bool) else results}
    return response

if __name__ == '__main__':
  scan_manager = ScanController()
  response = scan_manager.run()

  print("Content-type: application/json\n\n")
  print(response)
  print("\n")
