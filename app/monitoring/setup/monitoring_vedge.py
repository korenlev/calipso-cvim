from monitoring.setup.monitoring_check_handler import MonitoringCheckHandler


class MonitoringVedge(MonitoringCheckHandler):

    def __init__(self, mongo_conf_file, env):
        super().__init__(mongo_conf_file, env)

    # add monitoring setup for remote host
    def create_setup(self, o):
        values = {
            "objtype": "vedge",
            "objid": o['id']}
        self.create_monitoring_for_object(o, values)
