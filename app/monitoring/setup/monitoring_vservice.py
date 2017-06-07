from monitoring.setup.monitoring_simple_object import MonitoringSimpleObject


class MonitoringVservice(MonitoringSimpleObject):

    def __init__(self, env):
        super().__init__(env)

    def create_setup(self, o):
        self.setup('vservice', o)
