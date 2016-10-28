from discover.scan_oteps import ScanOteps
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_oteps import obj, id_field, child_id, child_type


class TestScanOteps(TestScan):
    def test_scan_oteps(self):

        self.scan_oteps = ScanOteps()

        self.scan = Scanner(self.scan_oteps.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_oteps.types_to_fetch)

        self.assertEqual(type_of_environment, True)
