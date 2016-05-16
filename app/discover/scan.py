#!/usr/bin/env python3

# Scan an object and insert/update in the inventory

# phase 2: either scan default environment, or scan specific object

import cgi
import sys
import os
import argparse

from configuration import Configuration
from inventory_mgr import InventoryMgr
from scan_environment import ScanEnvironment

class ScanController:

  default_env = "WebEX-Mirantis@Cisco"

  def __init__(self):
    self.conf = Configuration()
    self.inv = InventoryMgr()

  def get_scan_plan(self):
    form = cgi.FieldStorage()
    if "REQUEST_METHOD" in os.environ:
      return self.get_scan_object_from_cgi()
    # try to read scan plan from command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cgi", nargs="?", type=bool, default=False,
      help="read argument from CGI (true/false) \n(default: false)")
    parser.add_argument("-e", "--env", nargs="?", type=str,
      default=self.default_env,
      help="name of environment to scan \n(default: " + self.default_env + ")")
    parser.add_argument("-t", "--type", nargs="?", type=str,
      default="environment",
      help="type of object to scan \n(default: environment)")
    parser.add_argument("-y", "--inventory", nargs="?", type=str,
      default="inventory",
      help="name of inventory collection \n(default: 'inventory')")
    parser.add_argument("-s", "--scan_self", nargs="?", type=bool, default=False,
      help="scan changes to a specific object \n(default: false)")
    parser.add_argument("-i", "--id", nargs="?", type=str,
      default=ScanController.default_env,
      help="ID of object to scan (when scan_self=true)")
    parser.add_argument("-p", "--parent_id", nargs="?", type=str, default="",
      help="ID of parent object (when scan_self=true)")
    parser.add_argument("-a", "--parent_type", nargs="?", type=str, default="",
      help="type of parent object (when scan_self=true)")
    parser.add_argument("-f", "--id_field", nargs="?", type=str, default="id",
      help="name of ID field (when scan_self=true) \n(default: 'id', use 'name' for projects)")
    args = parser.parse_args()
    plan = {
      "object_type": args.type,
      "env": args.env,
      "object_id": args.id,
      "parent_id": args.parent_id,
      "type_to_scan": args.parent_type,
      "id_field": args.id_field,
      "scan_self": args.scan_self,
      "child_type": None,
      "child_id": None,
      "inventory_collection": args.inventory
    }
    return self.prepare_scan_plan(plan)

  def get_scan_object_from_cgi(self):
    object_type = form.getvalue("type", "environment")
    env = form.getvalue("env", ScanController.default_env)
    object_id = form.getvalue("id", ScanController.default_env)
    object_id = form.getvalue("parent_id", "")
    type_to_scan = form.getvalue("parent_type", "")
    id_field = form.getvalue("id_field", "id")
    scan_self = form.getvalue("scan_self", "")
    inventory_collection = form.getvalue("inventory_collection", "inventory")
    return self.prepare_scan_plan(plan)

  def prepare_scan_plan(self, plan):
    self.inv.set_inventory_collection(plan["inventory_collection"])
    module = plan["object_type"]
    if not plan["scan_self"]:
      plan["scan_self"] = plan["object_type"] != "environment"
    plan["child_type"] = None

    plan["object_type"] = plan["object_type"].title().replace("_", "")
    if plan["scan_self"]:
      child_id = plan["object_id"]
      plan["child_type"] = plan["type_to_scan"]
      if plan["type_to_scan"].endswith("_object_type"):
        module = plan["child_type"] + "s_root"
      else:
        module = plan["type_to_scan"]
      plan["object_type"] = module.title().replace("_", "")
    if module == "environment":
      plan["obj"] = {"id": plan["env"]}
    else:
      # fetch object from inventory
      obj = self.inv.get_by_id(plan["env"], plan["object_id"])
      if not obj:
        raise ValueError("No match for object ID: " + plan["object_id"])
      plan["obj"] = obj

    plan["scanner_class"] = "Scan" + plan["object_type"]
    plan["module_file"] = "scan_" + module
    return plan


  def run(self):
    scan_plan = self.get_scan_plan()
    env_name = scan_plan["env"]
    self.conf.use_env(env_name)
    class_name = scan_plan["scanner_class"]
    module = __import__(scan_plan["module_file"])
    class_ = getattr(module, class_name)
    scanner = class_()
    scanner.set_env(env_name)
    results = scanner.scan(
      scan_plan["obj"],
      scan_plan["id_field"],
      scan_plan["child_id"],
      scan_plan["child_type"])
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
