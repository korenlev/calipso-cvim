from discover.api_fetch_regions import ApiFetchRegions
from test.fetch.api_fetch.test_fetch import TestFetch
import json


class TestApiFetchRegions(TestFetch):

    def test_get(self):
        fetcher = ApiFetchRegions()
        fetcher.set_env(self.env)
        ret = fetcher.get("fake_id")
        # print(json.dumps(ret, sort_keys=True, indent=4))
        self.assertNotEqual(ret, [], "Can't get regions information")