from test.test_data.event_payload_instance_add import EVENT_PAYLOAD_INSTANCE_ADD
from test.test_event import TestEvent


class TestInstanceAdd(TestEvent):

    def test_handle_instance_add(self):
        self.values = EVENT_PAYLOAD_INSTANCE_ADD
        payload = self.values['payload']
        _id = payload['instance_id']
        host_id = payload['host']

        # check instance document
        instance = self.handler.inv.get_by_id(self.env, _id)
        if instance:
            self.handler.log.info('instance document has existed, delete it first.')
            self.handler.instance_delete(payload)

        # add instance into database
        self.handler.instance_add(payload)

        # check instance document
        instance = self.handler.inv.get_by_id(self.env, _id)
        self.assertNotEqual(instance, [])

        # check host document
        host = self.handler.inv.get_by_id(self.env, host_id)
        self.assertNotEqual(host, [])

        # Delete the document after test.
        self.handler.instance_delete(payload)
