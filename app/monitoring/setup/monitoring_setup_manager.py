# handle adding of monitoring setup as needed

from monitoring.setup.monitoring_handler import MonitoringHandler
from monitoring.setup.monitoring_host import MonitoringHost
from monitoring.setup.monitoring_otep import MonitoringOtep


class MonitoringSetupManager(MonitoringHandler):

    object_handlers = None

    def __init__(self, mongo_conf_file):
        super().__init__(mongo_conf_file)
        self.object_handlers = {
            "host": MonitoringHost(mongo_conf_file),
            "otep": MonitoringOtep(mongo_conf_file)}

    # add monitoring setup to Sensu server
    def server_setup(self):
        sensu_server_files = [
            'transport.json',
            'client.json',
            'rabbitmq.json',
            'handlers.json',
            'redis.json',
            'api.json'
        ]
        if 'monitoring_setup_done' in self.config.env_config:
            return
        server_host = self.env_monitoring_config['server_ip']
        config_folder = self.env_monitoring_config['config_folder']
        directory = self.make_directory(config_folder + '/server/')
        for file_name in sensu_server_files:
            content = self.prepare_config_file(
                file_name,
                {'side': 'server'},
                self.env_monitoring_config)
            full_path = directory + '/' + file_name
            self.write_file(full_path, server_host, content)
        self.config.update_env({'monitoring_setup_done': True})

    # add setup for inventory object
    def create_setup(self, o):
        if o['type'] in self.object_handlers.keys():
            object_handler = self.object_handlers[o['type']]
            object_handler.create_setup(o)
