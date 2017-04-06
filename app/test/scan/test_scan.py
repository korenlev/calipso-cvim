import unittest
from unittest.mock import MagicMock

from discover.configuration import Configuration
from monitoring.setup.monitoring_setup_manager import MonitoringSetupManager
from test.scan.config.local_config \
    import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG
from test.scan.test_data.configurations import CONFIGURATIONS
from utils.inventory_mgr import InventoryMgr


class TestScan(unittest.TestCase):

    def configure_environment(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.inventory_collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.inv = InventoryMgr()
        self.conf.env_config = CONFIGURATIONS
        self.inv.set_collections(self.inventory_collection)
        self.inv.monitoring_setup_manager = \
            MonitoringSetupManager(MONGODB_CONFIG, self.env)
        MonitoringSetupManager.create_setup = MagicMock()
