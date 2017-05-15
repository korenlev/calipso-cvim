import json


from test.api.test_base import TestBase
from test.api.auth_test.test_data import base
from test.api.auth_test.test_data import tokens
from unittest.mock import patch


class TestTokens(TestBase):

    def test_create_token_without_auth_obj(self):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITHOUT_AUTH),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_create_token_without_methods(self):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITHOUT_METHODS),
                                   expected_code=base.BAD_REQUEST_CODE)

    def test_create_token_without_credentials_in_credentials_method(self):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITHOUT_CREDENTIALS),
                                   expected_code=base.UNAUTHORIZED_CODE)

    def test_create_token_without_token_in_token_method(self):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITHOUT_TOKEN),
                                   expected_code=base.UNAUTHORIZED_CODE)

    @patch(base.AUTH_VALIDATE_CREDENTIALS)
    def test_create_token_with_wrong_credentials(self, validate_credentials):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITH_WRONG_CREDENTIALS),
                                   mocks={
                                       validate_credentials: False
                                   },
                                   expected_code=base.UNAUTHORIZED_CODE)

    @patch(base.AUTH_VALIDATE_TOKEN)
    def test_create_token_with_wrong_token(self, validate_token):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITH_WRONG_TOKEN),
                                   mocks={
                                       validate_token: 'token error'
                                   },
                                   expected_code=base.UNAUTHORIZED_CODE)

    @patch(base.AUTH_WRITE_TOKEN)
    @patch(base.AUTH_VALIDATE_CREDENTIALS)
    def test_create_token_with_correct_credentials(self, validate_credentials, write_token):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITH_CORRECT_CREDENTIALS),
                                   mocks={
                                       validate_credentials: True,
                                       write_token: None
                                   },
                                   expected_code=base.CREATED_CODE)

    @patch(base.AUTH_WRITE_TOKEN)
    @patch(base.AUTH_VALIDATE_TOKEN)
    def test_create_token_with_correct_token(self, validate_token, write_token):
        self.validate_post_request(tokens.URL,
                                   body=json.dumps(tokens.AUTH_OBJ_WITH_CORRECT_TOKEN),
                                   mocks={
                                       validate_token: None,
                                       write_token: None
                                   },
                                   expected_code=base.CREATED_CODE)
