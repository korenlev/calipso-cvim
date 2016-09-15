import unittest
from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.get_args import GetArgs
from test.test_data.event_payload_instance_update import EVENT_PAYLOAD_INSTANCE_UPDATE


class TestInstanceUpdate(unittest.TestCase):
    def setUp(self):
        self.arg_getter = GetArgs()
        self.args = self.arg_getter.get_args()

        self.conf = Configuration(self.args.mongo_config)
        self.conf.use_env(self.args.env)
        self.handler = EventHandler(self.args.env, self.args.inventory)
        self.values = EVENT_PAYLOAD_INSTANCE_UPDATE

    def test_handle_normal_situation(self):
        payload = self.values['payload']
        id = payload['instance_id']
        new_name = payload['display_name']

        # get instance document
        instance = self.handler.inv.get_by_id(self.args.env, id)
        name_path = instance['name_path']
        new_name_path = name_path[:name_path.rindex('/') + 1] + new_name

        # update instance document
        self.handler.instance_update(self.values)

        # get new document
        instance = self.handler.inv.get_by_id(self.args.env, id)

        # check update result.
        self.assertEqual(instance['name'], new_name)
        self.assertEqual(instance['name_path'], new_name_path)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestInstanceUpdate)
    runner.run(itersuite)
