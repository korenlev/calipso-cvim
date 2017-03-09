from copy import deepcopy

from discover.scan_instances_root import ScanInstancesRoot

from test.scan.test_scan import TestScan


class TestScanInstanceRoot(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_inst_root_type_for_environment_condition(self):

        self.scan_inst_root = ScanInstancesRoot()
        self.scan_inst_root.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_inst_root.types_to_fetch)

        result = self.scan_inst_root.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)




