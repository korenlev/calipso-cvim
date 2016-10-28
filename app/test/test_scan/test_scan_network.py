from discover.scan_network import ScanNetwork
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_instance import obj, id_field, child_id, child_type


class TestScanNetwork(TestScan):
    def test_scan_network(self):

        self.scan_network = ScanNetwork()

        self.scan = Scanner(self.scan_network.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(results, [], "Can't get the networks info")

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_network.types_to_fetch)

        self.assertEqual(type_of_environment, True)
