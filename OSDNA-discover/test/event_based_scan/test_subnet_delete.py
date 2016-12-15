from test.event_based_scan.test_event import TestEvent
from test.event_based_scan.test_data.event_payload_subnet_delete import EVENT_PAYLOAD_SUBNET_DELETE, \
    EVENT_PAYLOAD_NETWORK


class TestSubnetDelete(TestEvent):

    def test_handle_subnet_delete(self):
        self.values = EVENT_PAYLOAD_SUBNET_DELETE
        self.subnet_id = self.values['payload']['subnet_id']
        self.network_doc = EVENT_PAYLOAD_NETWORK
        self.network_id = self.network_doc['id']
        self.item_ids.append(self.network_id)

        self.subnet_name = None
        self.cidr = None

        for subnet in self.network_doc['subnets'].values():
            if subnet['id'] == self.subnet_id:
                self.subnet_name = subnet['name']
                self.cidr = subnet['cidr']
                break

        # add document for subnet deleting test.
        self.set_item(self.network_doc)
        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertNotEqual(network_document, [], "add network document failed")

        # delete subnet
        self.handler.subnet_delete(self.values)

        network_document = self.handler.inv.get_by_id(self.env, self.network_id)
        self.assertNotIn(self.subnet_id, network_document['subnet_ids'])
        self.assertNotIn(self.cidr, network_document['cidrs'])
        self.assertNotIn(self.subnet_name, network_document['subnets'])

        # assert children documents
        vservice_dhcp_id = 'qdhcp-' + network_document['id']
        dhcp_doc = self.handler.inv.get_by_id(self.env, vservice_dhcp_id)
        self.assertEqual(dhcp_doc,[])

        vnic_parent_id = vservice_dhcp_id + '-vnics'
        vnic = self.handler.inv.get_by_field(self.env, 'vnic', 'parent_id', vnic_parent_id, get_single=True)
        self.assertEqual(vnic, [])
