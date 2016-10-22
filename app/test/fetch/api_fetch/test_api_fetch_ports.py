from discover.api_fetch_ports import ApiFetchPorts
from test.fetch.test_fetch import TestFetch
from test_data.api_fetch_ports import *
from test_data.token import *
from unittest.mock import MagicMock


class TestApiFetchPorts(TestFetch):

    def setUp(self):
        self.configure_environment()
        ApiFetchPorts.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.fetcher = ApiFetchPorts()
        self.set_regions_for_fetcher(self.fetcher)

    def get_ports_for_region(self):
        # mock endpoint
        self.fetcher.get_region_url = MagicMock(return_value=ENDPOINT)
        # mock ports info from OpenStack Api
        self.fetcher.get_url = MagicMock(return_value=PORTS_RESPONSE)

        result = self.fetcher.get_ports_for_region(REGION_NAME, TOKEN)

        self.assertNotEqual(result, [], "Can't get ports info")

    def test_get_ports_for_region_with_wrong_ports_response(self):
        # mock endpoint
        self.fetcher.get_region_url = MagicMock(return_value=ENDPOINT)
        # mock ports info from OpenStack Api
        self.fetcher.get_url = MagicMock(return_value=ERROR_PORTS_RESPONSE)

        result = self.fetcher.get_ports_for_region(REGION_NAME, TOKEN)

        self.assertEqual(result, [], "Can't get ports info")

    def test_get(self):
        # store original get_ports_for_region method
        original_method = self.fetcher.get_ports_for_region
        # mock get_ports_for_region result
        self.fetcher.get_ports_for_region = MagicMock(return_value=GET_PORTS_FOR_REGION)

        result = self.fetcher.get(REGION_NAME)

        # reset get_ports_for_region method
        self.fetcher.get_ports_for_region = original_method

        self.assertNotEqual(result, [], "Can't get ports info")

    def test_get_with_wrong_token(self):
        # set the invalid token
        self.fetcher.v2_auth_pwd = MagicMock(return_value=None)
        result = self.fetcher.get(REGION_NAME)

        # reset v2_auth_pwd method
        self.fetcher.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.assertEqual(result, [], "Can't get empty array when the token is invalid")
