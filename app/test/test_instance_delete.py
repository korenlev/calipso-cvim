from bson import ObjectId
from test.test_data.event_payload_instance_delete import EVENT_PAYLOAD_INSTANCE_DELETE
from test.test_event import TestEvent


class TestInstanceDelete(TestEvent):

    def test_handle_instance_delete(self):
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE
        payload = self.values['payload']
        id = payload['instance_id']
        item = self.handler.inv.get_by_id(self.env, id)
        if not item:
            self.handler.log.info('instance document not found, aborting instance delete')
            return None

        db_id = ObjectId(item['_id'])
        clique_finder = self.handler.inv.get_clique_finder()

        # delete instance
        self.handler.instance_delete(payload)

        # check instance delete result.
        instance = self.handler.inv.get_by_id(self.env, id)
        self.assertEqual(instance, [])

        # check links
        matched_links_source = clique_finder.find_links_by_source(db_id)
        matched_links_target = clique_finder.find_links_by_target(db_id)
        links_using_object = [l['_id'] for l in matched_links_source].extend([l['_id'] for l in matched_links_target])
        self.assertIs(links_using_object, None)

        # check children
        matched_children = self.handler.inv.get_children(self.env, None, id)
        self.assertEqual(matched_children, [])
