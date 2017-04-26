import base64

from api.backends.ldap_access import LDAPAccess
from api.responders.responder_base import ResponderBase


class AuthenticationMiddleware(ResponderBase):
    def __init__(self, ldap_config=""):
        super().__init__()
        self.ldap_access = LDAPAccess(ldap_config)
        self.BASIC_AUTH = "AUTHORIZATION"
        self.TOKEN_AUTH = "X-AUTH-TOKEN"
        self.EXCEPTION_ROUTES = ['/auth/tokens']

    def process_request(self, req, resp):
        if req.path in self.EXCEPTION_ROUTES:
            return

        self.log.debug("Authentication middleware is processing the request")
        headers = self.change_dict_naming_convention(req.headers,
                                                     self.convert_to_uppercase)
        auth_error = None
        if self.BASIC_AUTH in headers:
            # basic authentication
            self.log.debug("Authenticating the basic credentials")
            basic = headers[self.BASIC_AUTH]
            auth_error = self.authenticate_with_basic_auth(basic)
        elif self.TOKEN_AUTH in headers:
            # token authentication
            self.log.debug("Authenticating token")
            token = headers[self.TOKEN_AUTH]
            auth_error = self.authenticate_with_token(token)
        else:
            auth_error = "Authentication required"

        if auth_error:
            self.unauthorized(auth_error)

    def authenticate_with_basic_auth(self, basic):
        error = None
        if not basic or not basic.startswith("Basic"):
            error = "Credentials not provided"
        else:
            # get username and password
            credential = basic.lstrip("Basic").lstrip()
            username_password = base64.b64decode(credential).decode("utf-8")
            credentials = username_password.split(":")
            if not self.ldap_access.authenticate_user(credentials[0],
                                                      credentials[1]):
                self.log.info("Authentication for {0} failed".format(credentials[0]))
                error = "Authentication failed"
            self.log.info("Authentication for {0} succeeded".format(credentials[0]))

        return error

    def authenticate_with_token(self, token):
        error = None
        return error

    def convert_to_uppercase(self, s):
        return s.upper()
