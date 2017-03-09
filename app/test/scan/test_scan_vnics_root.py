from copy import deepcopy
from unittest.mock import MagicMock

from discover.scan_vnics_root import ScanVnicsRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanVnicsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_vnivcs_root_type_for_env_condition(self):

        self.scan_vr = ScanVnicsRoot()
        self.scan_vr.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_vr.types_to_fetch)

        # mock the method
        self.scan_vr.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        result = self.scan_vr.check_type_env(types_to_fetch[0])

        # expected environment_condition is OVS
        # actual environment_condition is OVS
        # hence result will be True
        self.assertEqual(result, True)
