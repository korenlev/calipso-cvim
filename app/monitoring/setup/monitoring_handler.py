# handle specific setup of monitoring

import copy
import json
import os
import pymongo
import shutil
import subprocess

from boltons.iterutils import remap

from utils.cli_access import CliAccess
from discover.configuration import Configuration
from discover.ssh_conn import SshConn
from utils.binary_converter import BinaryConverter
from utils.deep_merge import remerge
from utils.inventory_mgr import InventoryMgr
from utils.mongo_access import MongoAccess
from utils.ssh_connection import SshConnection


class MonitoringHandler(MongoAccess, CliAccess, BinaryConverter):
    PRODUCTION_CONFIG_DIR = '/etc/sensu/conf.d'

    provision_levels = {
        'none': 0,
        'db': 1,
        'files': 2,
        'deploy': 3
    }

    pending_changes = {}
    ssh_connections = {}

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file)
        self.configuration = Configuration()
        self.mechanism_drivers = \
            self.configuration.environment['mechanism_drivers']
        self.env = env
        self.monitoring_config = self.db.monitoring_config_templates
        self.env_monitoring_config = self.configuration.get('Monitoring')
        self.local_host = self.env_monitoring_config['server_ip']
        self.replacements = self.env_monitoring_config
        self.inv = InventoryMgr()
        self.config_db = self.db[self.inv.get_coll_name('monitoring_config')]
        self.provision = self.provision_levels['none']
        if self.env_monitoring_config:
            provision = self.env_monitoring_config.get('provision', 'none')
            provision = str.lower(provision)
            self.provision =\
                self.provision_levels.get(provision,
                                          self.provision_levels['none'])

    # create a directory if it does not exist
    @staticmethod
    def make_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    def get_config_dir(self, sub_dir=''):
        config_folder = self.env_monitoring_config['config_folder'] + \
            ('/' + sub_dir if sub_dir else '')
        return self.make_directory(config_folder).rstrip('/')

    def prepare_config_file(self, file_type, base_condition):
        condition = base_condition
        condition['type'] = file_type
        sort = [('order', pymongo.ASCENDING)]
        docs = self.monitoring_config.find(condition, sort=sort)
        content = {}
        for doc in docs:
            if self.check_env_condition(doc):
                content.update(doc)
        self.replacements['app_path'] = \
            self.configuration.environment['app_path']
        config = self.content_replace({'config': content['config']})
        return config

    def check_env_condition(self, doc):
        if 'condition' not in doc:
            return True
        condition = doc['condition']
        if 'mechanism_drivers' not in condition:
            return True
        return condition['mechanism_drivers'] in self.mechanism_drivers

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

    def write_config_file(self, file_name, sub_dir, host, content,
                          is_container=False):
        """
        apply environment definitions to the config,
        e.g. replace {server_ip} with the IP or host name for the server
        """
        # save the config to DB first, and while doing that
        # merge it with any existing config on same host
        content = self.merge_config(host, file_name, content)

        if self.provision == self.provision_levels['db']:
            self.log.debug('Monitoring setup kept only in DB')
            return
        # now dump the config to the file
        content_json = json.dumps(content['config'], sort_keys=True, indent=4)
        content_json += '\n'
        # always write the file locally first
        local_dir = self.make_directory(self.get_config_dir() + '/' +
                                        sub_dir.strip('/'))
        local_path = local_dir + '/' + file_name
        self.write_to_local_host(local_path, content_json)
        self.track_pending_host_setup_changes(host, is_container,
                                              file_name, local_path,
                                              sub_dir)

    def add_changes_for_all_clients(self):
        """
        to debug deployment, add simulated track changes entries.
        no need to add for server, as these are done by server_setup()
        """
        docs = self.config_db.find({'environment': self.env})
        for doc in docs:
            host = doc['host']
            sub_dir = '/host/' + host
            file_name = doc['type']
            local_path = self.env_monitoring_config['config_folder'] + \
                sub_dir + '/' + file_name
            if host == self.env_monitoring_config['server_ip']:
                continue
            doc = self.decode_mongo_keys(doc)
            self.track_pending_host_setup_changes(host, False, file_name,
                                                  local_path, sub_dir)

    def get_ssh(self, host, is_container=False):
        if host not in self.ssh_connections:
            if is_container:
                conf = self.env_monitoring_config
                host = conf['server_ip']
                port = int(conf['ssh_port'])
                user = conf['ssh_user']
                pwd = conf['ssh_password']
                ssh = SshConnection(host, user, _pwd=pwd, _port=port)
            else:
                ssh = SshConn(host)
            self.ssh_connections[host] = ssh
        return self.ssh_connections[host]

    def track_pending_host_setup_changes(self, host, is_container,
                                         file_name, local_path,
                                         sub_dir):
        if host not in self.pending_changes:
            self.pending_changes[host] = {}
        if file_name not in self.pending_changes[host]:
            self.pending_changes[host][file_name] = {
                "host": host,
                "is_container": is_container,
                "file_name": file_name,
                "local_path": local_path,
                "sub_dir": sub_dir
            }

    def handle_pending_setup_changes(self):
        if self.provision < self.provision_levels['files']:
            if self.provision == self.provision_levels['db']:
                self.log.info('Monitoring config applied only in DB')
            return
        self.log.info('applying monitoring setup')
        for host, host_changes in self.pending_changes.items():
            self.handle_pending_host_setup_changes(host_changes)
        self.log.info('done applying monitoring setup')

    def handle_pending_host_setup_changes(self, host_changes):
        hosts = {}
        if self.provision < self.provision_levels['deploy']:
            self.log.info('Monitoring config not deployed to remote host')
        for file_type, changes in host_changes.items():
            host = changes['host']
            is_container = changes['is_container']
            local_dir = changes['local_path']
            self.log.debug('applying monitoring setup changes ' +
                           'for host ' + host + ', file type: ' + file_type)
            is_local_host = host == self.local_host
            file_path = self.PRODUCTION_CONFIG_DIR + '/' + file_type
            if host not in hosts:
                hosts[host] = {
                    'host': host,
                    'local_dir': local_dir,
                    'is_local_host': is_local_host,
                    'is_container': is_container
                }
            if is_container:
                self.write_to_container(changes['local_path'])
            elif is_local_host:
                    # write to production configuration directory on local host
                    self.make_directory(self.PRODUCTION_CONFIG_DIR)
                    shutil.copy(changes['local_path'], file_path)
            else:
                # write to remote host prepare dir - use sftp
                if self.provision < self.provision_levels['deploy']:
                    continue
                self.write_to_remote_host(host, changes['local_path'])
        if self.provision < self.provision_levels['deploy']:
            return
        for host in hosts.values():
            self.deploy_config_to_target(host)

    def deploy_config_to_target(self, host_details):
        host = host_details['host']
        is_local_host = host_details['is_local_host']
        is_container = host_details['is_container']
        local_dir = host_details['local_dir']
        if is_container or not is_local_host:
            # copy the files to remote target config directory
            self.make_remote_dir(host, self.PRODUCTION_CONFIG_DIR)
            local_dir = local_dir[:local_dir.rindex('/')]
            self.move_setup_files_to_remote_host(host, local_dir)
            # restart the Sensu client on the remote host,
            # so it takes the new setup
            self.run('sudo /etc/init.d/sensu-client restart',
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
        if self.provision < self.provision_levels['deploy']:
            self.log.info('Monitoring config not written to remote host')
            return
        monitor_server = self.env_monitoring_config['server_ip']
        if self.is_gateway_host(monitor_server) and host == monitor_server:
            # do a copy on the monitoring server host
            self.run('cp ' + local_dir + '/* ' + self.PRODUCTION_CONFIG_DIR,
                     enable_cache=False)
            return
        # need to scp the files from the gateway host to the target host
        ssh = self.get_ssh(host)
        remote_path = ssh.get_user() + '@' + host + ':' + \
            self.PRODUCTION_CONFIG_DIR + '/'
        self.make_remote_dir(host, self.PRODUCTION_CONFIG_DIR)
        self.run_on_gateway('scp ' + local_dir + '/client.json ' + remote_path,
                            enable_cache=False)

    def make_remote_dir_on_host(self, ssh, host, path, path_is_file=False):
        # make sure we have write permissions in target directories
        dir_path = path
        if path_is_file:
            dir_path = dir_path[:dir_path.rindex('/')]
        cmd = 'sudo mkdir -p ' + dir_path
        self.run(cmd, ssh_to_host=host, ssh=ssh)
        cmd = 'sudo chown -R ' + ssh.get_user() + ' ' + dir_path
        self.run(cmd, ssh_to_host=host, ssh=ssh)

    def make_remote_dir(self, host, path, path_is_file=False):
        ssh = self.get_ssh(host)
        self.make_remote_dir_on_host(ssh, host, path, path_is_file)

    def copy_to_remote_host(self, host, local_path, remote_path, mode=None):
        # copy the local file to the preparation folder for the remote host
        # on the gateway host
        ssh = self.get_ssh(host)
        gateway_host = ssh.host
        gateway_ssh = self.get_ssh(gateway_host)
        self.make_remote_dir(gateway_host, remote_path, path_is_file=True)
        gateway_ssh.copy_file(local_path, remote_path, mode)

    def write_to_remote_host(self, host, local_path):
        remote_path = local_path  # copy to config dir first
        self.copy_to_remote_host(host, local_path, remote_path)

    def write_to_container(self, local_path):
        host = self.env_monitoring_config['server_ip']
        ssh = self.get_ssh(host, is_container=True)
        self.make_remote_dir_on_host(ssh, host, local_path, True)
        ssh.copy_file(local_path, local_path)  # copy to config dir first

    @staticmethod
    def write_to_local_host(file_path, content):
        f = open(file_path, "w")
        f.write(content)
        f.close()
        return file_path
