import os

from pymongo import MongoClient
from api.etc.logger import Logger
from api.etc.singleton import Singleton
from api.etc.utils import Utils


class MongoAccess(Logger, Utils, metaclass=Singleton):

    # this default mongo config file is just for development
    # it should point to the mongo config file of the overall system
    default_config_file = "/home/xiacong/OSDNA/app/config/osdna_mongo_access.conf"

    def __init__(self):
        super().__init__()
        self.mongo_params = self.get_mongo_params()
        self.db = self.mongo_connect()
        self.collections = self.get_collections()

    def get_mongo_params(self):
        mongo_params = {
            "server": "localhost",
            "port": "27017",
            "auth_db": "osdna"
        }

        if not os.path.isfile(self.default_config_file):
            raise ValueError("mongo config file doesn't exist")

        try:
            mongo_config_params = self.read_config_from_config_file(self.default_config_file)
        except Exception as e:
            self.log.error("Failed to read mongo config file " + self.default_config_file)
            raise e

        mongo_params.update(mongo_config_params)
        return mongo_params

    def mongo_connect(self):
        if not self.mongo_params:
            self.mongo_params = self.get_mongo_params()

        mongodb_url = "mongodb://"
        user = self.mongo_params.get("user")
        password = self.mongo_params.get("password")
        server = self.mongo_params.get("server")
        port = self.mongo_params.get("port")
        auth_db = self.mongo_params.get("auth_db")

        if user and password:
            mongodb_url = mongodb_url + user + ":" + password + "@"

        mongodb_url = mongodb_url + server + ":" + port

        mongo_client = MongoClient(mongodb_url)
        return mongo_client[auth_db]

    def get_collections(self):
        if not self.db:
            self.mongo_connect()

        collections = {}
        collections_map = {
            "inventory": "api",
            "links": "api_links",
            "cliques": "api_cliques",
            "clique_constraints": "api_clique_constraints",
            "clique_types": "api_clique_types",
            "link_types": "api_link_types",
            "messages": "api_messages",
            "environments_config": "api_environments_config",
            "constants": "api_constants",
            "scans": "api_scans",
            "monitoring_config_templates": "api_monitoring_config_templates"
        }

        for collection, collection_name in collections_map.items():
            collections[collection] = self.db[collection_name]

        return collections

    def get_collection(self, collection_name):
        if not self.collections:
            self.collections = self.get_collections()
        return self.collections[collection_name]

    def get_constants_by_name(self, name):
        constants = self.get_collection('constants').find_one({"name": name})
        return [d['value'] for d in constants['data']]

    def read(self, collection, matches={}, projection={}, skip=0, limit=1000):
        collection = self.get_collection(collection)
        skip *= limit
        if not projection:
            query = collection.find(matches).skip(skip).limit(limit)
        else:
            query = collection.find(matches, projection).skip(skip).limit(limit)
        data = [obj for obj in query]
        return data

    def write(self, document, collection="inventory"):
        self.get_collection(collection).insert_one(document)

    def aggregate(self, pipeline, collection):
        collection = self.get_collection(collection)
        data = collection.aggregate(pipeline)
        return [d for d in data]