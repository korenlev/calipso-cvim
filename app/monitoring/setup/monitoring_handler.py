# handle specific setup of monitoring

import copy
import json
import os
import pymongo
import shutil
import socket
import subprocess

from boltons.iterutils import remap

from discover.cli_access import CliAccess
from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from discover.mongo_access import MongoAccess
from discover.ssh_conn import SshConn
from utils.deep_merge import remerge
from utils.binary_converter import BinaryConverter


class MonitoringHandler(MongoAccess, CliAccess, BinaryConverter):
    PRODUCTION_CONFIG_DIR = '/etc/sensu/conf.d'

    pending_changes = {}

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file)
        self.config = Configuration()
        self.env = env
        self.monitoring_config = self.db.monitoring_config_templates
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

    # create a directory if it does not exist
    def make_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def get_config_dir(self, sub_dir=''):
        config_folder = self.env_monitoring_config['config_folder'] + \
            ('/' + sub_dir if sub_dir else '')
        return self.make_directory(config_folder)

    def prepare_config_file(self, file_type, base_condition):
        condition = base_condition
        condition['type'] = file_type
        sort = [('order', pymongo.ASCENDING)]
        docs = self.monitoring_config.find(condition, sort=sort)
        content = {}
        for doc in docs:
            content.update(doc)
        self.replacements['app_path'] = self.config.env_config['app_path']
        config = self.content_replace({'config': content['config']})
        return config

    def content_replace(self, content):
        content_remapped = remap(content, visit=self.fill_values)
        return content_remapped

    def format_string(self, val):
        formatted = val if not isinstance(val, str) or '{' not in val \
            else val.format_map(self.replacements)
        return formatted

    def fill_values(self, path, key, value):
        if not path:
            return key, value
        key_formatted = self.format_string(key)
        value_formatted = self.format_string(value)
        return key_formatted, value_formatted

    def get_config_from_db(self, host, file_type):
        find_tuple = {
            'environment': self.env,
            'host': host,
            'type': file_type
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

    def write_config_file(self, file_name, sub_dir, host, content):
        """
        apply environment definitions to the config,
        e.g. replace {server_ip} with the IP or host name for the server
        """
        # save the config to DB first, and while doing that
        # merge it with any existing config on same host
        content = self.merge_config(host, file_name, content)

        # now dump the config to the file
        content_json = json.dumps(content['config'], sort_keys=True, indent=4)
        content_json = content_json + '\n'
        # always write the file locally first
        local_dir = self.make_directory(self.get_config_dir() + '/' + sub_dir)
        local_path = local_dir + '/' + file_name
        self.write_to_local_host(local_path, content_json)
        self.track_pending_host_setup_changes(host, file_name, local_path,
                                              sub_dir)

    def track_pending_host_setup_changes(self, host, file_name, local_path,
                                         sub_dir):
        if host not in self.pending_changes:
            self.pending_changes[host] = {}
        if file_name not in self.pending_changes[host]:
            self.pending_changes[host][file_name] = {
                "host": host,
                "file_name": file_name,
                "local_path": local_path,
                "sub_dir": sub_dir
            }

    def handle_pending_setup_changes(self):
        self.log.info('applying monitoring setup')
        for host, host_changes in self.pending_changes.items():
            self.handle_pending_host_setup_changes(host_changes)
        self.log.info('done applying monitoring setup')

    def handle_pending_host_setup_changes(self, host_changes):
        if self.in_debug():
            return
        host = None
        for file_type, changes in host_changes.items():
            host = changes['host']
            self.log.debug('applying monitoring setup changes ' +
                           'for host ' + host + ', file type: ' + file_type)
            is_local_host = host == self.local_host
            file_path = self.PRODUCTION_CONFIG_DIR + '/' + file_type
            if is_local_host:
                # write to production configuration directory on local host
                self.make_directory(self.PRODUCTION_CONFIG_DIR)
                shutil.copy(changes['local_path'], file_path)
            else:
                # write to remote host prepare dir - use sftp
                self.write_to_remote_host(host, changes['local_path'],
                                          changes['file_name'])
        if not is_local_host:
            # copy the files to remote target config directory
            self.make_remote_dir(host, self.PRODUCTION_CONFIG_DIR)
            local_path = changes['local_path']
            local_dir = local_path[:local_path.rindex('/')]
            self.move_setup_files_to_remote_host(host, local_dir)
            # restart the Sensu client on the remote host,
            # so it takes the new setup
            self.run('sudo /etc/init.d/sensu-service client restart',
                     ssh_to_host=host)

    def run_cmd_locally(self, cmd):
        try:
            subprocess.popen(cmd.split(),
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("Error running command: " + cmd +
                  ", output: " + self.binary2str(e.output) + "\n")

    def move_setup_files_to_remote_host(self, host, local_dir):
        if self.is_gateway_host(host):
            # do a simple copy on the gateway host
            self.run('cp ' + local_dir + '/* ' + self.PRODUCTION_CONFIG_DIR,
                     enable_cache=False)
            return
        # need to scp the files from the gateway host to the target host
        ssh = SshConn(host)
        remote_path = ssh.get_user() + '@' + host + ':' + \
            self.PRODUCTION_CONFIG_DIR + '/'
        self.make_remote_dir(host, remote_path)
        self.run_on_gateway('scp ' + local_dir + '/* ' + remote_path,
                            ssh_to_host=host, enable_cache=False)

    def make_remote_dir(self, host, path, path_is_file=False):
        # make sure we have write permissions in target directories
        dir = path
        if path_is_file:
            dir = dir[:dir.rindex('/')]
        ssh = SshConn(host)
        cmd = 'sudo mkdir -p ' + dir + \
            ' && sudo chown -R ' + ssh.get_user() + ' ' + dir
        self.run(cmd, ssh_to_host=host)

    def copy_to_remote_host(self, host, local_path, remote_path, mode=None):
        # copy the local file to the remote host
        ssh = SshConn(host)
        self.make_remote_dir(host, remote_path, path_is_file=True)
        ssh.copy_file(local_path, remote_path, mode)

    def write_to_remote_host(self, host, local_path, file_name):
        remote_path = local_path  # copy to config dir first
        self.copy_to_remote_host(host, local_path, remote_path)

    def write_to_local_host(self, file_path, content):
        f = open(file_path, "w")
        f.write(content)
        f.close()
        return file_path
