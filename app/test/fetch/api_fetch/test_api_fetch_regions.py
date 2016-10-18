from discover.api_fetch_regions import ApiFetchRegions
from test.fetch.api_fetch.test_fetch import TestFetch


class TestApiFetchRegions(TestFetch):

    def test_get(self):
        fetcher = ApiFetchRegions()
        fetcher.set_env(self.env)

        ret = fetcher.get("test_id")
        self.assertNotEqual(ret, [], "Can't get regions information")