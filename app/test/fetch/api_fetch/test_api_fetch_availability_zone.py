import json

from discover.api_fetch_availability_zones import ApiFetchAvailabilityZones
from test.fetch.api_fetch.test_fetch import TestFetch
from test.test_data.fetch_data.projects import PROJECTS


class TestApiFetchAvailabilityZones(TestFetch):

    def test_get(self):
        fetcher = ApiFetchAvailabilityZones()
        self.setRegion(fetcher)
        project_name = PROJECTS[0]['name']
        results = fetcher.get(project_name)
        print(json.dumps(results, sort_keys=True, indent=4))
        self.assertNotEqual(results, [], "can't get projects information")