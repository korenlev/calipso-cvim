from test.event_based_scan.test_data.event_payload_router_delete import EVENT_PAYLOAD_ROUTER_DELETE, ROUTER_DOCUMENT
from test.event_based_scan.test_event_delete_base import TestEventDeleteBase


class TestRouterDelete(TestEventDeleteBase):

    def setUp(self):
        super().setUp()
        self.values = EVENT_PAYLOAD_ROUTER_DELETE
        self.set_item_for_deletion(object_type="router", document=ROUTER_DOCUMENT)

    def test_handle_router_delete(self):
        self.handle_delete(self.handler.router_delete)
