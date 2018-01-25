from discover.events.event_base import EventBase


class KubeEventBase(EventBase):

    def __init__(self):
        super().__init__()
        self.object = None
        self.metadata = None

    def handle(self, env, values):
        self.object = values['object']
        self.metadata = self.object.metadata