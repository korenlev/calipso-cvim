import paramiko
import os

from configuration import Configuration
from fetcher import Fetcher

class SshConn(Fetcher):

  config = None
  ssh = None
  connections = {}
  call_count_per_con = {}
  max_call_count_per_con = 100

  def __init__(self, host_name):
    super().__init__()
    self.config = Configuration()
    self.conf = self.config.get('CLI')
    if 'hosts' in self.conf:
      if not host_name:
        raise ValueError('SshConn(): host must be specified ' +
          'if multi-host CLI config is used')
      if host_name not in self.conf['hosts']:
        raise ValueError('host details missing: ' + host_name)
      self.host_conf = self.conf['hosts'][host_name]
    else:
      self.host_conf = self.conf
    try:
      self.host = self.host_conf['host']
      if self.host in self.connections:
        self.ssh = self.connections[self.host]
        return
    except KeyError:
      raise ValueError('Missing definition of host for CLI access')
    if host_name in self.connections:
      self.ssh = self.connections[host_name]
      return
    try:
      self.user = self.host_conf['user']
    except KeyError:
      raise ValueError('Missing definition of user for CLI access')
    self.key = None
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
    if self.key == None and self.pwd == None:
      raise ValueError('Must specify key or password for CLI access')

  def connect(self):
    if self.host in self.connections:
      self.ssh = self.connections[self.host]
    if self.ssh:
      if self.call_count_per_con[self.host] < self.max_call_count_per_con:
        return
      self.log.info("CliAccess: ****** forcing reconnect, call count: %s ******",
        self.call_count_per_con[self.host])
      self.ssh = None
    self.ssh = paramiko.SSHClient()
    self.connections[self.host] = self.ssh
    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if (self.key):
      k = paramiko.RSAKey.from_private_key_file(self.key)
      self.ssh.connect(hostname=self.host, username=self.user, pkey=k,
        password=self.pwd,timeout=30)
    else:
      self.ssh.connect(self.host, username=self.user, password=self.pwd,
        timeout=30)
    self.call_count_per_con[self.host] = 0

  def exec(self, cmd):
    self.connect()
    self.call_count_per_con[self.host] +=1
    self.log.debug("call count: %s, running call:\n%s\n",
      str(self.call_count_per_con[self.host]), cmd)
    stdin, stdout, stderr = self.ssh.exec_command(cmd)
    stdin.close()
    err = self.binary2str(stderr.read())
    if err:
      self.log.error("CLI access: " + err + ",cmd:\n" + cmd)
      return ""
    ret = self.binary2str(stdout.read())
    return ret
