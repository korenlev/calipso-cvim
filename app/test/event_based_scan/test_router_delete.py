from test.event_based_scan.test_data.event_payload_router_delete import EVENT_PAYLOAD_ROUTER_DELETE, ROUTER_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestRouterDelete(TestEvent):

    def test_handle_router_delete(self):
        self.values = EVENT_PAYLOAD_ROUTER_DELETE
        self.handle_delete(self.handler.router_delete, self.values, "router", document=ROUTER_DOCUMENT)
