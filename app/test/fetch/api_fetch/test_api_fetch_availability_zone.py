from discover.api_fetch_availability_zones import ApiFetchAvailabilityZones
from test.fetch.api_fetch.test_fetch import TestFetch
from test.fetch.test_data.project import PROJECT


class TestApiFetchAvailabilityZones(TestFetch):

    def test_get(self):
        fetcher = ApiFetchAvailabilityZones()
        self.set_regions_for_fetcher(fetcher)

        zones = fetcher.get(PROJECT['name'])
        self.assertNotEqual(zones, [], "Can't get zones information with project name")