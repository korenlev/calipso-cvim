from typing import Callable

from bson import ObjectId

from discover.events.event_base import EventResult
from test.event_based_scan.test_event import TestEvent


class TestEventDeleteBase(TestEvent):

    def setUp(self):
        super().setUp()
        self.values = {}

    def set_item_for_deletion(self, object_type, document):

        payload = self.values['payload']
        self.item_id = payload['{}_id'.format(object_type)]
        if object_type == 'router':
            host_id = self.values['publisher_id'].replace("network.", "", 1)
            self.item_id = "-".join([host_id, "qrouter", self.item_id])

        self.assertEqual(document['id'], self.item_id, msg="Document id and payload id are different")

        item = self.handler.inv.get_by_id(self.env, self.item_id)
        if not item:
            self.handler.log.info('{} document is not found, add document for deleting.'.format(object_type))

            # add network document for deleting.
            self.set_item(document)
            item = self.handler.inv.get_by_id(self.env, self.item_id)
            self.assertIsNotNone(item)

    def handle_delete(self,
                      handler: Callable[[dict], EventResult]):

        item = self.handler.inv.get_by_id(self.env, self.item_id)
        db_id = ObjectId(item['_id'])
        clique_finder = self.handler.inv.get_clique_finder()

        # delete item
        event_result = handler(self.values)
        self.assertTrue(event_result.result)

        # check instance delete result.
        item = self.handler.inv.get_by_id(self.env, self.item_id)
        self.assertIsNone(item)

        # check links
        matched_links_source = clique_finder.find_links_by_source(db_id)
        matched_links_target = clique_finder.find_links_by_target(db_id)
        self.assertEqual(matched_links_source.count(), 0)
        self.assertEqual(matched_links_target.count(), 0)

        # check children
        matched_children = self.handler.inv.get_children(self.env, None, self.item_id)
        self.assertEqual(len(matched_children), 0)
