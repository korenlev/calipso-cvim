import base64

from api.backends.ldap_access import LDAPAccess
from api.responders.responder_base import ResponderBase


class AuthenticationMiddleware(ResponderBase):
    def __init__(self, ldap_config=""):
        super().__init__()
        self.ldap_access = LDAPAccess(ldap_config)
        self.BASIC_AUTH = "AUTHORIZATION"

    def process_request(self, req, resp):
        self.log.debug("Authentication middleware is processing the request")
        headers = self.change_dict_naming_convention(req.headers,
                                                     self.convert_to_uppercase)

        # check whether it has basic authentication info in the headers
        if self.BASIC_AUTH in headers:
            self.log.debug("Authenticating the basic credentials")
            basic = headers[self.BASIC_AUTH]
            if not basic or not basic.startswith("Basic"):
                self.unauthorized("Credentials not provided")
            else:
                # get username and password
                credential = basic.lstrip("Basic").lstrip()
                username_password = base64.b64decode(credential).decode("utf-8")
                credentials = username_password.split(":")
                if not self.ldap_access.authenticate_user(credentials[0],
                                                          credentials[1]):
                    self.log.info("Authentication for {0} failed".format(credentials[0]))
                    self.unauthorized("Authentication failed")
                self.log.info("Authentication for {0} succeeded".format(credentials[0]))
        else:
            self.unauthorized("Authentication required")

    def convert_to_uppercase(self, s):
        return s.upper()
