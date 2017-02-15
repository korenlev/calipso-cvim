from utils.mongo_access import MongoAccess
from utils.singleton import Singleton


class MongoMgr(MongoAccess, metaclass=Singleton):

    def __init__(self, config_file=""):
        super().__init__(config_file)
        self.collections = self.get_collections()

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
