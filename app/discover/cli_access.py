import paramiko
import json

from configuration import Configuration
from fetcher import Fetcher

class CliAccess(Fetcher):

  initialized  = False
  config = None
  ssh = None
  
  def __init__(self):
    if CliAccess.initialized:
      return
    CliAccess.config = Configuration.instance.get('CLI')
    self.host = CliAccess.config['host']
    self.user = CliAccess.config['user']
    self.key = CliAccess.config['keyfile']
    self.pwd = CliAccess.config['pwd']
    if (self.host == None or self.user == None or self.key == None) and self.pwd == None:
      raise ValueError('Missing definition of host, user or key/pwd for CLI access')
 
  def connect(self):
    if CliAccess.ssh:
      return
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(self.host, username=self.user,  password=self.pwd)
  
  def run(self, cmd):
    connect()
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout
