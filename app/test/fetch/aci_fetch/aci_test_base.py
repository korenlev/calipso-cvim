import unittest
from unittest.mock import patch, MagicMock

import requests

import test.fetch.aci_fetch.test_data.aci_access as test_data
from discover.fetchers.aci.aci_access import AciAccess


class AciTestBase(unittest.TestCase):

    RESPONSES = {}

    def setUp(self):
        super().setUp()

        self.req_patcher = patch("discover.fetchers.aci.aci_access.requests")
        self.requests = self.req_patcher.start()
        self.requests.codes = requests.codes
        self.response = MagicMock()
        self.response.json.return_value = test_data.LOGIN_RESPONSE
        self.requests.get.return_value = self.response
        self.requests.post.return_value = self.response

        self.aci_access = AciAccess(config=test_data.ACI_CONFIG)

    def _requests_get(self, url, *args, **kwargs):
        response = MagicMock()
        return_value = next((resp
                             for endpoint, resp in self.RESPONSES.items()
                             if endpoint in url),
                            None)
        response.json.return_value = return_value
        return response

    def tearDown(self):
        self.req_patcher.stop()
        super().tearDown()

