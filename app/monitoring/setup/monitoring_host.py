import copy

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
        sub_dir = '/host/' + host_id
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
        for file_name in sensu_host_files:
            content = self.prepare_config_file(file_name, {'side': 'client'})
            self.write_config_file(file_name, file_name, sub_dir, host_id,
                                   content)
        self.config.update_env({'monitoring_setup_done': True})
