from unittest.mock import MagicMock

from discover.events.event_port_add import EventPortAdd
from discover.find_links_for_instance_vnics import FindLinksForInstanceVnics
from discover.find_links_for_vedges import FindLinksForVedges
from discover.scan_instances_root import ScanInstancesRoot
from discover.api_fetch_host_instances import ApiFetchHostInstances
from discover.cli_fetch_instance_vnics import CliFetchInstanceVnics
from test.event_based_scan.test_data.event_payload_port_add import EVENT_PAYLOAD_PORT_INSTANCE_ADD, NETWORK_DOC, \
    INSTANCE_DOC, INSTANCES_ROOT, VNIC_DOCS, INSTANCE_DOCS
from test.event_based_scan.test_event import TestEvent


class TestPortAdd(TestEvent):
    def test_handle_port_add(self):
        self.values = EVENT_PAYLOAD_PORT_INSTANCE_ADD
        self.payload = self.values['payload']
        self.port = self.payload['port']
        self.port_id = self.port['id']
        self.item_ids.append(self.port_id)

        # prepare data for test
        self.set_item(NETWORK_DOC)
        self.set_item(INSTANCE_DOC)
        self.set_item(INSTANCES_ROOT)
        self.item_ids.append(VNIC_DOCS[0]['id'])

        # mock methods
        original_get_instance = ApiFetchHostInstances.get
        ApiFetchHostInstances.get = MagicMock(return_value=INSTANCE_DOCS)

        original_get_vnic = CliFetchInstanceVnics.get
        CliFetchInstanceVnics.get = MagicMock(return_value=VNIC_DOCS)

        original_find_link_instance = FindLinksForInstanceVnics.add_links
        original_find_link_vedge = FindLinksForVedges.add_links
        orginal_scan = ScanInstancesRoot.scan_cliques

        FindLinksForInstanceVnics.add_links = MagicMock(return_value=None)
        FindLinksForVedges.add_links = MagicMock(return_value=None)
        ScanInstancesRoot.scan_cliques = MagicMock(return_value=None)

        # add network document
        EventPortAdd().handle(self.env, self.values)

        # check network document
        port_document = self.inv.get_by_id(self.env, self.port_id)
        self.assertIsNotNone(port_document)
        self.assertEqual(port_document["name"], self.port['name'])

        instance = self.inv.get_by_id(self.env, INSTANCE_DOC['id'])
        self.assertEqual(instance["network_info"][0]['devname'], INSTANCE_DOCS[0]["network_info"][0]['devname'])
        self.assertEqual(instance["network_info"], INSTANCE_DOCS[0]["network_info"])
        self.assertEqual(instance["network"], INSTANCE_DOCS[0]["network"])

        vnic = self.inv.get_by_field(self.env, 'vnic', 'mac_address', self.port['mac_address'])
        self.assertIsNotNone(vnic)

        FindLinksForVedges.add_links = original_find_link_vedge
        FindLinksForInstanceVnics.add_links = original_find_link_instance
        ScanInstancesRoot.scan_cliques = orginal_scan
        CliFetchInstanceVnics.get = original_get_vnic
        ApiFetchHostInstances.get = original_get_instance
