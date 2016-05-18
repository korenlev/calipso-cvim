# base class for scanners

from inventory_mgr import InventoryMgr
from util import Util
from fetcher import Fetcher

import queue
import json
import re

class Scanner(Util, Fetcher):
  
  inventory = None
  environment = None
  root_patern = None
  scan_queue = queue.Queue()
  scan_queue_track = {}
  
  def __init__(self, types_to_fetch):
    super(Scanner, self).__init__()
    self.types_to_fetch = types_to_fetch
    if not Scanner.inventory:
      Scanner.inventory = InventoryMgr()
  
  def scan(self, obj, id_field = "id",
      limit_to_child_id = None, limit_to_child_type = None):
    ret = True
    types_children = []
    try:
      for t in self.types_to_fetch:
        if limit_to_child_type and t["type"] != limit_to_child_type:
          continue
        children = self.scan_type(t, obj, id_field)
        if limit_to_child_id:
          children = [c for c in children if c[id_field] == limit_to_child_id]
        types_children.append({"type": t["type"], "children": children})
    except ValueError as e:
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
    fetcher.set_env(self.get_env())
    try:
      children_scanner = type_to_fetch["children_scanner"]
      children_scanner.set_env(self.get_env())
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
    environment = self.get_env()
    children = []
    for o in results:
      o["id"] = str(o["id"])
      o["environment"] = environment
      o["type"] = type_to_fetch["type"] if type_to_fetch["type"] else o["type"]
      try:
        o["show_in_tree"] = type_to_fetch["show_in_tree"]
      except KeyError:
        o["show_in_tree"] = True
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
         master_parent = self.inventory.get_by_id(self.get_env(), master_parent_id)
         if not master_parent:
           print("ERROR: failed to find master parent " + master_parent_id)
           continue
         folder = {
           "environment": parent["environment"],
           "parent_id": master_parent_id,
           "parent_type": master_parent_type,
           "id": o["parent_id"],
           "id_path": master_parent["id_path"] + "/" + o["parent_id"],
           "name_path": master_parent["name_path"] + "/" + o["parent_text"],
           "name": o["parent_id"],
           "type": o["parent_type"],
           "text": o["parent_text"]
         }
         # remove master_parent_type & master_parent_id after use,
         # as they're there just ro help create the dynamic folder
         o.pop("master_parent_type", True)
         o.pop("master_parent_id", True)
         Scanner.inventory.set(folder)
      except KeyError:
         pass

      if "text" in o and o["text"]:
        name = o["text"]
      elif "name" in o and o["name"]:
        name = o["name"]
      else:
        name = o["id"]
      o["name"] = name
     
      if "parent_id" not in o and parent:
        parent_id = parent["id"]
        o["parent_id"] = parent_id
        o["parent_type"] = parent["type"]
      elif "parent_id" in o and o["parent_id"] != parent["id"]:
        # using alternate parent - fetch parent path from inventory
        parent_obj = Scanner.inventory.get_by_id(environment, o["parent_id"])
        if parent_obj:
          parent_id_path = parent_obj["id_path"]
          parent_name_path = parent_obj["name_path"]
      o["id_path"] = parent_id_path + "/" + o["id"].strip()
      o["name_path"] = parent_name_path + "/" + name

      # keep list of projects that an object is in
      associated_projects = []
      keys_to_remove = []
      for k in o:
        if k.startswith("in_project-"):
          proj_name = k[k.index('-')+1:]
          associated_projects.append(proj_name)
          keys_to_remove.append(k)
      for k in keys_to_remove:
          o.pop(k)
      if len(associated_projects) > 0:
        projects = o["projects"] if "projects" in o.keys() else []
        projects.extend(associated_projects)
        if projects:
          o["projects"] = projects

      if "create_object" not in o or o["create_object"]:
        Scanner.inventory.set(o, fetcher)
      children.append(o)
      if children_scanner:
        self.queue_for_scan(o, child_id_field, children_scanner)
    return children

  # scanning queued items, rather than going depth-first (DFS)
  # this is done to allow collecting all required data for objects
  # before continuing to next level
  # for example, get host ID from API os-hypervisors call, so later
  # we can use this ID in the "os-hypervisors/<ID>/servers" call
  def queue_for_scan(self, o, child_id_field, children_scanner):
    if o["id"] in Scanner.scan_queue_track:
      return
    Scanner.scan_queue_track[o["type"] + ";" + o["id"]] = 1
    Scanner.scan_queue.put({"object": o,
      "child_id_field": child_id_field, "scanner": children_scanner})

  def scan_from_queue(self):
    while not Scanner.scan_queue.empty():
      item = Scanner.scan_queue.get()
      scanner = item["scanner"]
      scanner.scan(item["object"], item["child_id_field"])

