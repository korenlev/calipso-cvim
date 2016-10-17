from discover.api_fetch_projects import ApiFetchProjects
from test.fetch.api_fetch.test_fetch import TestFetch
from test.test_data.fetch_data.regions import REGIONS
import json


class TestApiFetchProjects(TestFetch):

    def test_get(self):
        fetcher = ApiFetchProjects()
        fetcher.regions = REGIONS
        results = fetcher.get("fake_id")
        # print(json.dumps(results, sort_keys=True, indent=4))
        self.assertNotEqual(results, [], "can't get projects information")