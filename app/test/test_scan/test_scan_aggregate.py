from unittest.mock import MagicMock

from discover.scan_aggregate import ScanAggregate
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_aggregate import types_of_fetches, obj, id_field, child_id, child_type


class TestScanAggregate(TestScan):
    def test_scan_aggregate(self):

        self.scan_agg = ScanAggregate()
        self.scan_agg = MagicMock(return_value=types_of_fetches)

        self.scan = Scanner(self.scan_agg.return_value)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(result, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(types_of_fetches)

        self.assertEqual(type_of_environment, True)


