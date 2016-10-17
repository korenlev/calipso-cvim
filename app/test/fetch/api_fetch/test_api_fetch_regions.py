from discover.api_fetch_regions import ApiFetchRegions
from test.fetch.api_fetch.test_fetch import TestFetch


class TestApiFetchRegions(TestFetch):

    def test_get(self):
        fetcher = ApiFetchRegions()
