from unittest.mock import MagicMock

from discover.api_fetch_projects import ApiFetchProjects
from discover.scan_projects_root import ScanProjectsRoot

from test.scan.test_data.scan import UNIT_TESTS_ENV
from test.scan.test_scan import TestScan


class TestScanProjectsRoot(TestScan):

    API_PROJECTS_RESULT = [
        {
            "description": "Webex-Dev",
            "environment": "WebEX-Mirantis@Cisco",
            "id": "9bb12590b58d4c729871dc0c41c5a0f3",
            "name": "Webex-Dev",
            "object_name": "Webex-Dev",
            "parent_id": "WebEX-Mirantis@Cisco-projects",
            "parent_type": "projects_folder",
            "type": "project"
        },
        {
            "description": "admin tenant",
            "environment": "WebEX-Mirantis@Cisco",
            "id": "329e0576da594c62a911d0dccb1238a7",
            "name": "admin",
            "object_name": "admin",
            "parent_id": "WebEX-Mirantis@Cisco-projects",
            "parent_type": "projects_folder",
            "type": "project"
        },
        {
            "description": "demo",
            "environment": "WebEX-Mirantis@Cisco",
            "id": "67796509be634932acef545fd1426a22",
            "name": "demo",
            "object_name": "demo",
            "parent_id": "WebEX-Mirantis@Cisco-projects",
            "parent_type": "projects_folder",
            "type": "project"
        },
        {
            "description": "Koren test project",
            "environment": "WebEX-Mirantis@Cisco",
            "id": "052eb1d73ba44677b118da7ee0089be1",
            "name": "koren-proj",
            "object_name": "koren-proj",
            "parent_id": "WebEX-Mirantis@Cisco-projects",
            "parent_type": "projects_folder",
            "type": "project"
        }
    ]

    def test_scan_projects_root(self):

        scanner = ScanProjectsRoot()
        scanner.set_env(self.env)
        scanner.scan_from_queue = MagicMock()
        ApiFetchProjects.get = MagicMock(return_value=self.API_PROJECTS_RESULT)

        projects_folder = {
            'id': UNIT_TESTS_ENV + '-projects',
            'type': 'projects_folder',
            'parent_type': 'environment',
            'parent_id': UNIT_TESTS_ENV
        }
        scanner.scan(projects_folder)
        queue = scanner.scan_queue_track
        expected_saves = len(self.API_PROJECTS_RESULT)
        self.assertEqual(len(queue.keys()), expected_saves,
                         'expected 1 result from ScanRegionsRoot')
        self.assertListEqual(list(queue.keys()), [
            'project;9bb12590b58d4c729871dc0c41c5a0f3',
            'project;329e0576da594c62a911d0dccb1238a7',
            'project;67796509be634932acef545fd1426a22',
            'project;052eb1d73ba44677b118da7ee0089be1',
        ])
        self.assertEqual(expected_saves, self.inv.set.call_count,
                         'expected {} objects to be saved'.
                         format(str(expected_saves)))
