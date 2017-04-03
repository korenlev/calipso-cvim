import os

from discover.configuration import Configuration
from utils.inventory_mgr import InventoryMgr
from utils.ssh_connection import SshConnection


class SshConn(SshConnection):
    config = None
    ssh = None
    connections = {}
    call_count_per_con = {}

    max_call_count_per_con = 100
    timeout = 15  # timeout for exec in seconds

    def __init__(self, host_name):
        self.config = Configuration()
        self.env_config = self.config.get_env_config()
        self.env = self.env_config['name']
        self.conf = self.config.get('CLI')
        self.host_details = None
        self.host = None
        self.host_conf = self.get_host_conf(host_name)
        self.ssh = None
        self.ftp = None
        self.key = None
        self.port = None
        self.user = None
        self.pwd = None
        self.check_definitions()
        super().__init__(self.host, self.user, _pwd=self.pwd, _key=self.key,
                         _port=self.port)
        self.inv = InventoryMgr()
        if host_name in self.connections and not self.ssh:
            self.ssh = self.connections[host_name]
        self.fetched_host_details = False

    def get_host_conf(self, host_name):
        if 'hosts' in self.conf:
            if not host_name:
                raise ValueError('SshConn(): host must be specified ' +
                                 'if multi-host CLI config is used')
            if host_name not in self.conf['hosts']:
                raise ValueError('host details missing: ' + host_name)
            return self.conf['hosts'][host_name]
        else:
            return self.conf

    def check_definitions(self):
        try:
            self.host = self.host_conf['host']
            if self.host in self.connections:
                self.ssh = self.connections[self.host]
        except KeyError:
            raise ValueError('Missing definition of host for CLI access')
        try:
            self.user = self.host_conf['user']
        except KeyError:
            raise ValueError('Missing definition of user for CLI access')
        try:
            self.key = self.host_conf['key']
            if self.key and not os.path.exists(self.key):
                raise ValueError('Key file not found: ' + self.key)
        except KeyError:
            pass
        try:
            self.pwd = self.host_conf['pwd']
        except KeyError:
            self.pwd = None
        if not self.key and not self.pwd:
            raise ValueError('Must specify key or password for CLI access')

    def get_host_details(self):
        if not self.fetched_host_details:
            host = self.inv.get_by_id(self.env, self.host)
            if not host:
                host = self.inv.find_items({'environment': self.env,
                                            'type': 'host',
                                            'ip_address': self.host},
                                           get_single=True)
            self.host_details = host
            self.fetched_host_details = True
        return self.host_details

    def is_gateway_host(self, host):
        gateway_host = self.host
        if host == gateway_host:
            return True
        # the values might not match if one is an IP address,
        # so need to look in gateway host details
        gateway_host_details = self.get_host_details()
        if gateway_host_details and host == gateway_host_details['id']:
            return True
        if gateway_host_details and host == gateway_host_details['ip_address']:
            return True
        return False

