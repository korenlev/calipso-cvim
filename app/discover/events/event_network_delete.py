from discover.events.constants import NETWORK_OBJECT_TYPE
from discover.events.event_delete_base import EventDeleteBase


class EventNetworkDelete(EventDeleteBase):

    OBJECT_TYPE = NETWORK_OBJECT_TYPE

    def handle(self, env, notification):
        network_id = notification['payload']['network_id']
        return self.delete_handler(env, network_id, "network")
