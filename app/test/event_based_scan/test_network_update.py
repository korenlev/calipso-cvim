from test.event_based_scan.test_data.event_payload_network_update import EVENT_PAYLOAD_NETWORK_UPDATE, \
    EVENT_PAYLOAD_NETWORK_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestNetworkUpdate(TestEvent):

    def test_handle_network_update(self):
        self.values = EVENT_PAYLOAD_NETWORK_UPDATE
        self.payload = self.values['payload']
        self.network = self.payload['network']
        self.network_id = self.network['id']
        self.item_id = self.network_id

        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        if len(network_document) == 0:
            # set document for testing update.
            self.handler.inv.set(EVENT_PAYLOAD_NETWORK_DOCUMENT)

        name = self.network['name']
        status = self.network['admin_state_up']
        self.handler.network_update(self.values)
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertEqual(network_document['name'], name)
        self.assertEqual(network_document['admin_state_up'], status)
