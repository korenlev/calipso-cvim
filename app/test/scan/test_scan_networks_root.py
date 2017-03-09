from copy import deepcopy

from discover.scan_instances_root import ScanInstancesRoot

from test.scan.test_scan import TestScan


class TestScanInstancesRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_instances_root_type_for_env_condition(self):

        self.scan_insts_root = ScanInstancesRoot()
        self.scan_insts_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_insts_root.types_to_fetch)

        result = self.scan_insts_root.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)
