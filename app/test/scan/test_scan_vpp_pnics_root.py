from copy import deepcopy
from unittest.mock import MagicMock

from discover.scan_vpp_pnics_root import ScanVppPnicsRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanVppPnicsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_vvppr_type_for_env_condition(self):

        self.scan_vvppr = ScanVppPnicsRoot()
        self.scan_vvppr.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_vvppr.types_to_fetch)

        # mock the method
        self.scan_vvppr.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        result = self.scan_vvppr.check_type_env(types_to_fetch[0])

        # expected environment_condition is OVS
        # actual environment_condition is VVP
        # hence result will be False
        self.assertEqual(result, False)