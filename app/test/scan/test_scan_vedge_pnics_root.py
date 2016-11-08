from copy import deepcopy
from unittest.mock import MagicMock
from discover.scan_vedge_pnics_root import ScanVedgePnicsRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanVedgePnicsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_vpr_type_for_env_condition(self):

        self.scan_vpr = ScanVedgePnicsRoot()
        self.scan_vpr.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_vpr.types_to_fetch)

        # mock the method
        self.scan_vpr.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        result = self.scan_vpr.check_type_env(types_to_fetch[0])

        # expected environment_condition is OVS
        # actual environment_condition is VVP
        # hence result will be False
        self.assertEqual(result, False)