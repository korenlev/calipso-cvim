from copy import deepcopy

from discover.scan_instance import ScanInstance

from test.scan.test_scan import TestScan


class TestScanInstance(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_inst_for_environment_condition(self):

        self.scan_inst = ScanInstance()
        self.scan_inst.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_inst.types_to_fetch)

        result = self.scan_inst.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(result, True)


