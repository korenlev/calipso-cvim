# handle adding of monitoring setup as needed

from monitoring.setup.monitoring_handler import MonitoringHandler
from monitoring.setup.monitoring_host import MonitoringHost
from monitoring.setup.monitoring_otep import MonitoringOtep
from monitoring.setup.monitoring_link_vnic_vconnector \
    import MonitoringLinkVnicVconnector


class MonitoringSetupManager(MonitoringHandler):

    object_handlers = None

    def __init__(self, mongo_conf_file, env):
        conf_file = mongo_conf_file
        super().__init__(conf_file, env)
        self.object_handlers = {
            "host": MonitoringHost(conf_file, env),
            "otep": MonitoringOtep(conf_file, env),
            "vnic-vconnector": MonitoringLinkVnicVconnector(conf_file, env)}

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
        self.replacements.update(self.env_monitoring_config)
        for file_name in sensu_server_files:
            content = self.prepare_config_file(file_name, {'side': 'server'})
            full_path = directory + '/' + file_name
            self.write_config_file(file_name, full_path, server_host, content)
        self.config.update_env({'monitoring_setup_done': True})

    # add setup for inventory object
    def create_setup(self, o):
        type_attribute = 'type' if 'type' in o else 'link_type'
        type_value = o[type_attribute]
        if type_value in self.object_handlers.keys():
            object_handler = self.object_handlers[type_value]
            object_handler.create_setup(o)
