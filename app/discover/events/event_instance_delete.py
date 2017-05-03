from discover.events.constants import INSTANCE_OBJECT_TYPE
from discover.events.event_delete_base import EventDeleteBase


class EventInstanceDelete(EventDeleteBase):

    OBJECT_TYPE = INSTANCE_OBJECT_TYPE

    def handle(self, env, values):
        # find the corresponding object
        instance_id = values['payload']['instance_id']
        return self.delete_handler(env, instance_id, "instance")
