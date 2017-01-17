import copy
from os import listdir
from os.path import isfile, join
import stat

from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringHost(MonitoringHandler):
    APP_SCRIPTS_FOLDER = 'monitoring/checks'
    REMOTE_SCRIPTS_FOLDER = '/etc/sensu/plugins'

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file, env)

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
        env_name = self.config.env_config['name']
        client_name = env_name + '-' + o['id']
        client_ip = o['ip_address'] if 'ip_address' in o else o['id']
        self.replacements.update(config)
        self.replacements.update({
            'server_ip': server_ip,
            'client_name': client_name,
            'client_ip': client_ip,
            'env_name': env_name
        })

        # make sure the remote directories are there
        # with the right permissions
        self.make_remote_dir(host_id, self.PRODUCTION_CONFIG_DIR)
        self.make_remote_dir(host_id, self.REMOTE_SCRIPTS_FOLDER)

        # copy configuration files
        for file_name in sensu_host_files:
            content = self.prepare_config_file(file_name, {'side': 'client'})
            self.write_config_file(file_name, file_name, sub_dir, host_id,
                                   content)
        # copy scripts to host
        scripts_dir = join(self.env_monitoring_config['app_path'],
                           self.APP_SCRIPTS_FOLDER)
        script_files = [f for f in listdir(scripts_dir)
                        if isfile(join(scripts_dir, f))]
        script_mode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | \
            stat.S_IROTH | stat.S_IXOTH
        for file_name in script_files:
            remote_path = join(self.REMOTE_SCRIPTS_FOLDER, file_name)
            local_path = join(scripts_dir, file_name)
            self.copy_to_remote_host(host_id, local_path, remote_path,
                                     mode=script_mode)

        # mark this environment as prepared
        self.config.update_env({'monitoring_setup_done': True})
