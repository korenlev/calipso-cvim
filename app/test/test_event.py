import unittest

from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.get_args import GetArgs


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.arg_getter = GetArgs()
        self.args = self.arg_getter.get_args()

        self.conf = Configuration(self.args.mongo_config)
        self.conf.use_env(self.args.env)
        self.handler = EventHandler(self.args.env, self.args.inventory)
