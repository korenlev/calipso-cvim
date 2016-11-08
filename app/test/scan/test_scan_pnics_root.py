from copy import deepcopy
from unittest.mock import MagicMock

from discover.scan_pnics_root import ScanPnicsRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanPnicsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_pnics_root_type_for_env_condition(self):

        self.scan_pr = ScanPnicsRoot()
        self.scan_pr.set_env(self.env)

        type_to_fetch = deepcopy(self.scan_pr.types_to_fetch)

        # mock the method
        self.scan_pr.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        # check for the environment_condition in the types_to_fetches
        result = self.scan_pr.check_type_env(type_to_fetch[0])

        # Note: This environment_condition is based on what types_to_fetches we are passing into check_type_env
        # expected environment_condition is OVS
        # actual environment_condition is OVS
        # hence result will be True
        self.assertEqual(result, True)
