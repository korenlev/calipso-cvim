from test.event_based_scan.test_data.event_payload_network_add import EVENT_PAYLOAD_NETWORK_ADD
from test.test_event import TestEvent


class TestNetworkAdd(TestEvent):

    def test_handle_network_add(self):
        self.values = EVENT_PAYLOAD_NETWORK_ADD
        self.payload = self.values['payload']
        self.network = self.payload['network']
        self.network_id = self.network['id']

        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        if network_document:
            self.handler.log.info('network document existed already, deleting it first.')
            self.handler.inv.delete('inventory', {'id': self.network_id})

            network_document = self.handler.inv.get_by_id(self.env, self.network_id)
            self.assertEqual(network_document, [])

        # build network document for adding network
        project_name = self.values['_context_project_name']
        project_id = self.values['_context_project_id']
        parent_id = project_id + '-networks'
        network_name = self.network['name']

        # add network document
        self.handler.network_create(self.values)

        # check network document
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertNotEqual(network_document, [])
        self.assertEqual(network_document["project"], project_name)
        self.assertEqual(network_document["parent_id"], parent_id)
        self.assertEqual(network_document["name"], network_name)

    # Delete the document after test.
    def tearDown(self):
        self.handler.inv.delete('inventory', {'id': self.network_id})
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertEqual(network_document, [])
