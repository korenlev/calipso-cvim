import unittest

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr

from config.local_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class TestScan(unittest.TestCase):
    def setUp(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.inv = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.inventory = InventoryMgr()
        self.inventory.set_inventory_collection(self.inv)
