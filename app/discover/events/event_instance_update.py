import re

from discover.events.constants import INSTANCE_OBJECT_TYPE
from discover.events.event_base import EventBase, EventResult
from discover.events.event_instance_add import EventInstanceAdd
from discover.events.event_instance_delete import EventInstanceDelete


class EventInstanceUpdate(EventBase):

    OBJECT_TYPE = INSTANCE_OBJECT_TYPE

    def handle(self, env, values):
        # find the host, to serve as parent
        payload = values['payload']
        instance_id = payload['instance_id']
        state = payload['state']
        old_state = payload['old_state']

        if state == 'building':
            return self.construct_event_result(result=False, retry=False, object_id=instance_id)

        if state == 'active' and old_state == 'building':
            return EventInstanceAdd().handle(env, values)

        if state == 'deleted' and old_state == 'active':
            return EventInstanceDelete().handle(env, values)

        name = payload['display_name']
        instance = self.inv.get_by_id(env, instance_id)
        if not instance:
            self.log.info('instance document not found, aborting instance update')
            return self.construct_event_result(result=False, retry=True, object_id=instance_id)

        instance['name'] = name
        instance['object_name'] = name
        name_path = instance['name_path']
        instance['name_path'] = name_path[:name_path.rindex('/') + 1] + name

        # TBD: fix name_path for descendants
        if name_path != instance['name_path']:
            self.inv.values_replace({
                "environment": env,
                "name_path": {"$regex": r"^" + re.escape(name_path + '/')}},
                {"name_path": {"from": name_path, "to": instance['name_path']}})
        self.inv.set(instance)
        return self.construct_event_result(result=True,
                                           object_id=instance_id,
                                           document_id=instance.get('_id'))
