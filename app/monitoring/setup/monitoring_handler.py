# handle specific setup of monitoring

import json
import os
import pymongo
import socket

from boltons.iterutils import remap

from discover.mongo_access import MongoAccess
from discover.ssh_conn import SshConn
from discover.configuration import Configuration


class MonitoringHandler(MongoAccess):

    def __init__(self, mongo_conf_file):
        super().__init__(mongo_conf_file)
        self.config = Configuration()
        self.monitoring_config = self.db.monitoring_config
        self.env_monitoring_config = self.config.get('Monitoring')
        self.replacements = self.env_monitoring_config
        self.local_host = socket.gethostname()

    def make_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def prepare_config_file(self, file_name, base_condition, config):
        condition = base_condition
        condition['type'] = file_name
        sort = [('order', pymongo.ASCENDING)]
        docs = self.monitoring_config.find(condition, sort=sort)
        content = {}
        for doc in docs:
            content.update(doc)
        return self.content_replace(content['config'])

    def content_replace(self, content):
        content_remapped = remap(content['config'], visit=self.fill_values)
        return content_remapped

    def fill_values(self, path, key, value):
        if not path:
            return key, value
        if isinstance(value, dict):
            return key, value
        value = str(value)
        if '{' in value:
            value_formatted = value.format_map(self.replacements)
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
            ssh = SshConn(host)
            ssh.write_file(file_path, content_json)

    def write_to_local_host(self, file_path, content):
        f = open(file_path, "w")
        f.write(content)
        f.close()
