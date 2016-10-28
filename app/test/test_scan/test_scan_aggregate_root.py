from unittest.mock import MagicMock

from discover.scan_aggregates_root import ScanAggregatesRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_aggregates_root import types_of_fetches, obj, id_field, child_id, child_type


class TestScanAggregateRoot(TestScan):
    def test_scan_aggregares_root(self):
        self.scan_agg_root = ScanAggregatesRoot()
        self.scan_agg_root = MagicMock(return_value=types_of_fetches)

        self.scan = Scanner(self.scan_agg_root.return_value)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "Can't get the available zone info")

        # check environment
        type_of_environment = self.scan.check_type_env(types_of_fetches)

        self.assertEqual(type_of_environment, True)
