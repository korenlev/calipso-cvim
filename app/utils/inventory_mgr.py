from datetime import datetime

import bson

from utils.constants import EnvironmentFeatures
from utils.mongo_access import MongoAccess
from utils.singleton import Singleton


def inv_initialization_required(func):
    def decorated(self, *args, **kwargs):
        if self.inventory_collection is None:
            raise TypeError("Inventory collection is not set.")
        return func(self, *args, **kwargs)
    return decorated


class InventoryMgr(MongoAccess, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.inventory_collection = None
        self.inventory_collection_name = None
        self.collections = {}
        self.base_url_prefix = "/calipso_dev/discover.py?type=tree"
        self.monitoring_setup_manager = None

    def set_collection(self, collection_type, collection_name=""):

        # do not allow setting the collection more than once
        if not self.collections.get(collection_type):
            if collection_type != "inventory":
                collection_name = self.get_coll_name(collection_type)

            self.log.info("using " + collection_type + " collection: " +
                          collection_name)

            name = collection_name if collection_name else collection_type
            self.collections[collection_type] = MongoAccess.db[name]

            if collection_type == "inventory":
                self.inventory_collection_name = name

        return self.collections[collection_type]

    def get_coll_name(self, coll_name):
        if not self.inventory_collection_name:
            raise TypeError("inventory_collection_name is not set")

        return self.inventory_collection_name.replace("inventory", coll_name) \
            if self.inventory_collection_name.startswith("inventory") \
            else self.inventory_collection_name + "_" + coll_name

    def set_collections(self, inventory_collection=""):
        self.inventory_collection = self.set_collection("inventory",
                                                        inventory_collection)
        self.set_collection("links")
        self.set_collection("link_types")
        self.set_collection("clique_types")
        self.set_collection("clique_constraints")
        self.set_collection("cliques")
        self.set_collection("monitoring_config")
        self.set_collection("constants")
        self.set_collection("scans")
        self.set_collection("messages")
        self.set_collection("environments_config")
        self.set_collection("supported_environments")

    def clear(self, scan_plan):
        if scan_plan.inventory_only:
            collections = {"inventory"}
        elif scan_plan.links_only:
            collections = {"links"}
        elif scan_plan.cliques_only:
            collections = {"cliques"}
        else:
            collections = {"inventory", "links", "cliques"}

        env_cond = {} if scan_plan.clear_all else {"environment": scan_plan.env}

        for collection_name in collections:
            collection = self.collections[collection_name]
            self.log.info("clearing collection: " + collection.full_name)
            # delete docs from the collection,
            # either all or just for the specified environment
            collection.delete_many(env_cond)

    # return single match
    def get_by_id(self, environment, item_id):
        return self.find({
            "environment": environment,
            "id": item_id
        }, get_single=True)

    # return matches for ID in list of values
    def get_by_ids(self, environment, ids_list):
        return self.find({
            "environment": environment,
            "id": {"$in": ids_list}
        })

    def get_by_field(self, environment, item_type, field_name, field_value,
                     get_single=False):
        if field_value:
            return self.find({"environment": environment,
                              "type": item_type,
                              field_name: field_value},
                             get_single=get_single)
        else:
            return self.find({"environment": environment,
                              "type": item_type},
                             get_single=get_single)

    def get(self, environment, item_type, item_id, get_single=False):
        return self.get_by_field(environment, item_type, "id", item_id,
                                 get_single=get_single)

    def get_children(self, environment, item_type, parent_id):
        if parent_id:
            if not item_type:
                return self.find({"environment": environment,
                                  "parent_id": parent_id})
            else:
                return self.find({"environment": environment,
                                  "type": item_type,
                                  "parent_id": parent_id})
        else:
            return self.find({"environment": environment,
                              "type": item_type})

    def get_single(self, environment, item_type, item_id):
        matches = self.find({"environment": environment,
                             "type": item_type,
                             "id": item_id})
        if len(matches) > 1:
            raise ValueError("Found multiple matches for item: " +
                             "type=" + item_type + ", id=" + item_id)
        if len(matches) == 0:
            raise ValueError("No matches for item: " +
                             "type=" + item_type + ", id=" + item_id)
        return matches[0]

    # item must contain properties 'environment', 'type' and 'id'
    def set(self, item, collection=None):
        col = collection
        mongo_id = None
        projects = None
        if "_id" in item:
            mongo_id = item.pop("_id", None)

        if not collection or collection == self.collections['inventory']:
            # make sure we have environment, type & id
            self.check(item, "environment")
            self.check(item, "type")
            self.check(item, "id")

            item["last_scanned"] = datetime.now()
            item.pop("projects", [])

            obj_name = item["name_path"]
            obj_name = obj_name[obj_name.rindex('/') + 1:]

            if 'object_name' not in item:
                item['object_name'] = obj_name

            self.set_collections()  # make sure we have all collections set
            if not col:
                col = self.collections['inventory']

            find_tuple = {"environment": item["environment"],
                          "type": item["type"], "id": item["id"]}
        else:
            find_tuple = {'_id': bson.ObjectId(mongo_id)}
            doc = col.find_one(find_tuple)
            if not doc:
                raise ValueError('set(): could not find document with _id=' +
                                 mongo_id)

        col.update_one(find_tuple,
                       {'$set': self.encode_mongo_keys(item)},
                       upsert=True)
        if mongo_id:
            # restore original mongo ID of document, in case we need to use it
            item['_id'] = mongo_id
        if projects:
            col.update_one(find_tuple,
                           {'$addToSet': {"projects": {'$each': projects}}},
                           upsert=True)

    @staticmethod
    def check(obj, field_name):
        arg = obj[field_name]
        if not arg or not str(arg).rstrip():
            raise ValueError("Inventory item - " +
                             "the following field is not defined: " +
                             field_name)

    # note: to use general find, call find_items(),
    # which also does process_results
    @inv_initialization_required
    def find(self, search, projection=None, collection=None, get_single=False):
        coll = self.inventory_collection if not collection \
            else self.collections[collection]
        if get_single is True:
            return self.decode_object_id(
                self.decode_mongo_keys(
                    coll.find_one(search, projection=projection)
                )
            )
        else:
            return list(
                map(
                    self.decode_object_id,
                    map(
                        self.decode_mongo_keys,
                        coll.find(search, projection=projection))
                    )
            )

    def find_one(self, search, projection=None, collection=None) -> dict:
        return self.find(search, projection, collection, True)

    def find_items(self, search,
                   projection=None,
                   get_single=False,
                   collection=None):
        return self.find(search, projection, collection, get_single)

    # record a link between objects in the inventory, to be used in graphs
    # returns - the new link document
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
                    source_label="", target_label="",
                    extra_attributes=None):
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
            "attributes": extra_attributes if extra_attributes else {}
        }
        return self.write_link(link)

    def write_link(self, link):
        find_tuple = {
            'environment': link['environment'],
            'source_id': link['source_id'],
            'target_id': link['target_id']
        }
        if "_id" in link:
            link.pop("_id", None)
        link_encoded = self.encode_mongo_keys(link)
        links_col = self.collections["links"]
        result = links_col.update_one(find_tuple, {'$set': link_encoded},
                                      upsert=True)
        link['_id'] = result.upserted_id
        return link

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
    # - search: dict with search parameters
    # - values_replacement: dict,
    #     - keys: names of keys for which to replace the values
    #     - values: dict with "from" (value to be replaced) and "to" (new value)
    @inv_initialization_required
    def values_replace(self, search, values_replacement):
        for doc in self.inventory_collection.find(search):
            self.values_replace_in_object(doc, values_replacement)

    def delete(self, coll, query_filter):
        collection = self.collections[coll]
        if not collection:
            self.log.warn('delete(): collection not found - ' + coll)
            return
        result = collection.delete_many(query_filter)
        count = result.deleted_count
        self.log.info('delete(): ' + ('deleted ' + str(count) + ' documents'
                                      if count else 'no matching documents'))
        return count

    def get_env_config(self, env: str):
        return self.find_one(search={'name': env},
                             collection='environments_config')

    def is_feature_supported(self, env: str, feature: EnvironmentFeatures)\
            -> bool:
        env_config = self.get_env_config(env)
        if not env_config:
            return False

        # Workaround for mechanism_drivers field type
        mechanism_driver = env_config['mechanism_drivers'][0] \
            if isinstance(env_config['mechanism_drivers'], list) \
            else env_config['mechanism_drivers']

        full_env = {'environment.distribution': env_config['distribution'],
                    'environment.type_drivers': env_config['type_drivers'],
                    'environment.mechanism_drivers': mechanism_driver}

        result = self.collections['supported_environments'].find_one(full_env)
        if not result:
            return False
        features_in_env = result.get('features', {})
        return features_in_env.get(feature.value) is True
