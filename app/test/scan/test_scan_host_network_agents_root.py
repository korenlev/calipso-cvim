from copy import deepcopy

from discover.scan_host_network_agents_root import ScanHostNetworkAgentsRoot

from test.scan.test_scan import TestScan


class TestScanHostNetworkAgentsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_host_nar_for_environment_condition(self):

        self.scan_hnar = ScanHostNetworkAgentsRoot()
        self.scan_hnar.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_hnar.types_to_fetch)

        result = self.scan_hnar.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)

