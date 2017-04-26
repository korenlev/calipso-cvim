from datetime import datetime

from bson.objectid import ObjectId

from api.auth.auth import Auth
from api.auth.token import Token
from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from utils.string_utils import stringify_object_values_by_types, convert_to_uppercase


class Tokens(ResponderBase):

    def __init__(self):
        super().__init__()
        self.auth_requirements = {
            'methods': self.require(list, False,
                                    DataValidate.LIST,
                                    ['credentials', 'token'],
                                    True),
            'credentials': self.require(dict, True),
            'token': self.require(str)
        }

        self.credential_requirements = {
            'username': self.require(str, mandatory=True),
            'password': self.require(str, mandatory=True)
        }
        self.auth = Auth()

    def on_post(self, req, resp):
        self.log.debug('creating new token')
        error, data = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        if 'auth' not in data:
            self.bad_request('Request must contain auth object')

        auth = data['auth']

        self.validate_query_data(auth, self.auth_requirements)

        if 'credentials' in auth:
            self.validate_query_data(auth['credentials'],
                                     self.credential_requirements)

        auth_error = self.authenticate(auth)
        if auth_error:
            self.unauthorized(auth_error)

        new_token = Token.new_uuid_token(auth['methods'])
        write_error = self.auth.write_token(new_token)

        if write_error:
            # TODO if writing token to the database failed, what kind of error should be return?
            self.bad_request(write_error)

        stringify_object_values_by_types(new_token, [datetime, ObjectId])
        self.set_successful_response(resp, new_token, '201')

    def authenticate(self, auth):
        error = None
        methods = auth['methods']
        credentials = auth.get('credentials')
        token = auth.get('token')

        if 'credentials' in methods:
            if not credentials:
                error = 'credentials must be provided for credentials method'
            else:
                if not self.auth.validate_credentials(credentials['username'],
                                                       credentials['password']):
                    error = 'authentication failed'

        if 'token' in methods:
            if not token:
                error = 'token must be provided for token method'
            else:
                error = self.auth.validate_token(token)

        return error

    def on_delete(self, req, resp):
        headers = self.change_dict_naming_convention(req.headers,
                                                     convert_to_uppercase)
        if Token.FIELD not in headers:
            self.unauthorized('Authentication failed')

        token = headers[Token.FIELD]
        error = self.auth.validate_token(token)
        if error:
            self.unauthorized(error)

        delete_error = self.auth.delete_token(token)

        if delete_error:
            self.bad_request(delete_error)
