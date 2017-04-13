import unittest
from unittest.mock import MagicMock

from discover.configuration import Configuration
from discover.scanner import Scanner
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
        self.inv.set = MagicMock()
        self.conf.env_config = CONFIGURATIONS
        self.inv.set_collections(self.inventory_collection)
        self.inv.monitoring_setup_manager = \
            MonitoringSetupManager(MONGODB_CONFIG, self.env)
        MonitoringSetupManager.create_setup = MagicMock()

    def test_folder_object(self, scanner, expected_queue):
        scanner.set_env(self.env)
        Scanner.scan_from_queue = MagicMock()
        scanner.run_scan({'id': 'test-env'}, 'id', None, None)
        queue = scanner.scan_queue_track
        expected_len = len(expected_queue)
        self.assertEqual(len(queue), expected_len,
                         'expected {} results from ScanEnvironment'.
                         format(expected_len))
        self.assertListEqual(list(queue.keys()), expected_queue)
