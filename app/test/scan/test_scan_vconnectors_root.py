from copy import deepcopy
from unittest.mock import MagicMock

from discover.scan_vconnectors_root import ScanVconnectorsRoot

from test.scan.test_scan import TestScan
from test.scan.test_data.configurations import CONFIGURATIONS


class TestScanVconnectorsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_vonn_root_type_for_env_condition(self):

        self.scan_conn_root = ScanVconnectorsRoot()
        self.scan_conn_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_conn_root.types_to_fetch)

        # mock the method
        self.scan_conn_root.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)

        result = self.scan_conn_root.check_type_env(types_to_fetch[0])

        # expected environment_condition is OVS
        # actual environment_condition is OVS
        # hence result will be True
        self.assertEqual(result, True)
