from unittest.mock import MagicMock

from discover.scan_host import ScanHost
from discover.folder_fetcher import FolderFetcher
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_host import VSERVICES, HOST, types_of_fetches_vservices, \
    obj, id_field, child_id, child_type


class TestScanHost(TestScan):
    def test_scan_host_vservices(self):
        self.fetcher = FolderFetcher(VSERVICES, HOST)
        types_of_fetches_vservices[0]['fetcher'] = self.fetcher

        self.scan_host = ScanHost()
        self.scan_host = MagicMock(return_value=types_of_fetches_vservices)

        self.scan = Scanner(self.scan_host.return_value)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "Can't get verservices")

        # check environment
        type_of_environment = self.scan.check_type_env(types_of_fetches_vservices)

        self.assertEqual(type_of_environment, True)
