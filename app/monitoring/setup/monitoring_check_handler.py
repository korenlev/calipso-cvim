from discover.inventory_mgr import InventoryMgr
from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringCheckHandler(MonitoringHandler):

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file, env)
        self.inv = InventoryMgr()

    # add monitoring setup on remote host for given object
    def create_monitoring_for_object(self, o, values):
        self.replacements.update(self.env_monitoring_config)
        self.replacements.update(values)
        if 'host' in o:
            host = self.inv.get_by_id(self.env, o['host'])
            if host and 'ip_address' in host:
                self.replacements['client_ip'] = host['ip_address']
        config_folder = self.env_monitoring_config['config_folder']
        file_type = 'client_check_' + o['type'] + '.json'
        host = o['host']
        directory = self.make_directory(config_folder + '/host/' + host)
        content = self.prepare_config_file(
            file_type,
            {'side': 'client', 'type': file_type})
        # need to put this content inside client.json file
        client_file = 'client.json'
        host = o['host']
        client_file_content = self.get_config_from_db(host, client_file)
        # merge checks attribute from current content into client.json
        checks = client_file_content['config']['checks'] \
            if 'checks' in client_file_content['config'] \
            else {}
        checks.update(content['config']['checks'])
        client_file_content['config']['checks'] = checks
        content = client_file_content
        full_path = directory + '/' + client_file
        self.write_config_file(client_file, full_path, host, content)
