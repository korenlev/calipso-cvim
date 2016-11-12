import unittest

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from test.scan.test_data.configurations import CONFIGURATIONS
from test.scan.config.local_config import ENV_CONFIG, COLLECTION_CONFIG


class TestScan(unittest.TestCase):

    def configure_environment(self):
        self.mongo_config = ""
        self.env = ENV_CONFIG
        self.inventory_collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.inv = InventoryMgr()
        self.conf.env_config = CONFIGURATIONS
        self.inv.set_inventory_collection(self.inventory_collection)
