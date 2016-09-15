import unittest
from test.test_data.event_payload_instance_add import EVENT_PAYLOAD_INSTANCE_ADD
from test.test_event import TestEvent


class TestInstanceAdd(TestEvent):

    def test_handle_instance_add(self):
        self.values = EVENT_PAYLOAD_INSTANCE_ADD
        payload = self.values['payload']
        _id = payload['instance_id']
        host_id = payload['host']

        # check instance document
        instance = self.handler.inv.get_by_id(self.args.env, _id)
        self.assertEqual(instance, [])

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
