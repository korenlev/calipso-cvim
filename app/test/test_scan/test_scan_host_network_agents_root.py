from unittest.mock import MagicMock

from discover.scan_host_network_agents_root import ScanHostNetworkAgentsRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_host_network_agents_root import types_of_fetches, obj, id_field, child_id, child_type


class TestScanHostNetworkAgentsRoot(TestScan):
    def test_scan_host_network_agent_root(self):

        self.scan_host_nar = ScanHostNetworkAgentsRoot()
        self.scan_host_nar = MagicMock(return_value=types_of_fetches)

        self.scan = Scanner(self.scan_host_nar.return_value)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "No Matches for item id")

        # check environment
        type_of_environment = self.scan.check_type_env(types_of_fetches)

        self.assertEqual(type_of_environment, True)
