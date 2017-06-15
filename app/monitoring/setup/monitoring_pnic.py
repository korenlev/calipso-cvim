from monitoring.setup.monitoring_simple_object import MonitoringSimpleObject


class MonitoringPnic(MonitoringSimpleObject):

    def __init__(self, env):
        super().__init__(env)

    # add monitoring setup for remote host
    def create_setup(self, o):
        self.setup('pnic', o)
