from test.event_based_scan.test_data.event_payload_port_update import EVENT_PAYLOAD_PORT_UPDATE, PORT_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestPortUpdate(TestEvent):

    def test_handle_port_update(self):
        self.values = EVENT_PAYLOAD_PORT_UPDATE
        self.payload = self.values['payload']
        self.port = self.payload['port']
        self.port_id = self.port['id']
        self.item_id = self.port_id

        # set port data firstly.
        self.handler.inv.set(PORT_DOCUMENT)

        # add network document
        self.handler.port_update(self.values)

        # check network document
        port_document = self.handler.inv.get_by_id(self.env, self.port_id)
        self.assertNotEqual(port_document, [])
        self.assertEqual(port_document["name"], self.port['name'])
        self.assertEqual(port_document['admin_state_up'], self.port['admin_state_up'])
        self.assertEqual(port_document['binding:vnic_type'], self.port['binding:vnic_type'])
