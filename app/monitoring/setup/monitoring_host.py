import copy
from os.path import join

from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringHost(MonitoringHandler):

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
            self.write_config_file(file_name, sub_dir, host_id, content)

        if self.provision < self.provision_levels['deploy']:
            return

        self.track_setup_changes(host_id, False, "", "scripts", None)

        # mark this environment as prepared
        self.configuration.update_env({'monitoring_setup_done': True})
