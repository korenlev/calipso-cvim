# handle adding of monitoring setup as needed

from monitoring.setup.monitoring_handler import MonitoringHandler
from monitoring.setup.monitoring_host import MonitoringHost
from monitoring.setup.monitoring_link_vnic_vconnector \
    import MonitoringLinkVnicVconnector
from monitoring.setup.monitoring_otep import MonitoringOtep
from monitoring.setup.monitoring_vedge import MonitoringVedge
from monitoring.setup.monitoring_vnic import MonitoringVnic
from monitoring.setup.monitoring_pnic import MonitoringPnic


class MonitoringSetupManager(MonitoringHandler):

    object_handlers = None

    def __init__(self, env):
        super().__init__(env)
        self.object_handlers = {
            "host": MonitoringHost(env),
            "otep": MonitoringOtep(env),
            "vedge": MonitoringVedge(env),
            "pnic": MonitoringPnic(env),
            "vnic": MonitoringVnic(env),
            "vnic-vconnector": MonitoringLinkVnicVconnector(env)}

    # add monitoring setup to Sensu server
    def server_setup(self):
        if self.provision == self.provision_levels['none']:
            self.log.debug('Monitoring config setup skipped')
            return
        sensu_server_files = [
            'transport.json',
            'client.json',
            'rabbitmq.json',
            'handlers.json',
            'redis.json',
            'api.json'
        ]
        conf = self.env_monitoring_config
        is_container = bool(conf.get('ssh_user', ''))
        server_host = conf['server_ip']
        sub_dir = 'server'
        self.replacements.update(conf)
        for file_name in sensu_server_files:
            content = self.prepare_config_file(file_name, {'side': 'server'})
            self.write_config_file(file_name, sub_dir, server_host, content,
                                   is_container=is_container, is_server=True)
        self.configuration.update_env({'monitoring_setup_done': True})

    # add setup for inventory object
    def create_setup(self, o):
        if self.provision == self.provision_levels['none']:
            self.log.debug('Monitoring config setup skipped')
            return
        type_attribute = 'type' if 'type' in o else 'link_type'
        type_value = o[type_attribute]
        if type_value in self.object_handlers.keys():
            object_handler = self.object_handlers[type_value]
            object_handler.create_setup(o)

    def simulate_track_changes(self):
        self.add_changes_for_all_clients()
