import unittest

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from test.scan.config.local_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class TestScan(unittest.TestCase):

    def configure_environment(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.inventory_collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection(self.inventory_collection)
