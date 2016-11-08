from copy import deepcopy
from unittest.mock import MagicMock, Mock

from discover.scanner import Scanner
from discover.scan_environment import ScanEnvironment
from test.scan.test_scan import TestScan
from test.scan.test_data.scanner import obj, id_field, child_id, child_type


class TestScanner(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scanner_scan(self):

        self.scan_agg = ScanEnvironment()
        self.types_to_fetch = deepcopy(self.scan_agg.types_to_fetch)
        self.scanner = Scanner(self.types_to_fetch)
        self.scanner.set_env(self.env)

        # original method
        original_scan_type = self.scanner.scan_type

        # Mock Method
        # self.scanner.scan_type = MagicMock(return_value=[])

        result = self.scanner.scan(obj, id_field, child_id, child_type)

        self.scanner.scan_type = original_scan_type

        self.assertEqual(obj, result)

    def est_scanner_check_type_env(self):

        self.scan_agg = ScanEnvironment()

        self.types_to_fetch = deepcopy(self.scan_agg.types_to_fetch)
        self.scanner = Scanner(self.types_to_fetch)

        result = self.scanner.check_type_env(self.types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)

    def est_scanner_scan_type(self):
        self.scan_agg = ScanEnvironment()
        self.types_to_fetch = deepcopy(self.scan_agg.types_to_fetch)
        self.scanner = Scanner(self.types_to_fetch)
        self.scanner.set_env(self.env)

        # Mock methods
        # self.scanner.check_type_env = MagicMock()
        # self.scanner.get_instance_of_class = MagicMock()

        obj = {'id': 'Mirantis-Liberty-Nvn'}
        id_field = 'id'
        result = self.scanner.scan_type(self.types_to_fetch[0], obj, id_field)

        self.assertEqual(result, [], "Can't able to get the child list")

    def est_scan_run(self):
        self.scan_agg = ScanEnvironment()
        self.types_to_fetch = deepcopy(self.scan_agg.types_to_fetch)
        self.scanner = Scanner(self.types_to_fetch)
        self.scanner.set_env(self.env)

        result = self.scan_agg.run_scan(obj, id_field, child_id, child_type)

        print(result)








