from copy import deepcopy

from discover.scan_network import ScanNetwork

from test.scan.test_scan import TestScan


class TestScanNetwork(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_network_type_for_environment_condition(self):

        self.scan_net = ScanNetwork()
        self.scan_net.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_net.types_to_fetch)

        result = self.scan_net.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)

