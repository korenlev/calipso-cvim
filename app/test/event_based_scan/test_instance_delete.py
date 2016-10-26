from bson import ObjectId

from test.event_based_scan.test_data.event_payload_instance_delete import EVENT_PAYLOAD_INSTANCE_DELETE, INSTANCE_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestInstanceDelete(TestEvent):

    def test_handle_instance_delete(self):
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE
        self.handle_delete(self.handler.instance_delete, self.values, "instance", document=INSTANCE_DOCUMENT)
