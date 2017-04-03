from test.event_based_scan.test_data.event_payload_network_delete import EVENT_PAYLOAD_NETWORK_DELETE, \
    EVENT_PAYLOAD_NETWORK
from test.event_based_scan.test_event_delete_base import TestEventDeleteBase


class TestNetworkDelete(TestEventDeleteBase):

    def setUp(self):
        super().setUp()
        self.values = EVENT_PAYLOAD_NETWORK_DELETE
        self.set_item_for_deletion(object_type="network", document=EVENT_PAYLOAD_NETWORK)

    def test_handle_network_delete(self):
        self.handle_delete(self.handler.network_delete)
