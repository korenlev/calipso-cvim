from unittest.mock import MagicMock
from discover.api_access import ApiAccess
from discover.events.event_subnet_add import EventSubnetAdd
from discover.find_links_for_pnics import FindLinksForPnics
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from test.event_based_scan.test_data.event_payload_subnet_add import EVENT_PAYLOAD_SUBNET_ADD,\
    EVENT_PAYLOAD_REGION, NETWORK_DOC
from test.event_based_scan.test_event import TestEvent


class TestSubnetAdd(TestEvent):

    def test_handle_subnet_add(self):
        self.values = EVENT_PAYLOAD_SUBNET_ADD
        self.payload = self.values['payload']
        self.subnet = self.payload['subnet']
        self.subnet_id = self.subnet['id']
        self.network_id = self.subnet['network_id']
        self.item_ids.append(self.network_id)

        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        if network_document:
            # check subnet in network first.
            self.assertNotIn(self.subnet['cidr'], network_document['cidrs'])
        else:
            self.handler.log.info("network document is not found, add it first.")
            self.set_item(NETWORK_DOC)
            # check network document
            network_document = self.handler.inv.get_by_id(self.env, self.network_id)
            self.assertNotEqual(network_document, [])

        # check region data.
        if len(ApiAccess.regions) == 0:
            ApiAccess.regions = EVENT_PAYLOAD_REGION

        # Mock function instead of get children data. They should be test in their unit test.
        # add subnet document for updating network
        handler = EventSubnetAdd()
        handler.add_children_documents = MagicMock()

        original_add_pnic_links = FindLinksForPnics.add_links
        FindLinksForPnics.add_links = MagicMock()

        original_add_vservice_links = FindLinksForVserviceVnics.add_links
        FindLinksForVserviceVnics.add_links = MagicMock()

        handler.handle(self.env, self.values)

        # reset the methods back
        FindLinksForPnics.add_links = original_add_pnic_links
        FindLinksForVserviceVnics.add_links = original_add_vservice_links

        # check network document
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertIn(self.subnet['cidr'], network_document['cidrs'])
        self.assertIn(self.subnet['name'], network_document['subnets'])

        #tearDown method has been implemented in class testEvent.
