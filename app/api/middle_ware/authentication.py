import base64

from api.responders.responder_base import ResponderBase
from api.backends.ldap_access import LDAPAccess


class AuthenticationMiddleware(ResponderBase):

    def __init__(self):
        super().__init__()
        self.ldap_access = LDAPAccess()
        self.basic_auth = "AUTHORIZATION"

    def process_request(self, req, resp):
        self.log.debug("Authentication middleware is processing the request")
        uppercase_headers = self.convert_object_keys_to_uppercase(req.headers)

        # check whether it has basic authentication info in the headers
        if self.basic_auth in uppercase_headers:
            self.log.debug("Authenticating the username and password information")
            basic = uppercase_headers[self.basic_auth]
            if not basic or not basic.startswith("Basic"):
                self.unauthorized(message="No credential is provided")
            else:
                # get username and password
                credential = basic.lstrip("Basic").lstrip()
                username_password = base64.b64decode(credential).decode("utf-8")
                separator_index = username_password.index(':')
                username = username_password[:separator_index]
                password = username_password[separator_index + 1:]

                if not self.ldap_access.authenticate_user(username, password):
                    self.unauthorized("Authentication failed")
        else:
            self.unauthorized("The resources you request requires authentication")


