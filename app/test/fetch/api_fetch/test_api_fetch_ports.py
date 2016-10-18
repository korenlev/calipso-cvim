from discover.api_fetch_ports import ApiFetchPorts
from test.fetch.api_fetch.test_fetch import TestFetch
from test.fetch.test_data.regions import REGIONS


class TestApiFetchPorts(TestFetch):

    def test_get(self):
        fetcher = ApiFetchPorts()
        self.set_regions_for_fetcher(fetcher)

        region_name = list(REGIONS.keys())[0]
        region = REGIONS[region_name]

        ret = fetcher.get(region['id'])
        self.assertNotEqual(ret, [], "Can't get ports information with region id")