from mongo_access import MongoAccess
from util import Util
from datetime import datetime

class InventoryMgr(MongoAccess, Util):
  
  prettify = False
  
  def __init__(self):
    super(InventoryMgr, self).__init__()
    self.inv = MongoAccess.db["inventory"]
    self.base_url_prefix = "/osdna_dev/discover.py?type=tree"

  # return single match
  def get_by_id(self, environment, item_id):
    matches = self.find({
      "environment": environment,
      "id": item_id
    })
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      doc["children_url"] = self.get_base_url(doc)
      return doc
    return ret

  def get_by_field(self, environment, item_type, field_name, field_value):
    if field_value and (not isinstance(field_value, str) or field_value > ""):
      matches = self.find({
        "environment": environment,
        "type": item_type,
        field_name: field_value
      })
    else:
      matches = self.find({
        "environment": environment,
        "type": item_type
      })
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      doc["children_url"] = self.get_base_url(doc)
      ret.append(doc)
    return ret
    
  def get(self, environment, item_type, item_id):
    ret = self.get_by_field(environment, item_type, "id", item_id)
    return ret
  
  def get_children(self, environment, item_type, parent_id):
    matches = []
    if parent_id and parent_id > "" and item_type == None:
      matches = self.find({"environment": environment, "parent_id": parent_id})
    else:
      if parent_id and parent_id > "":
        matches = self.find({"environment": environment, "type": item_type, "parent_id": parent_id})
      else:
        matches = self.find({"environment": environment, "type": item_type})
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      doc["children_url"] = self.get_base_url(doc)
      ret.append(doc)
    return ret
  
  def getSingle(self, environment, item_type, item_id):
    matches = self.find({"environment": environment, "type": item_type, "id": item_id})
    ret = []
    for doc in matches:
      doc["_id"] = str(doc["_id"])
      doc["children_url"] = self.get_base_url(doc)
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
    item["last_scanned"] = datetime.now()
    try:
      projects = item.pop("projects")
    except KeyError:
      projects = []
    obj_name = item["name_path"]
    obj_name = obj_name[obj_name.rindex('/')+1:]
    item["object_name"] = obj_name
    self.inv.update(
      {"environment": item["environment"],
       "type": item["type"], "id": item["id"]},
      {'$set': self.encode_mongo_keys(item)},
      upsert=True)
    if projects:
      self.inv.update(
        {"environment": item["environment"],
         "type": item["type"], "id": item["id"]},
        {'$addToSet': {"projects": {'$each': projects}}},
        upsert=True)
  
  def check(self, obj, field_name):
    arg = obj[field_name]
    if arg == None or not str(arg).rstrip():
      raise ValueError("Inventory item - the following field is not defined: " + field_name)

  def get_base_url(self, doc):
    return self.base_url_prefix + "&id=" + str(doc["id"])

  def find(self, search):
    matches = self.inv.find(search)
    decoded_matches = []
    for m in matches:
      decoded_matches.append(self.decode_mongo_keys(m))
    return decoded_matches
