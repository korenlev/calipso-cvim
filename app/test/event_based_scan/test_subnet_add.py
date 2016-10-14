from discover.api_access import ApiAccess
from test.event_based_scan.test_data.event_payload_subnet_add import EVENT_PAYLOAD_SUBNET_ADD, EVENT_PAYLOAD_NETWORK_ADD, \
    EVENT_PAYLOAD_REGION
from test.test_event import TestEvent


class TestSubnetAdd(TestEvent):

    def test_handle_subnet_add(self):
        self.values = EVENT_PAYLOAD_SUBNET_ADD
        self.network_notification = EVENT_PAYLOAD_NETWORK_ADD

        self.payload = self.values['payload']
        self.subnet = self.payload['subnet']
        self.subnet_id = self.subnet['id']
        self.network_id = self.subnet['network_id']

        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        if network_document:
            # check subnet in network first.
            self.assertNotIn(self.subnet['cidr'], network_document['cidrs'])
        else:
            self.handler.log.info("network document is not found, add it first.")
            self.handler.network_create(self.network_notification)
            # check network document
            network_document = self.handler.inv.get_by_id(self.env, self.network_id)
            self.assertNotEqual(network_document, [])

            # todo add port data to the OpenStack DB. To create dhcp namespace as well.

        # check region data.
        if len(ApiAccess.regions) == 0:
            ApiAccess.regions = EVENT_PAYLOAD_REGION

        # add subnet document for updating network
        self.handler.subnet_create(self.values)

        # check network document
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertIn(self.subnet['cidr'], network_document['cidrs'])
        self.assertIn(self.subnet['name'], network_document['subnets'])


    # Delete the document after test.
    def tearDown(self):
        self.handler.inv.delete('inventory', {'id': self.network_id})
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertEqual(network_document, [])
