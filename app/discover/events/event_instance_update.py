import re

from discover.events.event_instance_add import EventInstanceAdd
from discover.events.event_instance_delete import EventInstanceDelete
from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventInstanceUpdate(Fetcher):
    def __init__(self):
        super(EventInstanceUpdate, self).__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        # find the host, to serve as parent
        payload = values['payload']
        id = payload['instance_id']
        state = payload['state']
        old_state = payload['old_state']

        if state == 'building':
            return

        if state == 'active' and old_state == 'building':
            handler = EventInstanceAdd()
            handler.handle(env, payload)
            return

        if state == 'deleted' and old_state == 'active':
            handler = EventInstanceDelete()
            handler.handle(env, payload)
            return

        name = payload['display_name']
        instance = self.inv.get_by_id(env, id)
        if not instance:
            self.log.info('instance document not found, aborting instance update')
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
