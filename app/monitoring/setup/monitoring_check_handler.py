from discover.inventory_mgr import InventoryMgr
from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringCheckHandler(MonitoringHandler):

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file, env)
        self.inv = InventoryMgr()

    # add monitoring setup on remote host for given object
    def create_monitoring_for_object(self, o, config):
        if 'host' in o:
            host = self.inv.get_by_id(self.env, o['host'])
            if host and 'ip_address' in host:
                self.replacements['client_ip'] = host['ip_address']
        config.update(self.env_monitoring_config)
        config_folder = self.env_monitoring_config['config_folder']
        file_type = 'client_check_' + o['type'] + '.json'
        host = o['host']
        directory = self.make_directory(config_folder + '/host/' + host)
        content = self.prepare_config_file(
            'client.json',
            {'side': 'client', 'type': file_type},
            config)
        full_path = directory + '/' + file_type
        self.write_config_file(full_path, 'client.json', host, content)
