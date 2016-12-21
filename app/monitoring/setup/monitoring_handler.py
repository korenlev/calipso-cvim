# handle specific setup of monitoring

import copy
import json
import os
import pymongo
import socket

from boltons.iterutils import remap

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from discover.mongo_access import MongoAccess
from discover.ssh_conn import SshConn
from utils.deep_merge import remerge


class MonitoringHandler(MongoAccess):

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file)
        self.config = Configuration()
        self.env = env
        self.monitoring_config = self.db.monitoring_config
        self.env_monitoring_config = self.config.get('Monitoring')
        self.replacements = self.env_monitoring_config
        self.local_host = socket.gethostname()
        self.inv = InventoryMgr()
        config_collection = self.inv.get_coll_name('monitoring_config')
        self.config_db = self.db[config_collection]

    def in_debug(self):
        conf = self.env_monitoring_config
        in_debug_mode = 'debug' in conf and bool(conf['debug'])
        return in_debug_mode

    def make_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def prepare_config_file(self, file_type, base_condition, config):
        condition = base_condition
        condition['type'] = file_type
        sort = [('order', pymongo.ASCENDING)]
        docs = self.monitoring_config.find(condition, sort=sort)
        content = {}
        for doc in docs:
            content.update(doc)
        return self.content_replace({'config': content['config']})

    def content_replace(self, content):
        content_remapped = remap(content, visit=self.fill_values)
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

    def get_config_from_db(self, host, file_type):
        find_tuple = {
            'environment': self.env,
            'host': host,
            'file': file_type
        }
        doc = self.config_db.find_one(find_tuple)
        if not doc:
            return {}
        doc.pop("_id", None)
        return self.decode_mongo_keys(doc)

    def write_config_to_db(self, host, config, file_type):
        find_tuple = {
            'environment': self.env,
            'host': host,
            'type': file_type
        }
        doc = copy.copy(find_tuple)
        doc.update(config)
        doc = self.encode_mongo_keys(doc)
        if not doc:
            return {}
        self.config_db.update_one(find_tuple, {'$set': doc}, upsert=True)

    def merge_config(self, host, file_type, content):
        """
        merge current monitoring config of host
        with newer content.
        return the merged config
        """
        doc = self.get_config_from_db(host, file_type)
        config = remerge([doc['config'], content]) if doc else content
        self.write_config_to_db(host, config, file_type)
        return config

    def write_config_file(self, file_type, file_path, host, content):
        """
        apply environment definitions to the config,
        e.g. replace {server_ip} with the IP or host name for the server
        """
        # save the config to DB first, and while doing that
        # merge it with any existing config on same host
        content = self.merge_config(host, file_type, content)

        # now dump the config to the file
        content_json = json.dumps(content, sort_keys=True, indent=4) + '\n'
        if self.in_debug() or host == self.local_host:
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
