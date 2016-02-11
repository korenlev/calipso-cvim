import mongo_access
import util

class InventoryMgr(MongoAccess, Util):
  
  prettify = False
  
  def get(self, environment, item_type, item_id):
    if item_id and (item_id > ""):
      matches = db.inventory.find({"environment": environment, "type": item_type, "id": item_id})
    else:
      matches = db.inventory.find({"environment": environment, "type": item_type})
    return matches
  
  def get_children(self, environment, item_type, parent_id):
    matches = []
    if parent_id and parent_id > "":
      matches = db.inventory.find({"environment": environment, "type": item_type, "parent_id": parent_id})
    else:
      matches = db.inventory.find({"environment": environment, "type": item_type})
    return matches
  
  def getSingle(self, environment, item_type, item_id):
    matches = db.inventory.find({"environment": environment, "type": item_type, "id": item_id})
    if matches.count() == 0:
      raise IndexError, "No matches for item: type=" + item_type + ", id=" + item_id
    elif matches.count() > 1:
      raise IndexError, "Found multiple matches for item: type=" + item_type + ", id=" + item_id
    else:
      for doc in matches:
        return doc
    end
  end
  
  # item must contain properties 'environment', 'type' and 'id'
  def set(self, item):
    # make sure we have environment, type & id
    check(item, "environment")
    check(item, "type")
    check(item, "id")
    curr_item_matches = get(item["environment"], item["type"], item["id"])
    if curr_item_matches.count() > 0:
      update(curr_item_matches, item)
    else:
      db.inventory.insert_one(item)
  
  def update(self, curr_item_matches, item):
    curr_item = curr_item_matches.first
    db.inventory.find_one_and_update({"_id": curr_item["_id"]}, {"$set": item})
  end
  
  def check(self, obj, field_name):
    arg = obj[field_name]
    if arg == None or not str(arg).rstrip():
      raise(ValueError, "Inventory item - the following field is not defined: " + field_name)
