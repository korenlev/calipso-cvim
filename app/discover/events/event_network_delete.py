from discover.events.event_delete_base import EventDeleteBase
from discover.inventory_mgr import InventoryMgr


class EventNetworkDelete(EventDeleteBase):
    def __init__(self):
        super(EventDeleteBase).__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        network_id = notification['payload']['network_id']
        self.delete_handler(env, network_id, "network")
