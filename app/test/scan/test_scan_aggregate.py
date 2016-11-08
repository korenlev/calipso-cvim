from copy import deepcopy

from discover.scan_aggregate import ScanAggregate

from test.scan.test_scan import TestScan


class TestScanAggregate(TestScan):
    def setUp(self):
        self.configure_environment()
        self.scan_aggregate_type = ScanAggregate()
        self.scan_aggregate_type.set_env(self.env)
        self.types_to_fetch = deepcopy(self.scan_aggregate_type.types_to_fetch)

    def test_scan_aggregate_for_environment_condition(self):

        result = self.scan_aggregate_type.check_type_env(self.types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)
