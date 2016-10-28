from unittest.mock import MagicMock

from test_scan.test_scan import TestScan
from discover.scan_environment import ScanEnvironment
from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner

from test_data.scan_environment import REGIONS, ENVIRONMENT, types_of_fetches, obj, id_field, child_id, child_type


class TestScanEnvironment(TestScan):
    def test_scan_environment(self):

        self.fetcher = FolderFetcher(REGIONS, ENVIRONMENT)
        types_of_fetches[0]['fetcher'] = self.fetcher
        types_of_fetches[1]['fetcher'] = self.fetcher

        self.scan_env = ScanEnvironment()
        self.scan_env = MagicMock(return_value=types_of_fetches)

        self.scan = Scanner(self.scan_env.return_value)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "Can't Create the dynamic folders")

        # check environment
        type_of_environment = self.scan.check_type_env(types_of_fetches)

        self.assertEqual(type_of_environment, True)
