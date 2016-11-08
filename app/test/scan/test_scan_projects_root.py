from copy import deepcopy

from discover.scan_projects_root import ScanProjectsRoot

from test.scan.test_scan import TestScan


class TestScanProjectsRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_proj_root_type_for_env_condition(self):

        self.scan_proj_root = ScanProjectsRoot()
        self.scan_proj_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_proj_root.types_to_fetch)

        result = self.scan_proj_root.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)