from monitoring.setup.monitoring_check_handler import MonitoringCheckHandler


class MonitoringPnic(MonitoringCheckHandler):

    def __init__(self, env):
        super().__init__(env)

    # add monitoring setup for remote host
    def create_setup(self, o):
        values = {
            'objtype': 'pnic',
            'objid': self.encode_special_characters(o['id'])}
        self.create_monitoring_for_object(o, values)
