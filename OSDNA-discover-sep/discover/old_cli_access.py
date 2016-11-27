import paramiko
import json
import os
 # older way to get from ssh master host (dep)
from configuration import Configuration
from fetcher import Fetcher

class CliAccess(Fetcher_new):

  initialized  = False
  config = None
  ssh = None
  
  def __init__(self):
    if CliAccess.initialized:
      return
    self.config = Configuration()
    self.conf = self.config.get('CLI')
    try:
      self.host = self.conf['host']
    except KeyError:
      raise ValueError('Missing definition of host for CLI access')
    try:
      self.user = self.conf['user']
    except KeyError:
      raise ValueError('Missing definition of user for CLI access')
    self.key = None
    try:
      self.key = self.conf['key']
      if not os.path.exists(self.key):
        raise ValueError('Key file not found: ' + self.key)
    except KeyError:
      pass
    try:
      self.pwd = self.conf['pwd']
    except KeyError:
      pass
    if self.key == None and self.pwd == None:
      raise ValueError('Must specify key or password for CLI access')
 
  def connect(self):
    if CliAccess.ssh:
      return
    CliAccess.ssh = SSHClient()
    if (self.key):
      k = paramiko.RSAKey.from_private_key_file(self.key)
      CliAccess.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      CliAccess.ssh.connect(hostname=self.host, username=self.user, pkey=k)
    else:
      CliAccess.ssh.connect(self.host, username=self.user,  password=self.pwd)
  
  def run(self, cmd):
    self.connect()
    stdin, stdout, stderr = CliAccess.ssh.exec_command(cmd)
    stdin.close()
    ret = self.binary2str(stdout.read())
    return ret
  
  def run_fetch_lines(self, cmd):
    out = self.run(cmd)
    if not out:
      return []
    # first try to split lines by whitespace
    ret = out.splitlines()
    # if split by whitespace did not work, try splitting by "\\n"
    if len(ret) == 1:
      ret = [l for l in out.split("\\n") if l != ""]
    return ret
 
  def parse_cmd_result(self, lines):
    headers = self.parse_headers_line(lines[1])
    # remove line with headers and formatting lines above it and below it
    del lines[:3]
    # remove formatting line in the end
    lines.pop()
    results = [self.parse_content_line(line, headers) for line in lines]
    return results
    
  def parse_line(self, line):
    s = self.binary2str(line)
    parts = [word.strip() for word in s.split("|") if word.strip()]
    # remove the ID field
    del parts[:1]
    return parts
  
  def parse_headers_line(self, line):
    return self.parse_line(line)
  
  def parse_content_line(self, line, headers):
    content_parts = self.parse_line(line)
    content = {}
    for i in range(0, len(content_parts)):
      content[headers[i]] = content_parts[i]
    return content
 
