from collections import defaultdict

import os

import paramiko

from utils.binary_converter import BinaryConverter
from utils.logger import Logger


class SshConnection(BinaryConverter, Logger):
    config = None
    ssh = None
    connections = {}
    call_count_per_con = defaultdict(int)

    max_call_count_per_con = 100
    timeout = 15  # timeout for exec in seconds

    DEFAULT_PORT = 22

    def __init__(self, _host, _user, _pwd=None, _key=None, _port=None):
        super().__init__()
        self.host = _host
        self.ssh = None
        self.ftp = None
        self.key = _key
        self.port = _port
        self.user = _user
        self.pwd = _pwd
        self.check_definitions()
        if self.host in self.connections and not self.ssh:
            self.ssh = self.connections[self.host]
        self.fetched_host_details = False

    def check_definitions(self):
        if self.host in self.connections:
            self.ssh = self.connections[self.host]
        if not self.host:
            raise ValueError('Missing definition of host for CLI access')
        if not self.user:
            raise ValueError('Missing definition of user ' +
                             'for CLI access to host {}'.format(self.host))
        if self.key and not os.path.exists(self.key):
            raise ValueError('Key file not found: ' + self.key)
        if not self.key and not self.pwd:
            raise ValueError('Must specify key or password ' +
                             'for CLI access to host {}'.format(self.host))

    @staticmethod
    def disconnect_all():
        for ssh in SshConnection.connections.values():
            ssh.close()
        SshConnection.connections = {}

    def get_host(self):
        return self.host

    def get_user(self):
        return self.user

    def connect(self):
        if self.host in self.connections:
            self.ssh = self.connections[self.host]
        if self.ssh is not None:
            if self.call_count_per_con[self.host] < self.max_call_count_per_con:
                return
            self.log.info("CliAccess: ****** forcing reconnect, " +
                          "call count: %s ******",
                          self.call_count_per_con[self.host])
            self.ssh.close()
            if self.host in self.connections:
                self.connections.pop(self.host)
            self.ssh = None
        self.ssh = paramiko.SSHClient()
        self.connections[self.host] = self.ssh
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.key:
            k = paramiko.RSAKey.from_private_key_file(self.key)
            self.ssh.connect(hostname=self.host, username=self.user, pkey=k,
                             port=self.port if self.port is not None
                             else self.DEFAULT_PORT,
                             password=self.pwd, timeout=30)
        else:
            self.ssh.connect(self.host, username=self.user, password=self.pwd,
                             port=self.port if self.port is not None
                             else self.DEFAULT_PORT,
                             timeout=30)
        self.call_count_per_con[self.host] = 0

    def exec(self, cmd):
        self.connect()
        self.call_count_per_con[self.host] += 1
        self.log.debug("call count: %s, running call:\n%s\n",
                       str(self.call_count_per_con[self.host]), cmd)
        stdin, stdout, stderr = self.ssh.exec_command(cmd, timeout=self.timeout)
        stdin.close()
        err = self.binary2str(stderr.read())
        if err:
            # ignore messages about loading plugin
            err_lines = [l for l in err.splitlines()
                         if 'Loaded plugin: ' not in l]
            if err_lines:
                self.log.error("CLI access: \n" +
                               "Host: {}\nCommand: {}\nError: {}\n".
                               format(self.host, cmd, err))
                stderr.close()
                stdout.close()
                return ""
        ret = self.binary2str(stdout.read())
        stderr.close()
        stdout.close()
        return ret

    def copy_file(self, local_path, remote_path, mode=None):
        self.connect()
        if not self.ftp:
            self.ftp = self.ssh.open_sftp()
        try:
            self.ftp.put(local_path, remote_path)
            remote_file = self.ftp.file(remote_path, 'a+')
            if mode:
                remote_file.chmod(mode)
        except IOError:
            self.log.error('failed to copy file to remote host ' + self.host)

    def is_gateway_host(self, host):
        return True
