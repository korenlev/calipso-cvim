import copy
import os
from os.path import join, sep

from monitoring.setup.monitoring_handler import MonitoringHandler

RABBITMQ_CONFIG_FILE = 'rabbitmq.json'
RABBITMQ_CONFIG_ATTR = 'rabbitmq'

RABBITMQ_CERT_FILE_ATTR = 'cert_chain_file'
RABBITMQ_PK_FILE_ATTR = 'private_key_file'
TMP_FILES_DIR = '/tmp'


class MonitoringHost(MonitoringHandler):

    def __init__(self, env):
        super().__init__(env)

    # add monitoring setup for remote host
    def create_setup(self, o):
        sensu_host_files = [
            'transport.json',
            'rabbitmq.json',
            'client.json'
        ]
        server_ip = self.env_monitoring_config['server_ip']
        host_id = o['host']
        sub_dir = join('/host', host_id)
        config = copy.copy(self.env_monitoring_config)
        env_name = self.configuration.env_name
        client_name = env_name + '-' + o['id']
        client_ip = o['ip_address'] if 'ip_address' in o else o['id']
        self.replacements.update(config)
        self.replacements.update({
            'server_ip': server_ip,
            'client_name': client_name,
            'client_ip': client_ip,
            'env_name': env_name
        })

        # copy configuration files
        for file_name in sensu_host_files:
            content = self.prepare_config_file(file_name, {'side': 'client'})
            self.get_ssl_files(host_id, file_name, content)
            self.write_config_file(file_name, sub_dir, host_id, content)

        if self.provision < self.provision_levels['deploy']:
            return

        self.track_setup_changes(host_id, False, "", "scripts", None)

        # mark this environment as prepared
        self.configuration.update_env({'monitoring_setup_done': True})

    def get_ssl_files(self, host, file_type, content):
        if self.fetch_ssl_files:
            return  # already got names of SSL files
        if file_type != RABBITMQ_CONFIG_FILE:
            return
        if not isinstance(content, dict):
            self.log.warn('invalid content of {}'.format(RABBITMQ_CONFIG_FILE))
            return
        config = content['config']
        if not config:
            self.log.warn('invalid content of {}'.format(RABBITMQ_CONFIG_FILE))
            return
        if RABBITMQ_CONFIG_ATTR not in config:
            self.log.warn('invalid content of {}'.format(RABBITMQ_CONFIG_FILE))
            return
        ssl_conf = config.get(RABBITMQ_CONFIG_ATTR).get('ssl')
        if not ssl_conf:
            return  # SSL not used

        for path_attr in [RABBITMQ_CERT_FILE_ATTR, RABBITMQ_PK_FILE_ATTR]:
            path = ssl_conf.get(path_attr)
            if not path:
                self.log.error('missing SSL path {}'.format(path_attr))
                return
            # this configuration requires SSL
            # keep the path of the files for later use
            self.fetch_ssl_files.append(path)
