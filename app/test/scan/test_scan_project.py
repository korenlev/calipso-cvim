from unittest.mock import MagicMock

from discover.api_fetch_availability_zones import ApiFetchAvailabilityZones
from discover.api_fetch_project_hosts import ApiFetchProjectHosts
from discover.scan_project import ScanProject
from test.scan.test_data.scan import UNIT_TESTS_ENV
from test.scan.test_scan import TestScan


class TestScanProject(TestScan):

    def test_scan_project(self):

        scanner = ScanProject()
        scanner.set_env(UNIT_TESTS_ENV)
        scanner.scan_from_queue = MagicMock()
        ApiFetchAvailabilityZones.get = MagicMock(return_value=self.AZ_RESULT)
        ApiFetchProjectHosts.get = MagicMock(return_value=
                                             self.PROJECT_HOSTS_RESULT)
        project = {
            'id': '9bb12590b58d4c729871dc0c41c5a0f3',
            'type': 'project',
            'parent_type': 'projects_folder',
            'parent_id': UNIT_TESTS_ENV + '-projects'
        }
