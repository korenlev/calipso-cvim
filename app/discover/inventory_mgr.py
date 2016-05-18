from mongo_access import MongoAccess
import bson
from util import Util
from datetime import datetime
from singleton import Singleton

class InventoryMgr(MongoAccess, Util, metaclass=Singleton):
  
  prettify = False
  
  def __init__(self):
    super(InventoryMgr, self).__init__()
    self.coll = {}
    self.base_url_prefix = "/osdna_dev/discover.py?type=tree"

  def set_collection(self, coll_type, collection_name):
    # do not allow setting the collection more than once
    if coll_type not in self.coll or not self.coll[coll_type]:
      print("using " + coll_type +" collection: " + collection_name)
      name = collection_name if collection_name else coll_type
      self.coll[coll_type] = MongoAccess.db[name]
    return self.coll[coll_type]

  def set_inventory_collection(self, inventory_collection = ""):
    self.inv = self.set_collection("inventory", inventory_collection)

  def set_links_collection(self, links_collection = ""):
    self.links = self.set_collection("links", links_collection)

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
  def set(self, item, fetcher = None):
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
    self.set_inventory_collection() # make sure we have it set
    find_tuple = {"environment": item["environment"],
       "type": item["type"], "id": item["id"]}
    update_result = self.inv.update_one(find_tuple,
      {'$set': self.encode_mongo_keys(item)},
      upsert=True)
    modify_count = update_result.raw_result["n"]
    if fetcher and modify_count and hasattr(fetcher, "add_links"):
      # add link if possible
      doc = self.inv.find_one(find_tuple)
      if doc:
        fetcher.add_links(item, doc["_id"])
    if projects:
      self.inv.update_one(find_tuple,
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

  # record a link between objects in the inventory, to be used in graphs
  # parameters -
  # environment: name of environment
  # source: node mongo _id
  # source_id: node id value of source node
  # target: node mongo _id
  # target_id: node id value of target node
  # link_type: string showing types of connected objects, e.g. "instance-vnic"
  # link_name: label for the link itself
  # state: up/down
  # link_weight: integer, position/priority for graph placement
  # source_label, target_label: labels for the ends of the link (optional)
  def create_link(self, env, src, source_id, target, target_id,
      link_type, link_name, state, link_weight,
      source_label = "", target_label = "",
      extra_attributes = {}):
    self.set_links_collection() # make sure we have it set
    s = bson.ObjectId(src)
    t = bson.ObjectId(target)
    link = {
      "environment": env,
      "source": s,
      "source_id": source_id,
      "target": t,
      "target_id": target_id,
      "link_type": link_type,
      "link_name": link_name,
      "state": state,
      "link_weight": link_weight,
      "source_label": source_label,
      "target_label": target_label,
      "attributes": extra_attributes
    }
    find_tuple = {
      "environment": env,
      "source_id": source_id,
      "target_id": target_id
    }
    self.links.update_one(find_tuple,
      {'$set': self.encode_mongo_keys(link)},
      upsert=True)
