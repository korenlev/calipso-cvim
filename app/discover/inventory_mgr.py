from mongo_access import MongoAccess
from util import Util

class InventoryMgr(MongoAccess, Util):
  
  prettify = False
  
  def __init__(self):
    super(InventoryMgr, self).__init__()
    self.inv = MongoAccess.db["inventory"]

    
  def get(self, environment, item_type, item_id):
    if item_id and (item_id > ""):
      matches = self.inv.find({"environment": environment, "type": item_type, "id": item_id})
    else:
      matches = self.inv.find({"environment": environment, "type": item_type})
    return matches
  
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
      ret.append(doc)
    return ret
  
  def getSingle(self, environment, item_type, item_id):
    matches = self.inv.find({"environment": environment, "type": item_type, "id": item_id})
    if matches.len() == 0:
      raise(ValueError, "No matches for item: type=" + item_type + ", id=" + item_id)
    elif matches.len() > 1:
      raise(ValueError, "Found multiple matches for item: type=" + item_type + ", id=" + item_id)
    else:
      for doc in matches:
        return doc
  
  # item must contain properties 'environment', 'type' and 'id'
  def set(self, item):
    # make sure we have environment, type & id
    check(item, "environment")
    check(item, "type")
    check(item, "id")
    curr_item_matches = get(item["environment"], item["type"], item["id"])
    if curr_item_matches.len() > 0:
      update(curr_item_matches, item)
    else:
      self.inv.insert_one(item)
  
  def update(self, curr_item_matches, item):
    curr_item = curr_item_matches.first
    self.inv.find_one_and_update({"_id": curr_item["_id"]}, {"$set": item})
  
  def check(self, obj, field_name):
    arg = obj[field_name]
    if arg == None or not str(arg).rstrip():
      raise(ValueError, "Inventory item - the following field is not defined: " + field_name)
