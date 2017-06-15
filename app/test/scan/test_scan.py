import unittest
from unittest.mock import MagicMock

from discover.configuration import Configuration
from test.scan.config.local_config \
    import ENV_CONFIG, COLLECTION_CONFIG
from test.scan.test_data.configurations import CONFIGURATIONS
from utils.inventory_mgr import InventoryMgr


class TestScan(unittest.TestCase):

    def configure_environment(self):
        self.env = ENV_CONFIG
        self.inventory_collection = COLLECTION_CONFIG

        self.conf = Configuration()
        self.conf.use_env = MagicMock()
        self.conf.environment = CONFIGURATIONS
        self.conf.configuration = CONFIGURATIONS["configuration"]

        self.inv = InventoryMgr()
        self.inv.set_collections(self.inventory_collection)

    def setUp(self):
        self.configure_environment()
