from copy import deepcopy

from discover.scan_regions_root import ScanRegionsRoot

from test.scan.test_scan import TestScan


class TestScanRegionsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_reg_root_type_for_env_condition(self):

        self.scan_reg_root = ScanRegionsRoot()
        self.scan_reg_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_reg_root.types_to_fetch)

        result = self.scan_reg_root.check_type_env(types_to_fetch[0])

        self.assertEqual(result, True)
