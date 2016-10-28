from discover.scan_project import ScanProject
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_project import obj, id_field, child_id, child_type


class TestScanProject(TestScan):
    def test_scan_project(self):
        self.scan_proj = ScanProject()

        self.scan = Scanner(self.scan_proj.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_proj.types_to_fetch)

        self.assertEqual(type_of_environment, True)
