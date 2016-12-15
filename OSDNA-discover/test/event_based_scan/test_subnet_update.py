from discover.api_access import ApiAccess
from discover.events.event_subnet_update import EventSubnetUpdate
from test.event_based_scan.test_data.event_payload_subnet_add import  \
    EVENT_PAYLOAD_REGION
from test.event_based_scan.test_data.event_payload_subnet_update import EVENT_PAYLOAD_SUBNET_UPDATE, NETWORK_DOC
from test.event_based_scan.test_event import TestEvent


class TestSubnetUpdate(TestEvent):

    def test_handle_subnet_add(self):
        self.values = EVENT_PAYLOAD_SUBNET_UPDATE
        self.payload = self.values['payload']
        self.subnet = self.payload['subnet']
        self.subnet_id = self.subnet['id']
        self.network_id = self.subnet['network_id']
        self.item_ids.append(self.network_id)

        #add network document for subnet.
        self.set_item(NETWORK_DOC)

        # check network document
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertNotEqual(network_document, [])

        # check region data.
        if len(ApiAccess.regions) == 0:
            ApiAccess.regions = EVENT_PAYLOAD_REGION

        handler = EventSubnetUpdate()
        handler.handle(self.env, self.values)

        # check network document
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertIn(self.subnet['name'], network_document['subnets'])
        self.assertEqual(self.subnet['gateway_ip'], network_document['subnets'][self.subnet['name']]['gateway_ip'])
