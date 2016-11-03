from unittest.mock import MagicMock

from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_port_add import EventPortAdd
from discover.events.event_router_add import EventRouterAdd
from discover.events.event_subnet_add import EventSubnetAdd
from test.event_based_scan.test_data.event_payload_router_add import EVENT_PAYLOAD_ROUTER_ADD, ROUTER_DOCUMENT, \
    HOST_DOC, NETWORK_DOC
from test.event_based_scan.test_event import TestEvent


class TestRouterAdd(TestEvent):
    def test_handle_router_add(self):
        self.values = EVENT_PAYLOAD_ROUTER_ADD
        self.payload = self.values['payload']
        self.router = self.payload['router']
        self.router_id = "qrouter-"+self.router['id']
        self.handler.inv.set(HOST_DOC)
        self.host_id = HOST_DOC['id']
        gateway_info = self.router['external_gateway_info']
        if gateway_info:
            self.network_id = self.router['external_gateway_info']['network_id']
            self.handler.inv.set(NETWORK_DOC)

        handler = EventRouterAdd()
        CliFetchHostVservice.get_vservice = MagicMock(return_value=ROUTER_DOCUMENT)
        EventSubnetAdd.add_port_document = MagicMock()
        EventPortAdd.add_vnic_document = MagicMock()
        handler.update_links_and_cliques = MagicMock()

        handler.handle(self.env, self.values)
        self.gw_port_id = ROUTER_DOCUMENT['gw_port_id']

        # assert router document
        router_doc = self.handler.inv.get_by_id(self.env, self.router_id)
        self.assertNotEqual(router_doc, [], "router_doc not found.")
        self.assertEqual(ROUTER_DOCUMENT['name'], router_doc['name'])
        self.assertEqual(ROUTER_DOCUMENT['gw_port_id'], router_doc['gw_port_id'])

        # assert children documents
        vnics_folder = self.handler.inv.get_by_id(self.env, self.router_id+'-vnics')
        self.assertNotEqual(vnics_folder, [], "Vnics folder not found.")

    def tearDown(self):
        # delete network document
        self.handler.inv.delete('inventory', {'id': self.network_id})
        item = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertEqual(item, [])

        # delete host document
        self.handler.inv.delete('inventory', {'id': self.host_id})
        item = self.handler.inv.get_by_id(self.env, self.host_id)
        self.assertEqual(item, [])

        # delete ports folder document
        self.handler.inv.delete('inventory', {'id': self.network_id+"-ports"})
        item = self.handler.inv.get_by_id(self.env, self.network_id+"-ports")
        self.assertEqual(item, [])

        # delete port document
        self.handler.inv.delete('inventory', {'id': self.gw_port_id})
        item = self.handler.inv.get_by_id(self.env, self.gw_port_id)
        self.assertEqual(item, [])

        # delete vnics folder document
        self.handler.inv.delete('inventory', {'id': self.router_id+'-vnics'})
        item = self.handler.inv.get_by_id(self.env, self.router_id+'-vnics')
        self.assertEqual(item, [])

        # delete vnics document
        self.handler.inv.delete('inventory', {'parent_id': self.router_id+'-vnics'})
        item = self.handler.inv.get_by_field(self.env, 'vnic', 'parent_id', self.router_id+'-vnics')
        self.assertEqual(item, [])

        # delete router document
        self.handler.inv.delete('inventory', {'id': self.router_id})
        item = self.handler.inv.get_by_id(self.env, self.router_id)
        self.assertEqual(item, [])

