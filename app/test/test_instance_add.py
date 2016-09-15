import unittest
from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.get_args import GetArgs
from test.test_data.event_payload_instance_add import EVENT_PAYLOAD_INSTANCE_ADD


class TestInstanceAdd(unittest.TestCase):
    def setUp(self):
        self.arg_getter = GetArgs()
        self.args = self.arg_getter.get_args()

        self.conf = Configuration(self.args.mongo_config)
        self.conf.use_env(self.args.env)
        self.handler = EventHandler(self.args.env, self.args.inventory)
        self.values = EVENT_PAYLOAD_INSTANCE_ADD

    def test_handle_instance_add(self):
        payload = self.values['payload']
        _id = payload['instance_id']
        host_id = payload['host']

        # add instance into database
        self.handler.instance_add(payload)

        # check instance document
        instance = self.handler.inv.get_by_id(self.args.env, _id)
        self.assertIsNot(instance, [])

        # check host document
        host = self.handler.inv.get_by_id(self.args.env, host_id)
        self.assertIsNot(host, [])


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestInstanceAdd)
    runner.run(itersuite)
