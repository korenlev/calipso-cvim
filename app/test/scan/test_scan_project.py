from copy import deepcopy

from discover.scan_project import ScanProject

from test.scan.test_scan import TestScan


class TestScanProject(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_project_type_for_env_condition(self):

        self.scan_proj = ScanProject()
        self.scan_proj.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_proj.types_to_fetch)

        result = self.scan_proj.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)

