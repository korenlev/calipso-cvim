from discover.events.event_delete_base import EventDeleteBase
from discover.inventory_mgr import InventoryMgr


class EventInstanceDelete(EventDeleteBase):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        # find the corresponding object
        id = values['instance_id']
        self.delete_handler(env, id, "instance")
