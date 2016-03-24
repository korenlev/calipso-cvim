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
  
  def scan(self, obj, id_field = "id",
      limit_to_child_id = None, limit_to_child_type = None):
    ret = True
    types_children = []
    try:
      for t in self.types_to_fetch:
        if limit_to_child_type and t["type"] != limit_to_child_type:
          next
        children = self.scan_type(t, obj, id_field)
        if limit_to_child_id:
          children = [c for c in children if c[id_field] == limit_to_child_id]
        types_children.append({"type": t["type"], "children": children})
    except ValueError:
      return False
    if limit_to_child_id:
      t = types_children[0]
      children = t["children"]
      return children[0]
    return obj
  
  def scan_type(self, type_to_fetch, parent, id_field):
    if not parent:
      id = None
    else:
      id = str(parent[id_field])
      if id == None or not id.rstrip():
        raise ValueError("Object missing " + id_field + " attribute")
    fetcher = type_to_fetch["fetcher"]
    try:
      children_scanner = type_to_fetch["children_scanner"]
    except KeyError:
      children_scanner = None
    escaped_id = fetcher.escape(str(id)) if id else id
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
    environment = Scanner.environment
    children = []
    for o in results:
      o["environment"] = environment
      o["type"] = type_to_fetch["type"] if type_to_fetch["type"] else o["type"]
      try:
        parent_id_path = parent["id_path"]
        parent_name_path = parent["name_path"]
      except KeyError:
         parent_id_path = "/" + environment
         parent_name_path = "/" + environment
      try:
         # case of dynamic folder added by need
         master_parent_type = o["master_parent_type"]
         master_parent_id = o["master_parent_id"]
         folder = {
           "environment": parent["environment"],
           "parent_id": master_parent_id,
           "parent_type": master_parent_type,
           "id": o["parent_id"],
           "id_path": parent_id_path + "/" + o["parent_id"],
           "name_path": parent_name_path + "/" + o["parent_text"],
           "name": o["parent_id"],
           "type": o["parent_type"],
           "text": o["parent_text"]
         }
         Scanner.inventory.set(folder)
      except KeyError:
         pass

      o["id_path"] = parent_id_path + "/" + str(o["id"]).strip()
      try:
        name = o["text"]
      except KeyError:
        try:
          name = o["name"]
        except KeyError:
          name = o["id"]
      o["name_path"] = parent_name_path + "/" + name
      
      if "parent_id" not in o and parent:
        parent_id = str(parent["id"])
        o["parent_id"] = parent_id
        o["parent_type"] = parent["type"]
      Scanner.inventory.set(o)
      children.append(o)
      if children_scanner:        
        children_scanner.scan(o, child_id_field)
    return children
