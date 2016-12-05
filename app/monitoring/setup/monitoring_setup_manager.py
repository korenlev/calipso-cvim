# handle adding of monitoring setup as needed

import json
import pymongo
import socket

from boltons.iterutils import remap

from discover.mongo_access import MongoAccess
from discover.ssh_conn import SshConn
from discover.configuration import Configuration

class MonitoringSetupManager(MongoAccess):

  def __init__(self, mongo_conf_file):
    super().__init__(mongo_conf_file)
    self.config = Configuration()
    self.monitoring_config = self.db.monitoring_config
    self.env_monitoring_config = self.config.get('Monitoring')
    self.local_host = socket.gethostname()

  # add monitoring setup to Sensu server
  def server_setup(self):
    sensu_server_files = ['transport.json', 'client.json', 'rabbitmq.json', 
        'handlers.json', 'redis.json', 'api.json']
    if 'monitoring_setup_done' in self.config.env_config:
      return
    server_host = self.env_monitoring_config['server_ip']
    ssh = SshConn(server_host)
    config_folder = self.env_monitoring_config['config_folder']
    for file_name in sensu_server_files:
      content = self.prepare_config_file(file_name, {'side': 'server'},
			  self.env_monitoring_config)
      full_path = config_folder + '/' + file_name
      self.write_file(full_path, server_host, content)
    self.config.update_env({'monitoring_setup_done': True})

  def prepare_config_file(self, file_name, base_condition, config):
    condition = base_condition
    condition['type'] = file_name
    sort = [('order', pymongo.ASCENDING)]
    docs = self.monitoring_config.find(condition, sort=sort)
    content = {}
    for doc in docs:
      content.update(doc)
    content_remapped = remap(content['config'], visit=self.fill_values)
    return content_remapped

  def fill_values(self, path, key, value):
    if not path:
      return key, value
    if isinstance(value, dict):
      return key, value
    value = str(value)
    if '{' in value:
      value_formatted = value.format_map(self.env_monitoring_config)
      return key, value_formatted
    return key, value

  def write_file(self, file_path, host, content):
    # apply environment definitions to the config,
    # e.g. replace {server_ip} with the IP or host name for the server
    content_json = json.dumps(content, sort_keys=True, indent=4) + '\n'
    if host == self.local_host:
      # just write to file locally
      self.write_to_local_host(file_path, content_json)
    else:
			# remote host - use sftp
      ssh.write_file(full_path, content_json)

  def write_to_local_host(self, file_path, content):
    f = open(file_path, "w")
    f.write(content)
    f.close()

