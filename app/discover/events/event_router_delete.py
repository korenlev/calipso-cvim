from discover.events.event_delete_base import EventDeleteBase


class EventRouterDelete(EventDeleteBase):

    def handle(self, env, notification):
        router_id = 'qrouter-' + notification['payload']['router_id']
        self.delete_handler(env, router_id, "vservice")
