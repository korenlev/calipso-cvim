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
