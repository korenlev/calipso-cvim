from discover.scan_instance import ScanInstance
from discover.scanner import Scanner

from test_scan import TestScan
from test_data.scan_instance import obj, id_field, child_id, child_type


class TestScanInstance(TestScan):
    def test_scan_instance(self):
        self.scan_inst = ScanInstance()

        self.scan = Scanner(self.scan_inst.types_to_fetch)
        result = self.scan.scan(obj, id_field, child_id, child_type)

        self.assertNotEqual(result, [], "Can't get the instance info")

        # check environment
        type_of_environment = self.scan.check_type_env(self.scan_inst.types_to_fetch)

        self.assertEqual(type_of_environment, True)
