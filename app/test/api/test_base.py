from api.app import App
from api.responders.responder_base import ResponderBase
from falcon.testing import TestCase
from test.api.responders_test.test_data import base
from unittest.mock import MagicMock


class TestBase(TestCase):

    def setUp(self):
        super().setUp()
        log_level = 'debug'
        self.app = App(log_level=log_level).get_app()
        ResponderBase.get_constants_by_name = MagicMock(side_effect=
                                                        lambda name: base.CONSTANTS_BY_NAMES[name]
                                                        )

    def validate_get_request(self, url, params={}, headers=None, mocks={},
                             expected_code=base.SUCCESSFUL_CODE,
                             expected_response=None):
        self.validate_request("GET", url, params, headers, "",
                              mocks, expected_code,
                              expected_response)

    def validate_request(self, action, url, params, headers, body,
                         mocks, expected_code,
                         expected_response):
        for mock_method, mock_data in mocks.items():
            mock_method.return_value = mock_data

        result = self.simulate_request(action, url, params=params, headers=headers, body=body)
        self.assertEqual(result.status, expected_code)
        if expected_response:
            self.assertEqual(result.json, expected_response)

    def validate_post_request(self, url, headers={}, body="", mocks={},
                              expected_code=base.CREATED_CODE, expected_response=None):
        self.validate_request("POST", url, {}, headers, body, mocks,
                              expected_code, expected_response)
