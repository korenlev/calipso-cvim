from discover.events.event_delete_base import EventDeleteBase


class EventInstanceDelete(EventDeleteBase):

    def handle(self, env, values):
        # find the corresponding object
        instance_id = values['payload']['instance_id']
        return self.delete_handler(env, instance_id, "instance")
