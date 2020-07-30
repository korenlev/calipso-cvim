###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import base64
from typing import Optional

from api.auth.auth import Auth
from api.auth.token import Token
from api.responders.responder_base import ResponderBase


class AuthenticationMiddleware(ResponderBase):
    def __init__(self, log_file: Optional[str] = None, log_level: Optional[str] = None):
        super().__init__(log_file=log_file, log_level=log_level)
        self.auth = Auth(log_file=log_file, log_level=log_level)
        self.BASIC_AUTH = "AUTHORIZATION"
        self.EXCEPTION_ROUTES = ['/auth/tokens']

    def process_request(self, req, resp):
        if req.path in self.EXCEPTION_ROUTES:
            return

        self.log.debug("Authentication middleware is processing the request")
        headers = self.change_dict_naming_convention(req.headers,
                                                     lambda s: s.upper())
        auth_error = None
        if self.BASIC_AUTH in headers:
            # basic authentication
            self.log.debug("Authenticating the basic credentials")
            basic = headers[self.BASIC_AUTH]
            try:
                self.authenticate_with_basic_auth(basic)
            except ValueError as e:
                auth_error = str(e)
        elif Token.FIELD in headers:
            # token authentication
            self.log.debug("Authenticating token")
            token = headers[Token.FIELD]
            try:
                self.auth.validate_token(token)
            except ValueError as e:
                auth_error = str(e)
        else:
            auth_error = "Authentication required"

        if auth_error:
            self.unauthorized(auth_error)

    def authenticate_with_basic_auth(self, basic: str) -> None:
        if not basic or not basic.startswith("Basic"):
            raise ValueError("Credentials not provided")
        else:
            # get username and password
            credential = basic.lstrip("Basic").lstrip()
            username_password = base64.b64decode(credential).decode("utf-8")
            credentials = username_password.split(":")
            if not self.auth.validate_credentials(credentials[0], credentials[1]):
                self.log.debug("Authentication for {0} failed".format(credentials[0]))
                raise ValueError("Authentication failed")
            else:
                self.log.debug("Authentication for {0} succeeded".format(credentials[0]))


class CORSMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')

        if (req_succeeded
                and req.method == 'OPTIONS'
                and req.get_header('Access-Control-Request-Method')):

            # This is a CORS preflight request.
            # Patch the response accordingly.
            allow = resp.get_header('Allow')
            resp.delete_header('Allow')

            allow_headers = req.get_header(
                'Access-Control-Request-Headers',
                default='*'
            )

            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'),  # 24 hours
            ))
