from copy import deepcopy

from discover.scan_host import ScanHost

from test.scan.test_scan import TestScan


class TestScanHost(TestScan):
    def setUp(self):
        self.configure_environment()

    def test_scan_host_for_environment_condition(self):
        self.scan_host = ScanHost()
        self.scan_host.set_env(self.env)

        types_to_fetch = deepcopy(self.scan_host.types_to_fetch)

        # check type for vservices_folder
        type_for_vservics_folder = self.scan_host.check_type_env(types_to_fetch[0])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(type_for_vservics_folder, True)

        # check type for vservice
        type_for_vservice = self.scan_host.check_type_env(types_to_fetch[1])

        # types to fetch don't have environment_condition hence it will return True
        self.assertEqual(type_for_vservice, True)











