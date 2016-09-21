import copy

from test.test_data.event_payload_instance_update import EVENT_PAYLOAD_INSTANCE_UPDATE
from test.test_event import TestEvent


class TestInstanceUpdate(TestEvent):

    def test_handle_normal_situation(self):
        self.values = EVENT_PAYLOAD_INSTANCE_UPDATE
        payload = self.values['payload']
        id = payload['instance_id']
        new_name = payload['display_name']

        # get instance document
        instance = self.handler.inv.get_by_id(self.env, id)
        if not instance:
            self.handler.log.info("instance document is not found, add document for updating")

            # build instance adding payload.
            add_payload = copy.deepcopy(payload)
            add_payload['old_state'] = 'building'
            add_payload['state'] = 'active'
            add_payload['display_name'] = 'test_update'

            self.handler.instance_add(add_payload)
            instance = self.handler.inv.get_by_id(self.env, id)

        name_path = instance['name_path']
        new_name_path = name_path[:name_path.rindex('/') + 1] + new_name

        # update instance document
        self.handler.instance_update(self.values)

        # get new document
        instance = self.handler.inv.get_by_id(self.env, id)

        # check update result.
        self.assertEqual(instance['name'], new_name)
        self.assertEqual(instance['name_path'], new_name_path)
