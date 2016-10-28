from discover.scan_regions_root import ScanRegionsRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_region import obj, id_field, child_id, child_type


class TestScanRegionsRoot(TestScan):
    def test_scan_regions_root(self):
        self.scan_reg_root = ScanRegionsRoot()

        self.scan = Scanner(self.scan_reg_root.types_to_fetch)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(result, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_reg_root.types_to_fetch)

        self.assertEqual(type_of_environment, True)
