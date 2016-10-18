from app.discover.api_access import ApiAccess

from app.test.fetch.api_fetch.test_fetch import TestFetch
from app.test.fetch.test_data.regions import REGIONS


class TestApiAccess(TestFetch):

    def test_v2_auth_pwd(self):
        api_access = ApiAccess()

        token = api_access.v2_auth_pwd("admin")

        self.assertNotEqual(token, [], "Can't get token")

    def test_get_region_url(self):
        api_access = ApiAccess()

        self.set_regions_for_fetcher(api_access)

        region_name = list(REGIONS.keys())[0]
        region = REGIONS[region_name]

        service_name = list(region['endpoints'].keys())[0]
        region_url = api_access.get_region_url(region_name, service_name)

        self.assertNotEqual(region_url, None, "Can't get region url")

    def test_region_url_nover(self):
        api_access = ApiAccess()

        self.set_regions_for_fetcher(api_access)

        region_name = list(REGIONS.keys())[0]
        region = REGIONS[region_name]

        service_name = list(region['endpoints'].keys())[0]

        region_url = api_access.get_region_url_nover(region_name, service_name)

        self.assertNotEqual(region_url, None, "Can't get region url")
