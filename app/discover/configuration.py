from discover.mongo_access import MongoAccess
from discover.singleton import Singleton


class Configuration(MongoAccess, metaclass=Singleton):
    def __init__(self, mongo_config=""):
        super().__init__(mongo_config)
        self.db_client = MongoAccess(mongo_config)
        self.db = MongoAccess.db
        self.collection = self.db["environments_config"]

    def use_env(self, env_name):
        self.log.info("configuration taken from environment: " + env_name)
        self.env = env_name
        envs = self.collection.find({"name": env_name})
        count = 0
        for e in envs:
            count += 1
            self.env_config = e
            self.config = e["configuration"]
            if count > 1:
                raise ValueError("set_env: found multiple matching environments")
        if count == 0:
            raise ValueError("set_env: could not find matching environment")

    def get_env_config(self):
        return self.env_config

    def get_config(self):
        return self.config

    def get_env(self):
        return self.env

    def get(self, component):
        if not self.config:
            raise ValueError("Configuration: environment not set")
        matches = [c for c in self.config if c["name"] == component]
        if (len(matches) == 0):
            raise IndexError("No matches for configuration component: " + component)
        if len(matches) > 1:
            raise IndexError("Found multiple matches for configuration component: " + component)
        return matches[0]

    def has_network_plugin(self, name):
        if 'network_plugins' not in self.env_config:
            self.log.error('Environment missing network_plugins definition: ' +
                           self.env_config['name'])
        network_plugins = self.env_config['network_plugins']
        return name in network_plugins
