from discover.events.event_router_update import EventRouterUpdate
from test.event_based_scan.test_data.event_payload_router_update import EVENT_PAYLOAD_ROUTER_UPDATE, ROUTER_DOCUMENT, \
    EVENT_PAYLOAD_ROUTER_SET_GATEWAY, EVENT_PAYLOAD_ROUTER_DEL_GATEWAY
from test.event_based_scan.test_event import TestEvent


class TestRouterUpdate(TestEvent):
    def test_handle_router_add(self):
        for values in [EVENT_PAYLOAD_ROUTER_UPDATE, EVENT_PAYLOAD_ROUTER_SET_GATEWAY, EVENT_PAYLOAD_ROUTER_DEL_GATEWAY]:
            self.values = values
            self.payload = self.values['payload']
            self.router = self.payload['router']
            self.router_id = "qrouter-" + self.router['id']
            self.item_id = self.router_id

            # add document for testing
            self.handler.inv.set(ROUTER_DOCUMENT)

            handler = EventRouterUpdate()
            handler.handle(self.env, self.values)
            self.gw_port_id = ROUTER_DOCUMENT['gw_port_id']

            # assert router document
            router_doc = self.handler.inv.get_by_id(self.env, self.router_id)
            self.assertNotEqual(router_doc, [], "router_doc not found.")
            self.assertEqual(self.router['name'], router_doc['name'])
            self.assertEqual(self.router['admin_state_up'], router_doc['admin_state_up'])

            if self.router['external_gateway_info'] == None:
                self.assertEqual(router_doc['gw_port_id'], None)
                self.assertEqual(router_doc['network'], [])
            else:
                self.assertIn(self.router['external_gateway_info']['network_id'], router_doc['network'])
