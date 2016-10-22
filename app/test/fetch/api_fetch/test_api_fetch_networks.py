from discover.api_fetch_networks import ApiFetchNetworks
from test.fetch.test_fetch import TestFetch
from unittest.mock import MagicMock
from test_data.api_fetch_networks import *
from test_data.token import TOKEN


class TestApiFetchNetworks(TestFetch):

    def setUp(self):
        self.configure_environment()
        ApiFetchNetworks.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.fetcher = ApiFetchNetworks()
        self.set_regions_for_fetcher(self.fetcher)

    def test_get_for_region(self):
        # mock endpoint
        self.fetcher.get_region_url_nover = MagicMock(return_value=ENDPOINT)
        # mock networks response and subnet response
        self.fetcher.get_url = MagicMock(side_effect=[NETWORKS_RESPONSE, SUBNETS_RESPONSE])
        # mock project info
        self.fetcher.inv.get_by_id = MagicMock(return_value=PROJECT)

        result = self.fetcher.get_for_region(REGION_NAME, TOKEN)
        self.assertNotEqual(result, [], "Can't get networks info")
        self.assertIn("project", result[0], "Can't put project info in the network doc")

    def test_get_for_region_with_wrong_networks_response(self):
        # mock endpoint
        self.fetcher.get_region_url_nover = MagicMock(return_value=ENDPOINT)
        # mock the wrong networks response
        self.fetcher.get_url = MagicMock(return_value=WRONG_NETWORK_RESPONSE)

        result = self.fetcher.get_for_region(REGION_NAME, TOKEN)
        self.assertEqual(result, [], "Can't get empty empty when the networks response is wrong")

    def test_get_for_region_with_wrong_subnet_response(self):
        # mock endpoint
        self.fetcher.get_region_url_nover = MagicMock(return_value=ENDPOINT)
        # mock the correct networks response and wrong subnets response
        self.fetcher.get_url = MagicMock(side_effect=[NETWORKS_RESPONSE, WRONG_SUBNETS_RESPONSE])
        # mock project info
        self.fetcher.inv.get_by_id = MagicMock(return_value=PROJECT)

        result = self.fetcher.get_for_region(REGION_NAME, TOKEN)

        self.assertNotEqual(result, [], "Can't get networks info when the subnets response is wrong")

    def test_get(self):
        # store original get_for_region method
        original_method = self.fetcher.get_for_region
        # mock the get_for_region method
        self.fetcher.get_for_region = MagicMock(return_value=GET_FOR_REGION)

        result = self.fetcher.get(REGION_NAME)

        # reset get_for_region method
        self.fetcher.get_for_region = original_method
        self.assertNotEqual(result, [], "Can't get region networks info")

    def test_get_with_wrong_token(self):
        # mock the token
        self.fetcher.v2_auth_pwd = MagicMock(return_value=None)

        result = self.fetcher.get(REGION_NAME)

        # reset token
        self.fetcher.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.assertEqual(result, [], "Can't get empty array when the token is invalid")