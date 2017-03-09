from copy import deepcopy

from discover.scan_region import ScanRegion

from test.scan.test_scan import TestScan


class TestScanRegion(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_region_type_for_env_condition(self):

        self.scan_reg_type = ScanRegion()
        self.scan_reg_type.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_reg_type.types_to_fetch)

        result = self.scan_reg_type.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)

