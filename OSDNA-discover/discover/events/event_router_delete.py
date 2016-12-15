from discover.events.event_delete_base import EventDeleteBase
from discover.inventory_mgr import InventoryMgr


class EventRouterDelete(EventDeleteBase):
    def __init__(self):
        super(EventDeleteBase).__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        router_id = 'qrouter-' + notification['payload']['router_id']
        self.delete_handler(env, router_id, "vservice")
