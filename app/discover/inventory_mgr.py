from mongo_access import MongoAccess
from util import Util

class InventoryMgr(MongoAccess, Util):
  
  prettify = False
  
  def __init__(self):
    super(InventoryMgr, self).__init__()
    self.inv = MongoAccess.db["inventory"]

    
  def get(self, environment, item_type, item_id):
    if item_id and (not isinstance(item_id, str) or item_id > ""):
      matches = self.inv.find({"environment": environment, "type": item_type, "id": item_id})
    else:
      matches = self.inv.find({"environment": environment, "type": item_type})
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      base_url = "/osdna_dev/discover.py?"
      url = base_url + "type=tree&parent_type=" + doc["type"] + "&id=" + str(doc["id"])
      doc["children_url"] = url
      ret.append(doc)
    return ret
  
  def get_children(self, environment, item_type, parent_id):
    matches = []
    if parent_id and parent_id > "" and item_type == None:
      matches = self.inv.find({"environment": environment, "parent_id": parent_id})
    else:
      if parent_id and parent_id > "":
        matches = self.inv.find({"environment": environment, "type": item_type, "parent_id": parent_id})
      else:
        matches = self.inv.find({"environment": environment, "type": item_type})
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      base_url = "/osdna_dev/discover.py?"
      url = base_url + "type=tree&parent_type=" + doc["type"] + "&id=" + doc["id"]
      doc["children_url"] = url
      ret.append(doc)
    return ret
  
  def getSingle(self, environment, item_type, item_id):
    matches = self.inv.find({"environment": environment, "type": item_type, "id": item_id})
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      base_url = "/osdna_dev/discover.py?"
      url = base_url + "type=tree&parent_type=" + doc["type"] + "&id=" + doc["id"]
      doc["children_url"] = url
      ret.append(doc)
      if len(ret) > 1:
        raise ValueError("Found multiple matches for item: type=" + item_type + ", id=" + item_id)
    if len(ret) == 0:
      raise ValueError("No matches for item: type=" + item_type + ", id=" + item_id)
    return ret[0]
  
  # item must contain properties 'environment', 'type' and 'id'
  def set(self, item):
    # make sure we have environment, type & id
    self.check(item, "environment")
    self.check(item, "type")
    self.check(item, "id")
    curr_item_matches = self.get(item["environment"], item["type"], item["id"])
    if len(curr_item_matches) > 0:
      self.update(curr_item_matches, item)
    else:
      self.inv.insert_one(item)
  
  def update(self, curr_item_matches, item):
    curr_item = curr_item_matches[0]
    self.inv.find_one_and_update({"_id": curr_item["_id"]}, {"$set": item})
  
  def check(self, obj, field_name):
    arg = obj[field_name]
    if arg == None or not str(arg).rstrip():
      raise ValueError("Inventory item - the following field is not defined: " + field_name)
