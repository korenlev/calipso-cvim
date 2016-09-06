import re

from events.event_instance_add import EventInstanceAdd
from events.event_instance_delete import EventInstanceDelete
from events.event_instance_update import EventInstanceUpdate
from fetcher import Fetcher
from inventory_mgr import InventoryMgr


class EventHandler(Fetcher):
    def __init__(self, env, inventory_collection):
        super().__init__()
        self.inv = InventoryMgr()
        self.inv.set_inventory_collection(inventory_collection)
        self.env = env

    def instance_add(self, vals):
        self.log.info("instance_add")
        handler = EventInstanceAdd()
        handler.handle(self.env, vals)

    def instance_delete(self, vals):
        self.log.info("instance_delete")
        handler = EventInstanceDelete()
        handler.handle(self.env, vals)

    def instance_update(self, vals):
        self.log.info("instance_update")
        handler = EventInstanceUpdate()
        handler.handle(self.env, vals)

    def instance_down(self, notification):
        pass

    def instance_up(self, notification):
        pass

    def region_add(self, notification):
        pass

    def region_delete(self, notification):
        pass

    def region_update(self, notification):
        pass
