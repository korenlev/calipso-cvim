from copy import deepcopy
from unittest.mock import MagicMock

from discover.scan_vedges_root import ScanVedgesRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanVedgesRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_vedg_root_type_for_env_condition(self):

        self.scan_ver = ScanVedgesRoot()
        self.scan_ver.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_ver.types_to_fetch)

        # mock the method
        self.scan_ver.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        result = self.scan_ver.check_type_env(types_to_fetch[0])

        # expected environment_condition is OVS
        # actual environment_condition is OVS
        # hence result will be True
        self.assertEqual(result, True)
