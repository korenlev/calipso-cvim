from copy import deepcopy

from discover.scan_oteps import ScanOteps

from test.scan.test_scan import TestScan


class TestScanOteps(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_oteps_type_for_env_condition(self):

        self.scan_oteps = ScanOteps()
        self.scan_oteps.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_oteps.types_to_fetch)

        result = self.scan_oteps.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)