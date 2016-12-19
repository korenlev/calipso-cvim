from discover.api_access import ApiAccess
from test.event_based_scan.test_data.event_payload_interface_delete import EVENT_PAYLOAD_INTERFACE_DELETE, NETWORK_DOC, \
    EVENT_PAYLOAD_REGION, PORT_DOC, ROUTER_DOCUMENT, HOST, VNIC_DOCS
from test.event_based_scan.test_event import TestEvent


class TestInterfaceDelete(TestEvent):
    def test_handle_interface_delete(self):
        self.values = EVENT_PAYLOAD_INTERFACE_DELETE
        self.payload = self.values['payload']
        self.interface = self.payload['router_interface']

        self.port_id = self.interface['port_id']
        self.router_id = 'qrouter-' + self.interface['id']

        # set document for instance deleting.
        self.set_item(NETWORK_DOC)
        self.set_item(PORT_DOC)
        self.set_item(ROUTER_DOCUMENT)
        self.set_item(HOST)
        self.set_item(VNIC_DOCS[0])
        ApiAccess.regions = EVENT_PAYLOAD_REGION

        # delete interface
        self.handler.router_interface_delete(self.values)

        # assert data
        router_doc = self.handler.inv.get_by_id(self.env, ROUTER_DOCUMENT['id'])
        self.assertNotIn(NETWORK_DOC['id'], router_doc['network'])

        self.assert_empty_by_id(PORT_DOC['id'])
        self.assert_empty_by_id(VNIC_DOCS[0]['id'])
