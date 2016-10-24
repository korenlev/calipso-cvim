from unittest.mock import MagicMock

from discover.api_access import ApiAccess
from discover.api_fetch_regions import ApiFetchRegions
from test.fetch.test_fetch import TestFetch
from test.fetch.token import TOKEN
from test_data.api_fetch_regions import *


class TestApiFetchRegions(TestFetch):

    def setUp(self):
        ApiFetchRegions.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.configure_environment()

    def test_get(self):
        fetcher = ApiFetchRegions()
        # mock the auth response from OpenStack Api
        ApiAccess.auth_response = AUTH_RESPONSE
        # set environment
        fetcher.set_env(self.env)

        ret = fetcher.get("test_id")
        self.assertNotEqual(ret, [], "Can't get regions information")

    def test_get_without_token(self):
        # mock the empty token info
        ApiFetchRegions.v2_auth_pwd = MagicMock(return_value=[])

        fetcher = ApiFetchRegions()
        fetcher.set_env(self.env)

        ret = fetcher.get("test_id")

        # reset token info
        ApiFetchRegions.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.assertEqual(ret, [], "Can't get empty array when the token is invalid")