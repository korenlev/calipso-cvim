import unittest

import re

from discover.configuration import Configuration
from test.event_based_scan.config.test_config import DEFAULT_METADATA_FILE, \
    MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger
from utils.util import MetadataParser


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.log = Logger().log
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)

        metadata_parser = MetadataParser()
        metadata_parser.parse_metadata_file(DEFAULT_METADATA_FILE)
        self.inv = InventoryMgr()
        self.inv.set_collections(self.collection)
        self.item_ids = []

    def set_item(self, document):
        self.inv.set(document)
        self.item_ids.append(document['id'])

    def assert_empty_by_id(self, object_id):
        doc = self.inv.get_by_id(self.env, object_id)
        self.assertIsNone(doc)

    def tearDown(self):
        for item_id in self.item_ids:
            item = self.inv.get_by_id(self.env, item_id)
            # delete children
            if item:
                regexp = re.compile('^' + item['id_path'])
                self.inv.delete('inventory', {'id_path': {'$regex': regexp}})

            # delete target item
            self.inv.delete('inventory', {'id': item_id})
            item = self.inv.get_by_id(self.env, item_id)
            self.assertIsNone(item)
