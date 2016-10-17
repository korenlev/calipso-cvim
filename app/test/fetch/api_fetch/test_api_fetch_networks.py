import json

from discover.api_fetch_networks import ApiFetchNetworks
from test.fetch.api_fetch.test_fetch import TestFetch
from test.test_data.fetch_data.regions import REGIONS


class TestApiFetchNetworks(TestFetch):

    def test_get(self):
        fetcher = ApiFetchNetworks()
        regions = REGIONS['RegionOne']
        ApiFetchNetworks.regions = REGIONS
        escaped_id = fetcher.escape(regions['id'])
        ret = fetcher.get(escaped_id)
        # print(json.dumps(ret, sort_keys=True, indent=4))
        self.assertNotEqual(ret, [], "Can't get networks information from region")