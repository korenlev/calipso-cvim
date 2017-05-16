import copy


from api.app import App
from api.middleware.authentication import AuthenticationMiddleware
from api.responders.responder_base import ResponderBase
from falcon.testing import TestCase
from test.api.responders_test.test_data import base
from unittest.mock import MagicMock


def mock_auth_method(*args):
    return None


class TestBase(TestCase):

    def setUp(self, authenticate=False):
        super().setUp()
        # mock
        self.authenticate = authenticate
        if not authenticate:
            self.original_auth_method = AuthenticationMiddleware.process_request
            AuthenticationMiddleware.process_request = mock_auth_method

        ResponderBase.get_constants_by_name = MagicMock(side_effect=
                                                        lambda name: base.CONSTANTS_BY_NAMES[name])

        log_level = 'debug'
        self.app = App(log_level=log_level).get_app()

    def validate_get_request(self, url, params={}, headers=None, mocks={},
                             side_effects={},
                             expected_code=base.SUCCESSFUL_CODE,
                             expected_response=None):
        self.validate_request("GET", url, params, headers, "",
                              mocks, side_effects,
                              expected_code,
                              expected_response)

    def validate_request(self, action, url, params, headers, body,
                         mocks, side_effects, expected_code,
                         expected_response):
        for mock_method, mock_data in mocks.items():
            mock_method.return_value = mock_data

        for mock_method, side_effect in side_effects.items():
            mock_method.side_effect = side_effect

        result = self.simulate_request(action, url, params=params, headers=headers, body=body)
        self.assertEqual(result.status, expected_code)
        if expected_response:
            self.assertEqual(result.json, expected_response)

    def validate_post_request(self, url, headers={}, body="", mocks={},
                              side_effects={},
                              expected_code=base.CREATED_CODE, expected_response=None):
        self.validate_request("POST", url, {}, headers, body, mocks, side_effects,
                              expected_code, expected_response)

    def validate_delete_request(self, url, params={}, headers={}, mocks={},
                                side_effects={},
                                expected_code=base.SUCCESSFUL_CODE, expected_response=None):
        self.validate_request("DELETE", url, params, headers, "",
                              mocks, side_effects,
                              expected_code,
                              expected_response)

    def get_updated_data(self, original_data, deleted_keys=[], updates={}):
        copy_data = copy.deepcopy(original_data)

        for key in deleted_keys:
            del copy_data[key]

        for key, value in updates.items():
            copy_data[key] = value

        return copy_data

    def tearDown(self):
        # if the authentication method has been mocked, it needs to be reset after test
        if not self.authenticate:
            AuthenticationMiddleware.process_request = self.original_auth_method
