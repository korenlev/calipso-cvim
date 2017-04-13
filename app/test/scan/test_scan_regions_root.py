from unittest.mock import MagicMock

from discover.scan_regions_root import ScanRegionsRoot
from discover.api_fetch_regions import ApiFetchRegions
from discover.scanner import Scanner
from test.scan.test_data.scan import UNIT_TESTS_ENV
from test.scan.test_scan import TestScan


class TestScanRegionsRoot(TestScan):

    API_REGIONS_RESULT = [
        {
            'id': 'RegionOne',
            'endpoints': {
                'keystone': {
                    'internalURL': 'http://192.168.0.2:5000/v2.0',
                    'adminURL': 'http://192.168.0.2:35357/v2.0',
                    'service_type': 'identity',
                    'publicURL': 'http://172.16.0.3:5000/v2.0',
                    'id': '18d3a7fc5a7f4240aa0505956d8b5591'},
                'neutron': {
                    'internalURL': 'http://192.168.0.2:9696',
                    'adminURL': 'http://192.168.0.2:9696',
                    'service_type': 'network',
                    'publicURL': 'http://172.16.0.3:9696',
                    'id': '68f4a43b3ac149148cd485fbcac4565f'},
                'nova': {
                    'internalURL': 'http://192.168.0.2:8774/v2/' +
                                   'c769218f0d3c429a8585696cba3d9f5a',
                    'adminURL': 'http://192.168.0.2:8774/v2/' +
                                'c769218f0d3c429a8585696cba3d9f5a',
                    'service_type': 'compute',
                    'publicURL': 'http://172.16.0.3:8774/v2/' +
                                 'c769218f0d3c429a8585696cba3d9f5a',
                    'id': '0ce6d475ca8742fab6a846f620ae901f'}
            },
            'name': 'RegionOne',
            'parent_id': UNIT_TESTS_ENV + '-regions',
            'parent_type': 'regions_folder'
        }
    ]

    def test_scan_regions_root(self):

        scanner = ScanRegionsRoot()
        scanner.set_env(UNIT_TESTS_ENV)
        Scanner.scan_from_queue = MagicMock()
        ApiFetchRegions.get = MagicMock(return_value=self.API_REGIONS_RESULT)
        regions_folder = {
            'id': UNIT_TESTS_ENV + '-regions',
            'type': 'regions_folder',
            'parent_type': 'environment',
            'parent_id': UNIT_TESTS_ENV
        }
        scanner.scan(regions_folder)
        queue = scanner.scan_queue_track
        self.assertEqual(len(queue), 1,
                         'expected 1 result from ScanRegionsRoot')
        self.assertListEqual(list(queue.keys()), ['region;RegionOne'])
        self.inv.set.assert_called_once()
