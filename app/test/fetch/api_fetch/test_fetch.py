import unittest

from test.config.local_config import ENV_CONFIG
from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from test.test_data.fetch_data.regions import REGIONS

class TestFetch(unittest.TestCase):

    def setUp(self):
        # use local database as test database
        self.mongo_config = ""
        self.env = ENV_CONFIG
        self.inv = "unittest"

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.inventory = InventoryMgr()
        self.inventory.set_inventory_collection("unittest")

    def setRegion(self, fetcher):
        fetcher.regions = REGIONS
