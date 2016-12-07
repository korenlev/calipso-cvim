from monitoring.setup.monitoring_handler import MonitoringHandler


class MonitoringCheckHandler(MonitoringHandler):

    def __init__(self, mongo_conf_file):
        super().__init__(mongo_conf_file)

    # add monitoring setup on remote host for given object
    def create_monitoring_for_object(self, o, config):
        config.update(self.env_monitoring_config)
        config_folder = self.env_monitoring_config['config_folder']
        type = 'client_check_' + o['type'] + '.json'
        host = o['host']
        directory = self.make_directory(config_folder + '/host/' + host)
        content = self.prepare_config_file(
            type,
            {'side': 'client', 'type': type},
            config)
        full_path = directory + '/' + type
        self.write_file(full_path, host, content)
