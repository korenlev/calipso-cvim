from discover.events.event_delete_base import EventDeleteBase


class EventNetworkDelete(EventDeleteBase):

    def handle(self, env, notification):
        network_id = notification['payload']['network_id']
        self.delete_handler(env, network_id, "network")
