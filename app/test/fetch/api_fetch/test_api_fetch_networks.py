from discover.api_fetch_networks import ApiFetchNetworks
from test.fetch.api_fetch.test_fetch import TestFetch
from test.fetch.test_data.regions import REGIONS


class TestApiFetchNetworks(TestFetch):

    def test_get(self):
        fetcher = ApiFetchNetworks()
        self.set_regions_for_fetcher(fetcher)

        region_name = list(REGIONS.keys())[0]
        region = REGIONS[region_name]

        ret = fetcher.get(region['id'])
        self.assertNotEqual(ret, [], "Can't get networks information with region id")