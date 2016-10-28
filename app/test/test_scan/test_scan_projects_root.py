from discover.scan_projects_root import ScanProjectsRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_project import obj, id_field, child_id, child_type


class TestScanProjectRoot(TestScan):
    def test_scan_project_root(self):
        self.scan_proj_root = ScanProjectsRoot()

        self.scan = Scanner(self.scan_proj_root.types_to_fetch)
        results = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(results, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_proj_root.types_to_fetch)

        self.assertEqual(type_of_environment, True)
