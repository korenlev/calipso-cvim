import os
import ssl
import sys

from ldap3 import Server, Connection, Tls
from utils.config_file import ConfigFile
from utils.logger import Logger
from utils.singleton import Singleton


class LDAPAccess(Logger, ConfigFile, metaclass=Singleton):

    default_config_file = "ldap.conf"
    TLS_REQUEST_CERTS = {
        "demand": ssl.CERT_REQUIRED,
        "allow": ssl.CERT_OPTIONAL,
        "never": ssl.CERT_NONE,
        "default": ssl.CERT_NONE
    }
    user_ssl = True

    def __init__(self, config_file=""):
        super().__init__()
        self.ldap_params = self.get_ldap_params(config_file)
        self.server = self.connect_ldap_server()

    def get_ldap_params(self, config_file):
        ldap_params = {
            "url": "ldap://localhost:389"
        }
        if not config_file:
            config_file = self.get_config_file(self.default_config_file)
            if not os.path.isfile(config_file):
                msg = "ldap config file doesn't exist: " + config_file
                self.log.error(msg)
                sys.exit(1)
        if config_file:
            try:
                params = self.read_config_from_config_file(config_file)
                ldap_params.update(params)
            except Exception:
                self.log.error("failed to open ldap config file: " +
                               config_file)
                raise
        if "user_tree_dn" not in ldap_params:
            raise ValueError("user_tree_dn must be specified in " +
                             config_file)
        if "user_id_attribute" not in ldap_params:
            raise ValueError("user_id_attribute must be specified in " +
                             config_file)
        return ldap_params

    def connect_ldap_server(self):
        if not self.ldap_params:
            self.ldap_params = self.get_ldap_params()

        ca_certificate_file = self.ldap_params.get('tls_cacertfile')
        req_cert = self.ldap_params.get('tls_req_cert')
        ldap_url = self.ldap_params.get('url')

        if ca_certificate_file:
            if not req_cert or req_cert not in self.TLS_REQUEST_CERTS.keys():
                req_cert = 'default'
            tls_req_cert = self.TLS_REQUEST_CERTS[req_cert]
            tls = Tls(local_certificate_file=ca_certificate_file,
                      validate=tls_req_cert)
            return Server(ldap_url, use_ssl=self.user_ssl, tls=tls)

        return Server(ldap_url, use_ssl=self.user_ssl)

    def authenticate_user(self, username, password):
        if not self.server:
            self.server = self.connect_ldap_server()

        user_dn = self.ldap_params['user_id_attribute'] + "=" + username + \
                  "," + self.ldap_params['user_tree_dn']
        connection = Connection(self.server, user=user_dn, password=password)
        # validate the user by binding
        # bound is true if binding succeed, otherwise false
        bound = connection.bind()
        connection.unbind()
        return bound
