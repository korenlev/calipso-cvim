import unittest

import re

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.event_based_scan.config.test_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.handler = EventHandler(ENV_CONFIG, self.collection)
        self.item_ids = []

    def set_item(self, document):
        self.handler.inv.set(document)
        self.item_ids.append(document['id'])

    def assert_empty_by_id(self, object_id):
        doc = self.handler.inv.get_by_id(self.env, object_id)
        self.assertIsNone(doc)

    def tearDown(self):
        for item_id in self.item_ids:
            item = self.handler.inv.get_by_id(self.env, item_id)
            # delete children
            if item:
                regexp = re.compile('^' + item['id_path'])
                self.handler.inv.delete('inventory', {'id_path': {'$regex': regexp}})

            # delete target item
            self.handler.inv.delete('inventory', {'id': item_id})
            item = self.handler.inv.get_by_id(self.env, item_id)
            self.assertIsNone(item)
