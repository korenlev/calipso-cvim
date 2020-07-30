###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from api.auth.auth import Auth
from api.auth.token import Token
from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from base.utils.string_utils import stringify_doc


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

        try:
            self.authenticate(auth)
        except KeyError as e:
            self.unauthorized("Missing key in auth payload: {}".format(e))
        except ValueError as e:
            self.unauthorized(str(e))

        new_token = Token.new_uuid_token(auth['method'])
        try:
            self.auth.write_token(new_token)
        except ValueError as e:
            # TODO if writing token to the database failed, what kind of error should be returned?
            self.bad_request(str(e))

        stringify_doc(new_token)
        self.set_created_response(resp, new_token)

    def authenticate(self, auth: dict):
        methods = auth['methods']
        credentials = auth.get('credentials')
        token = auth.get('token')

        if not token and not credentials:
            raise ValueError('You must provide either credentials or token')

        if 'credentials' in methods:
            if not credentials:
                raise ValueError('Credentials must be provided for credentials method')
            else:
                if not self.auth.validate_credentials(credentials['username'],
                                                      credentials['password']):
                    raise ValueError('Authentication failed')
                else:
                    auth['method'] = 'credentials'
                    return

        if 'token' in methods:
            if not token:
                raise ValueError('Token must be provided for token method')
            else:
                self.auth.validate_token(token)
                auth['method'] = 'token'
                return

    def on_delete(self, req, resp):
        headers = self.change_dict_naming_convention(req.headers,
                                                     lambda s: s.upper())
        if Token.FIELD not in headers:
            self.unauthorized('Authentication failed')

        token = headers[Token.FIELD]
        try:
            self.auth.validate_token(token)
        except ValueError as e:
            self.unauthorized(str(e))

        delete_error = self.auth.delete_token(token)

        if delete_error:
            self.bad_request(delete_error)

        self.set_ok_response(resp)
