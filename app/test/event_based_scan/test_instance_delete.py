from test.event_based_scan.test_data.event_payload_instance_delete import EVENT_PAYLOAD_INSTANCE_DELETE, \
    INSTANCE_DOCUMENT
from test.event_based_scan.test_event_delete_base import TestEventDeleteBase


class TestInstanceDelete(TestEventDeleteBase):

    def setUp(self):
        super().setUp()
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE
        self.set_item_for_deletion(object_type="instance", document=INSTANCE_DOCUMENT)

    def test_handle_instance_delete(self):
        self.handle_delete(handler=self.handler.instance_delete)
