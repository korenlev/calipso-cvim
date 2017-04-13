from unittest.mock import MagicMock

from discover.api_fetch_availability_zones import ApiFetchAvailabilityZones
from discover.api_fetch_project_hosts import ApiFetchProjectHosts
from discover.scan_project import ScanProject
from test.scan.test_data.scan import UNIT_TESTS_ENV
from test.scan.test_scan import TestScan


class TestScanProject(TestScan):

    API_AZS_RESULT = [
        {
            "available": True,
            "id": "internal",
            "name": "internal",
            "object_name": "internal",
            "parent_id": "RegionOne-availability_zones",
            "parent_text": "Availability Zones",
            "parent_type": "availability_zones_folder",
            "type": "availability_zone"
        },
        {
            "available": True,
            "id": "nova",
            "name": "nova",
            "object_name": "nova",
            "parent_id": "RegionOne-availability_zones",
            "parent_text": "Availability Zones",
            "parent_type": "availability_zones_folder",
            "type": "availability_zone"
        },
        {
            "available": True,
            "id": "WebEx-RTP-Zone",
            "name": "WebEx-RTP-Zone",
            "object_name": "WebEx-RTP-Zone",
            "parent_id": "RegionOne-availability_zones",
            "parent_text": "Availability Zones",
            "parent_type": "availability_zones_folder",
            "type": "availability_zone"
        }
    ]
    API_PROJECT_HOSTS_RESULT = [
        {
            'id': 'node-1.cisco.com', 'zone': 'internal', 'type': 'host',
            'host': 'node-1.cisco.com', 'parent_type': 'availability_zone',
            'name': 'node-1.cisco.com', 'parent_id': 'internal',
            'host_type': ['Controller', 'Network']
        },
        {
            'id': 'node-2.cisco.com', 'zone': 'nova', 'type': 'host',
            'ip_address': '192.168.0.5', 'host': 'node-2.cisco.com',
            'parent_type': 'availability_zone', 'name': 'node-2.cisco.com',
            'parent_id': 'nova', 'host_type': []
        },
        {
            'id': 'node-3.cisco.com', 'zone': 'nova', 'type': 'host',
            'ip_address': '192.168.0.4', 'host': 'node-3.cisco.com',
            'parent_type': 'availability_zone', 'name': 'node-3.cisco.com',
            'parent_id': 'nova', 'host_type': ['Compute']
        }
    ]

    def test_scan_project(self):

        scanner = ScanProject()
        scanner.set_env(UNIT_TESTS_ENV)
        scanner.scan_from_queue = MagicMock()
        ApiFetchAvailabilityZones.get = \
            MagicMock(return_value=self.API_AZS_RESULT)
        ApiFetchProjectHosts.get = \
            MagicMock(return_value=self.API_PROJECT_HOSTS_RESULT)
        project = {
            'id': '9bb12590b58d4c729871dc0c41c5a0f3',
            'type': 'project',
            'parent_type': 'projects_folder',
            'parent_id': UNIT_TESTS_ENV + '-projects'
        }
        scanner.scan(project)
        queue = scanner.scan_queue_track
        expected_saves = len(self.API_AZS_RESULT) +\
            len(self.API_PROJECT_HOSTS_RESULT)
        expected_queue_len = len(self.API_PROJECT_HOSTS_RESULT)
        # scan queue will not include availability zones
        self.assertEqual(len(queue.keys()), expected_queue_len,
                         'expected {} results from ScanProject'.
                         format(expected_queue_len))
        self.assertListEqual(list(queue.keys()), [
            'host;node-1.cisco.com',
            'host;node-2.cisco.com',
            'host;node-3.cisco.com'
        ])
        self.assertEqual(expected_saves, self.inv.set.call_count,
                         'expected {} objects to be saved'.
                         format(str(expected_saves)))
