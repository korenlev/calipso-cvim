from copy import deepcopy

from discover.scan_environment import ScanEnvironment

from test.scan.test_scan import TestScan


class TestScanEnvironment(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_env_for_environment_condition(self):

        self.scan_env = ScanEnvironment()
        self.scan_env.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_env.types_to_fetch)

        # Check env type for regions_folder
        type_for_region_folder = self.scan_env.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(type_for_region_folder, True)

        # Check env type for projects_folder
        type_for_project_folder = self.scan_env.check_type_env(types_to_fetch[1])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(type_for_project_folder, True)

