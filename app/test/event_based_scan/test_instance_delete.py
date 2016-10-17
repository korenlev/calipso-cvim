from bson import ObjectId

from test.event_based_scan.test_data.event_payload_instance_delete import EVENT_PAYLOAD_INSTANCE_DELETE, INSTANCE_DOCUMENT
from test.event_based_scan.test_event import TestEvent


class TestInstanceDelete(TestEvent):

    def test_handle_instance_delete(self):
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE
        payload = self.values['payload']
        self.instance_id = payload['instance_id']
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        if not instance:
            self.handler.log.info('instance document is not found, add document for deleting.')

            # add instance document for deleting.
            self.handler.inv.set(INSTANCE_DOCUMENT)
            instance = self.handler.inv.get_by_id(self.env, self.instance_id)
            self.assertNotEqual(instance, [])

        db_id = ObjectId(instance['_id'])
        clique_finder = self.handler.inv.get_clique_finder()

        # delete instance
        self.handler.instance_delete(payload)

        # check instance delete result.
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        self.assertEqual(instance, [])

        # check links
        matched_links_source = clique_finder.find_links_by_source(db_id)
        matched_links_target = clique_finder.find_links_by_target(db_id)
        links_using_object = [l['_id'] for l in matched_links_source].extend([l['_id'] for l in matched_links_target])
        self.assertIs(links_using_object, None)

        # check children
        matched_children = self.handler.inv.get_children(self.env, None, self.instance_id)
        self.assertEqual(matched_children, [])

    # delete document in case failure of test.
    def tearDown(self):
        self.handler.inv.delete('inventory', {'id': self.instance_id})
        instance = self.handler.inv.get_by_id(self.env, self.instance_id)
        self.assertEqual(instance, [])
