import unittest

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from test.fetch.config.local_config import ENV_CONFIG, MONGODB_CONFIG, COLLECTION_CONFIG
from test.fetch.api_fetch.test_data.regions import REGIONS
from test.fetch.api_fetch.test_data.configurations import CONFIGURATIONS


class TestFetch(unittest.TestCase):

    def configure_environment(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.inv = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.conf.config = CONFIGURATIONS['configuration']
        self.inventory = InventoryMgr()
        self.inventory.set_inventory_collection(self.inv)

    def set_regions_for_fetcher(self, fetcher):
        fetcher.regions = REGIONS