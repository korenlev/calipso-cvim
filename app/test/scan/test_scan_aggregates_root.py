from copy import deepcopy

from discover.scan_aggregates_root import ScanAggregatesRoot

from test.scan.test_scan import TestScan


class TestScanAggregatesRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_agg_root_for_environment_condition(self):

        self.scan_agg_root = ScanAggregatesRoot()
        self.scan_agg_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_agg_root.types_to_fetch)

        result = self.scan_agg_root.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)