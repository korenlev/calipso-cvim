from discover.scan_vconnectors_root import ScanVconnectorsRoot
from discover.scanner import Scanner

from test_scan.test_scan import TestScan
from test_data.scan_vconnectors_root import obj, id_field, child_id, child_type


class TestScanVconnectorsRoot(TestScan):

    def test_scan_vconnectors_root(self):

        self.scan_vcon_root = ScanVconnectorsRoot()

        self.scan = Scanner(self.scan_vcon_root.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_vcon_root.types_to_fetch)

        self.assertEqual(type_of_environment, True)
