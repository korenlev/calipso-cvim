from unittest.mock import MagicMock

from discover.scan_environment import ScanEnvironment
from discover.scanner import Scanner
from test.scan.test_scan import TestScan


class TestScanEnvironment(TestScan):

    ENV = 'test-env'
    EXPECTED_RESULTS = [
        {
            "type": "regions_folder",
            "children_scanner": "ScanRegionsRoot"
        },
        {
            "type": "projects_folder",
            "children_scanner": "ScanProjectsRoot"
        }
    ]

    def setUp(self):
        self.configure_environment()

    def test_scan_environment(self):
        scanner = ScanEnvironment()
        scanner.set_env(self.env)
        Scanner.scan_from_queue = MagicMock()
        scanner.run_scan({'id': 'test-env'}, 'id', None, None)
        queue = scanner.scan_queue_track
        self.assertEqual(len(queue), 2,
                         'expected 2 results from ScanEnvironment')
        self.assertListEqual(list(queue.keys()), [
            'regions_folder;{}-regions'.format(self.ENV),
            'projects_folder;{}-projects'.format(self.ENV)
        ])

