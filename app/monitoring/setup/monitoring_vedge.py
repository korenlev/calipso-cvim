from monitoring.setup.monitoring_simple_object import MonitoringSimpleObject


class MonitoringVedge(MonitoringSimpleObject):

    def __init__(self, env):
        super().__init__(env)

    def create_setup(self, o):
        self.setup('vedge', o)
