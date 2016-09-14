import unittest
from discover.configuration import Configuration
from discover.event_handler import EventHandler
from test.get_args import GetArgs


test_json_instance_add = {'publisher_id': 'compute.node-6.cisco.com', '_context_resource_uuid': None,
                         '_context_instance_lock_checked': False,
                         '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                         '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
                         '_context_request_id': 'req-432fccc8-4d13-4e62-8639-c99acee82cb3',
                         '_context_show_deleted': False,
                         '_context_timestamp': '2016-09-08T22:01:41.724236',
                         '_unique_id': '537fc5b27c244479a69819a4a435723b',
                         '_context_roles': ['_member_', 'admin'], '_context_read_only': False,
                         '_context_user_id': '13baa553aae44adca6615e711fd2f6d9',
                         '_context_project_name': 'OSDNA-project',
                         '_context_project_domain': None, 'event_type': 'compute.instance.update',
                         '_context_service_catalog': [{'endpoints': [
                             {'internalURL': 'http://192.168.0.2:8776/v2/75c0eb79ff4a42b0ae4973c8375ddf40',
                              'publicURL': 'http://172.16.0.3:8776/v2/75c0eb79ff4a42b0ae4973c8375ddf40',
                              'adminURL': 'http://192.168.0.2:8776/v2/75c0eb79ff4a42b0ae4973c8375ddf40',
                              'region': 'RegionOne'}],
                             'type': 'volumev2',
                             'name': 'cinderv2'},
                             {'endpoints': [{
                                 'internalURL': 'http://192.168.0.2:8776/v1/75c0eb79ff4a42b0ae4973c8375ddf40',
                                 'publicURL': 'http://172.16.0.3:8776/v1/75c0eb79ff4a42b0ae4973c8375ddf40',
                                 'adminURL': 'http://192.168.0.2:8776/v1/75c0eb79ff4a42b0ae4973c8375ddf40',
                                 'region': 'RegionOne'}],
                                 'type': 'volume',
                                 'name': 'cinder'}],
                         'payload': {'instance_type': 'm1.micro', 'progress': '', 'display_name': 'test8',
                                     'kernel_id': '',
                                     'new_task_state': None, 'old_display_name': 'name-change', 'state_description': '',
                                     'old_state': 'building', 'ramdisk_id': '', 'created_at': '2016-09-08 16:32:46+00:00',
                                     'os_type': None,
                                     'ephemeral_gb': 0, 'launched_at': '2016-09-08T16:25:08.000000',
                                     'instance_flavor_id': 'f068e24b-5d7e-4819-b5ca-89a33834a918',
                                     'image_meta': {'min_ram': '64', 'container_format': 'bare', 'min_disk': '0',
                                                    'disk_format': 'qcow2',
                                                    'base_image_ref': 'c6f490c4-3656-43c6-8d03-b4e66bd249f9'},
                                     'audit_period_beginning': '2016-09-01T00:00:00.000000', 'memory_mb': 64,
                                     'cell_name': '',
                                     'access_ip_v6': None, 'instance_type_id': 6, 'reservation_id': 'r-bycutzve',
                                     'access_ip_v4': None,
                                     'hostname': 'chengli-test-vm1', 'metadata': {},
                                     'user_id': '13baa553aae44adca6615e711fd2f6d9',
                                     'availability_zone': 'osdna-zone',
                                     'instance_id': '27a87908-bc1b-45cc-9238-09ad1ae686a7', 'deleted_at': '',
                                     'image_ref_url': 'http://172.16.0.4:9292/images/c6f490c4-3656-43c6-8d03-b4e66bd249f9',
                                     'host': 'node-5.cisco.com', 'vcpus': 1, 'state': 'active', 'old_task_state': None,
                                     'architecture': None,
                                     'terminated_at': '', 'root_gb': 0, 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                                     'node': 'node-5.cisco.com', 'bandwidth': {}, 'disk_gb': 0,
                                     'audit_period_ending': '2016-09-08T22:01:43.165282'}, '_context_quota_class': None,
                         '_context_is_admin': True, '_context_read_deleted': 'no',
                         'timestamp': '2016-09-08 22:01:43.189907',
                         'message_id': '4a9068c6-dcd1-4d6c-81d7-db866e07c1ff', 'priority': 'INFO',
                         '_context_domain': None,
                         '_context_user': '13baa553aae44adca6615e711fd2f6d9',
                         '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
                         '_context_remote_address': '192.168.0.2', '_context_user_domain': None,
                         '_context_auth_token': '''gAAAAABX0d-R0Q4zIrznmZ_L8BT0m4r_lp-7eOr4IenbKz511g2maNo8qhIb86HtA7S
                         VGsEJvy4KRcNIGlVRdmGyXBYm3kEuakQXTsXLxvyQeTtgZ9UgnLLXhQvMLbA2gwaimVpyRljq92R7Y7CwnNFLjibhOiYs
                         NlvBqitJkaRaQa4sg4xCN2tBj32Re-jRu6dR_sIA-haT''',
                         '_context_user_name': 'admin'}


class TestInstanceAdd(unittest.TestCase):
    def setUp(self):
        self.arg_getter = GetArgs()
        self.args = self.arg_getter.get_args()

        self.conf = Configuration(self.args.mongo_config)
        self.conf.use_env(self.args.env)
        self.handler = EventHandler(self.args.env, self.args.inventory)
        self.values = test_json_instance_add

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
