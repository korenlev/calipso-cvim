from test.test_data.event_payload_instance_add \
  import EVENT_PAYLOAD_INSTANCE_ADD, INSTANCES_ROOT
from test.test_event import TestEvent


class TestInstanceAdd(TestEvent):

    def test_handle_instance_add(self):
        self.values = EVENT_PAYLOAD_INSTANCE_ADD
        payload = self.values['payload']
        self.instance_id = payload['instance_id']
        host_id = payload['host']

        # prepare instances root, in case it's not there
        self.handler.inv.set(INSTANCES_ROOT)

        # check instance document
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        if instance:
            self.handler.log.info('instance document has existed, delete it first.')
            self.handler.inv.delete('inventory', {'id': self.instance_id})

            instance = self.handler.inv.get_by_id(self.env, self.instance_id)
            self.assertEqual(instance, [])

        # add instance into database
        self.handler.instance_add(payload)

        # check instance document
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        self.assertNotEqual(instance, [])

        # check host document
        host = self.handler.inv.get_by_id(self.env, host_id)
        self.assertNotEqual(host, [])

    # Delete the document after test.
    def tearDown(self):
        self.handler.inv.delete('inventory', {'id': self.instance_id})
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        self.assertEqual(instance, [])

        self.handler.inv.delete('inventory', {'id': INSTANCES_ROOT['id']})
        root = self.handler.inv.get_by_id(self.env, INSTANCES_ROOT['id'])
        self.assertEqual(root, [])
