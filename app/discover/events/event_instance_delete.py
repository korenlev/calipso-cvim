from discover.events.event_delete_base import EventDeleteBase


class EventInstanceDelete(EventDeleteBase):

    def handle(self, env, values):
        # find the corresponding object
        id = values['payload']['instance_id']
        return self.delete_handler(env, id, "instance")
