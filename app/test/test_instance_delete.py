import unittest
from bson import ObjectId
from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.get_args import GetArgs
from test.test_data.event_payload_instance_delete import EVENT_PAYLOAD_INSTANCE_DELETE


class TestInstanceDelete(unittest.TestCase):
    def setUp(self):
        self.arg_getter = GetArgs()
        self.args = self.arg_getter.get_args()

        self.conf = Configuration(self.args.mongo_config)
        self.conf.use_env(self.args.env)
        self.handler = EventHandler(self.args.env, self.args.inventory)
        self.values = EVENT_PAYLOAD_INSTANCE_DELETE

    def test_handle_instance_delete(self):
        payload = self.values['payload']
        id = payload['instance_id']
        item = self.handler.inv.get_by_id(self.args.env, id)
        if not item:
            self.handler.log.info('instance document not found, aborting instance delete')
            return None

        db_id = ObjectId(item['_id'])
        clique_finder = self.handler.inv.get_clique_finder()

        # delete instance
        self.handler.instance_delete(payload)

        # check instance delete result.
        instance = self.handler.inv.get_by_id(self.args.env, id)
        self.assertEqual(instance, [])

        # check links
        links_using_object = []

        matched_links = clique_finder.find_links_by_source(db_id)
        for l in matched_links:
            links_using_object.append(l['_id'])

        matched_links = clique_finder.find_links_by_target(db_id)
        for l in matched_links:
            links_using_object.append(l['_id'])

        self.assertEqual(links_using_object, [])

        # check children
        matched_children = self.handler.inv.get_children(self.args.env, None, id)
        self.assertEqual(matched_children, [])


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestInstanceDelete)
    runner.run(itersuite)
