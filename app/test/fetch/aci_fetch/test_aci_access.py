from unittest.mock import MagicMock

import requests
from copy import deepcopy

from discover.fetchers.aci.aci_access import AciAccess
import test.fetch.aci_fetch.test_data.aci_access as test_data
from test.fetch.aci_fetch.aci_test_base import AciTestBase


class TestAciAccess(AciTestBase):

    def test_login(self):

        self.aci_access.login()
        new_token = deepcopy(AciAccess.cookie_token)
        AciAccess.reset_token()

        self.assertEqual(test_data.VALID_COOKIE_TOKEN, new_token)

    def test_refresh_no_token(self):

        self.aci_access.refresh_token()
        new_token = deepcopy(AciAccess.cookie_token)
        AciAccess.reset_token()

        self.assertEqual(test_data.VALID_COOKIE_TOKEN, new_token)

    def test_refresh_ok_token(self):

        AciAccess.cookie_token = test_data.VALID_COOKIE_TOKEN
        self.aci_access.refresh_token()
        new_token = deepcopy(AciAccess.cookie_token)
        AciAccess.reset_token()

        self.assertEqual(test_data.VALID_COOKIE_TOKEN, new_token)

    def test_refresh_expired_token(self):

        AciAccess.cookie_token = test_data.VALID_COOKIE_TOKEN
        refresh_response_expired = MagicMock()
        refresh_response_expired.status_code = requests.codes.forbidden
        self.requests.get.return_value = refresh_response_expired
        self.aci_access.refresh_token()
        new_token = deepcopy(AciAccess.cookie_token)
        AciAccess.reset_token()

        self.assertEqual(test_data.VALID_COOKIE_TOKEN, new_token)
