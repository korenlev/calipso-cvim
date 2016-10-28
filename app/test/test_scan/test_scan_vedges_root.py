from discover.scan_vedges_root import ScanVedgesRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_vedges_root import obj, id_field, child_id, child_type


class TestScanVedgesRoot(TestScan):

    def test_scan_vedges_root(self):

        self.scan_vedges = ScanVedgesRoot()

        self.scan = Scanner(self.scan_vedges.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_vedges.types_to_fetch)

        self.assertEqual(type_of_environment, True)
