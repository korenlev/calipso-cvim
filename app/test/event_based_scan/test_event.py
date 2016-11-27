import unittest

from bson import ObjectId

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.event_based_scan.config.local_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.handler = EventHandler(ENV_CONFIG , self.collection)
        self.item_id = None

    def handle_delete(self, handler, values, type, document=[]):
        payload = values['payload']
        self.item_id = payload['%s_id' % type]
        if type == 'router':
            self.item_id = "q%s-%s" % (type, self.item_id)
        item = self.handler.inv.get_by_id(self.env, self.item_id)
        if not item:
            self.handler.log.info('%s document is not found, add document for deleting.' % type)

            # add network document for deleting.
            self.handler.inv.set(document)
            item = self.handler.inv.get_by_id(self.env, self.item_id)
            self.assertNotEqual(item, [])

        db_id = ObjectId(item['_id'])
        clique_finder = self.handler.inv.get_clique_finder()

        # delete item
        handler(values)

        # check instance delete result.
        item = self.handler.inv.get_by_id(self.env, self.item_id)
        self.assertEqual(item, [])

        # check links
        matched_links_source = clique_finder.find_links_by_source(db_id)
        matched_links_target = clique_finder.find_links_by_target(db_id)
        links_using_object = [l['_id'] for l in matched_links_source].extend([l['_id'] for l in matched_links_target])
        self.assertIs(links_using_object, None)

        # check children
        matched_children = self.handler.inv.get_children(self.env, None, self.item_id)
        self.assertEqual(matched_children, [])

    def tearDown(self):
        self.handler.inv.delete('inventory', {'id': self.item_id})
        item = self.handler.inv.get_by_id(self.env, self.item_id)
        self.assertEqual(item, [])
