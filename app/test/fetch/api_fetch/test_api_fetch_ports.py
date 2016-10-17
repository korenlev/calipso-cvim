import json

from test.fetch.api_fetch.test_fetch import TestFetch
from discover.api_fetch_ports import ApiFetchPorts
from test.test_data.fetch_data.regions import REGIONS


class TestApiFetchPorts(TestFetch):

    def test_get(self):
        fetcher = ApiFetchPorts()
        regions = REGIONS['RegionOne']
        fetcher.regions = REGIONS
        escaped_id = fetcher.escape(regions['id'])
        ret = fetcher.get(escaped_id)
        print(json.dumps(ret, sort_keys=True, indent=4))
        self.assertNotEqual(ret, [], "Can't get ports information from region")