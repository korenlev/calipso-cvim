from discover.scan_environment import ScanEnvironment
from test.scan.test_scan import TestScan


class TestScanEnvironment(TestScan):

    ENV = 'test-env'

    def setUp(self):
        self.configure_environment()

    def test_scan_environment(self):
        self.test_folder_object(ScanEnvironment(), [
            'regions_folder;{}-regions'.format(self.ENV),
            'projects_folder;{}-projects'.format(self.ENV)
        ])
