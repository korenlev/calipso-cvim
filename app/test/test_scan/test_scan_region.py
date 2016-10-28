from discover.scan_region import ScanRegion
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_region import obj, id_field, child_id, child_type


class TestScanRegion(TestScan):
    def test_scan_region(self):
        self.scan_reg = ScanRegion()

        self.scan = Scanner(self.scan_reg.types_to_fetch)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "Can't get the region info")

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_reg.types_to_fetch)

        self.assertEqual(type_of_environment, True)
