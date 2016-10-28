from discover.scan_instances_root import ScanInstancesRoot
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_instance import obj, id_field, child_id, child_type


class TestScanInstancesRoot(TestScan):
    def test_scan_instance_root(self):

        self.scan_inst_root = ScanInstancesRoot()

        self.scan = Scanner(self.scan_inst_root.types_to_fetch)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertEqual(result, obj)

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_inst_root.types_to_fetch)

        self.assertEqual(type_of_environment, True)
