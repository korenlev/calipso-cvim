# base class for scanners

from inventory_mgr import InventoryMgr
from util import Util

import json
import re

class Scanner(Util):
  
  inventory = None
  environment = None
  root_patern = None
  
  def __init__(self, types_to_fetch):
    self.types_to_fetch = types_to_fetch
    if not Scanner.inventory:
      Scanner.inventory = InventoryMgr()
  
  def set_env(self, env):
    Scanner.environment = env
  
  def scan(self, obj, id_field):
    self.obj_to_scan = obj
    for t in self.types_to_fetch:
      self.scan_type(t, obj, id_field)
  
  def scan_type(self, type_to_fetch, parent, id_field):
    if not self.obj_to_scan:
      self.id = None
    elif id_field == "name":
      self.id = str(self.obj_to_scan["name"])
    else:
      self.id = str(self.obj_to_scan["id"])
    if self.obj_to_scan and (self.id == None or not self.id.rstrip()):
      raise ValueError("Object missing " + id_field + " attribute")
    fetcher = type_to_fetch["fetcher"]
    try:
      children_scanner = type_to_fetch["children_scanner"]
    except KeyError:
      children_scanner = None
    escaped_id = fetcher.escape(str(self.id)) if self.id else self.id
    db_results = fetcher.get(escaped_id)
    
    if isinstance(db_results, dict):
      results = db_results["rows"] if db_results["rows"] else [db_results]
    elif isinstance(db_results, str):
      results = json.loads(db_results)
    else:
      results = db_results
    try:
      child_id_field = type_to_fetch["object_id_to_use_in_child"]
    except KeyError:
      child_id_field = "id"
    for o in results:
      o["environment"] = Scanner.environment
      o["type"] = type_to_fetch["type"] if type_to_fetch["type"] else o["type"]
      try:
         # case of dynamic folder added by need
         master_parent_type = o["master_parent_type"]
         master_parent_id = o["master_parent_id"]
         folder = {
           "parent_id": master_parent_id,
           "parent_type": master_parent_type,
           "id": o["parent_id"],
           "name": o["parent_id"],
           "type": o["parent_type"],
           "text": o["parent_text"]
         }
         Scanner.inventory.set(folder)
      except KeyError:
         pass

      if "parent_id" not in o and parent:
        parent_id = str(parent["id"])
        o["parent_id"] = parent_id
        o["parent_type"] = parent["type"]
      Scanner.inventory.set(o)
      if children_scanner:
        children_scanner.scan(o, child_id_field)
