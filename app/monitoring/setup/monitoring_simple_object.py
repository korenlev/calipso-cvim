from monitoring.setup.monitoring_check_handler import MonitoringCheckHandler


class MonitoringSimpleObject(MonitoringCheckHandler):

    def __init__(self, env):
        super().__init__(env)

    # add monitoring setup for remote host
    def setup(self, type: str, o: dict, values: dict = None):
        if not values:
            values = {}
        values['objtype'] = type
        values['objid'] = self.encode_special_characters(o['id'])
        self.create_monitoring_for_object(o, values)
