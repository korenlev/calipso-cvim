import bson

from mongo_access import MongoAccess
from util import Util
from datetime import datetime
from singleton import Singleton
from clique_finder import CliqueFinder

class InventoryMgr(MongoAccess, Util, metaclass=Singleton):
  
  prettify = False
  
  def __init__(self):
    super().__init__()
    self.coll = {}
    self.base_url_prefix = "/osdna_dev/discover.py?type=tree"
    self.clique_scanner = None

  def set_collection(self, coll_type, collection_name = ""):
    if coll_type != "inventory":
      collection_name = self.get_coll_name(coll_type)
    # do not allow setting the collection more than once
    if coll_type not in self.coll or not self.coll[coll_type]:
      self.log.info("using " + coll_type +" collection: " + collection_name)
      name = collection_name if collection_name else coll_type
      self.coll[coll_type] = MongoAccess.db[name]
      if coll_type == "inventory":
        self.inventory_col = name
    return self.coll[coll_type]

  def get_coll_name(self, coll_name):
    return self.inventory_col.replace("inventory", coll_name) \
      if self.inventory_col.startswith("inventory") \
      else self.inventory_col + "_" + coll_name

  def set_inventory_collection(self, inventory_collection = ""):
    self.inv = self.set_collection("inventory", inventory_collection)
    self.links = self.set_collection("links")
    self.set_collection("link_types")
    self.set_collection("clique_types")
    self.set_collection("clique_constraints")
    self.set_collection("cliques")

  def clear(self, scan_plan):
      col_to_skip = ["link_types", "clique_types", "clique_constraints"]
      if scan_plan["links_only"] or scan_plan["cliques_only"]:
        col_to_skip.append("inventory")
      if scan_plan["inventory_only"] or scan_plan["cliques_only"]:
        col_to_skip.append("links")
      if scan_plan["inventory_only"] or scan_plan["links_only"]:
        col_to_skip.append("cliques")
      for c in [c for c in self.coll if c not in col_to_skip]:
        col = self.coll[c]
        self.log.info("clearing collection: " + col.full_name)
        col.delete_many({}) # delete all documents from the collection

  # return single match
  def process_results(self, raw_results, get_single=False):
    ret = []
    for doc in raw_results:
      doc["_id"] = str(doc["_id"])
      doc["children_url"] = self.get_base_url(doc)
      if get_single:
        return doc
      ret.append(doc)
    return ret

  # return single match
  def get_by_id(self, environment, item_id):
    matches = self.find({
      "environment": environment,
      "id": item_id
    })
    return self.process_results(matches, True)

  # return matches for ID in list of values
  def get_by_ids(self, environment, ids_list):
    matches = self.find({
      "environment": environment,
      "id": {"$in": ids_list}
    })
    return self.process_results(matches)

  def get_by_field(self, environment, item_type, field_name, field_value,
      get_single=False):
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
    return self.process_results(matches, get_single=get_single)
    
  def get(self, environment, item_type, item_id, get_single=False):
    ret = self.get_by_field(environment, item_type, "id", item_id,
      get_single=get_single)
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
    return self.process_results(matches)
  
  def get_single(self, environment, item_type, item_id):
    matches = self.find({"environment": environment, "type": item_type, "id": item_id})
    if len(matches) > 1:
      raise ValueError("Found multiple matches for item: type=" + item_type + ", id=" + item_id)
    if len(matches) == 0:
      raise ValueError("No matches for item: type=" + item_type + ", id=" + item_id)
    ret = self.process_results(matches)
    return ret[0]
  
  # item must contain properties 'environment', 'type' and 'id'
  def set(self, item):
    mongo_id = None
    if "_id" in item:
      mongo_id = item.pop("_id", None)

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
    item['object_name'] = item['object_name'] if 'object_name' in item \
      else obj_name
    self.set_inventory_collection() # make sure we have it set
    find_tuple = {"environment": item["environment"],
       "type": item["type"], "id": item["id"]}
    self.inv.update_one(find_tuple,
      {'$set': self.encode_mongo_keys(item)},
      upsert=True)
    if mongo_id:
      # restore original mongo ID of document, in case we need to use it
      item['_id'] = mongo_id
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

  # note: to use general find, call find_items() which also does process_results
  def find(self, search, projection = None, get_single=False):
    matches = self.inv.find(search, projection=projection)
    decoded_matches = []
    for m in matches:
      decoded_matches.append(self.decode_mongo_keys(m))
    return decoded_matches

  def find_items(self, search, projection = None, get_single=False):
    results = self.find(search, projection)
    return self.process_results(results, get_single=get_single)

  # record a link between objects in the inventory, to be used in graphs
  # parameters -
  # environment: name of environment
  # host: name of host
  # source: node mongo _id
  # source_id: node id value of source node
  # target: node mongo _id
  # target_id: node id value of target node
  # link_type: string showing types of connected objects, e.g. "instance-vnic"
  # link_name: label for the link itself
  # state: up/down
  # link_weight: integer, position/priority for graph placement
  # source_label, target_label: labels for the ends of the link (optional)
  def create_link(self, env, host, src, source_id, target, target_id,
      link_type, link_name, state, link_weight,
      source_label = "", target_label = "",
      extra_attributes = {}):
    s = bson.ObjectId(src)
    t = bson.ObjectId(target)
    link = {
      "environment": env,
      "host": host,
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

  def get_clique_finder(self):
    if not self.clique_scanner:
      self.clique_scanner = CliqueFinder(self.inv, self.links,
        self.coll["clique_types"],
        self.coll["clique_constraints"],
        self.coll["cliques"])
    return self.clique_scanner

  def scan_cliques(self, environment):
    clique_scanner = self.get_clique_finder()
    clique_scanner.find_cliques()

  def values_replace_in_object(self, o, values_replacement):
    for k in values_replacement.keys():
      if k not in o:
        continue
      repl = values_replacement[k]
      if 'from' not in repl or 'to' not in repl:
        continue
      o[k] = o[k].replace(repl['from'], repl['to'])
      self.set(o)

  # perform replacement of substring in values of objects in the inventory
  # input:
  # - search: dict with search parametes
  # - values_replacement: dict,
  #     - keys: names of keys for which to replace the values
  #     - values: dict with "from" (value to be replaced) and "to" (new value)
  def values_replace(self, search, values_replacement):
    for doc in self.inv.find(search):
      self.values_replace_in_object(doc, values_replacement)

  def delete(self, coll, filter):
    collection = self.coll[coll]
    if not collection:
      self.log.warn('delete(): collection not found - ' + coll)
      return
    result = collection.delete_many(filter)
    count = result.deleted_count
    self.log.info('delete(): ' + ('deleted ' + str(count) + ' documents'
      if count else 'no matching documents'))
    return count

