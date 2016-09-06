import re

from events.event_instance_add import EventInstanceAdd
from events.event_instance_delete import EventInstanceDelete
from fetcher import Fetcher
from inventory_mgr import InventoryMgr


class EventInstanceUpdate(Fetcher):
    def __init__(self):
        super(EventInstanceUpdate, self).__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        # find the host, to serve as parent
        values = values['payload']
        id = values['instance_id']
        state = values['state']
        old_state = values['old_state']

        if state == 'building':
            return

        if state == 'active' and old_state == 'building':
            handler = EventInstanceAdd()
            handler.handle(env, values)
            return

        if state == 'deleted' and old_state == 'active':
            handler = EventInstanceDelete()
            handler.handle(env, values)
            return

        name = values['display_name']
        instance = self.inv.get_by_id(env, id)
        if not instance:
            return
        instance['name'] = name
        instance['object_name'] = name
        name_path = instance['name_path']
        instance['name_path'] = name_path[:name_path.rindex('/') + 1] + name

        # TBD: fix name_path for descendants
        if (name_path != instance['name_path']):
            self.inv.values_replace({
                "environment": env,
                "name_path": {"$regex": r"^" + re.escape(name_path + '/')}},
                {"name_path": {"from": name_path, "to": instance['name_path']}})
        self.inv.set(instance)
