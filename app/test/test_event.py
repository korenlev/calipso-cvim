import unittest

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.config.local_config import MONGODB_CONFIG, ENV_CONFIG, COLLECTION_CONFIG


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.collection = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.use_env(self.env)
        self.handler = EventHandler(ENV_CONFIG , self.collection)
