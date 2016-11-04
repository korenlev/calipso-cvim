network_agent_list_type = 'firewall'

network_agent_false_list_type = 'firewall1'

inventory = 'inventory'

links='links'

clique_types = 'clique_types'

constraints ='constraints'

mongo_table = 'inventory'

mongo_table_false = 'xxxxx'

mongo_access_encode = 'test.inventory'

mongo_access_decode = 'test[dot]inventory'

mongo_access_key_encode = {'host.':'10.81.83.237','user':'root','pwd':'Lilies09!'}

mongo_access_key_decode = {'host[dot]': '10.81.83.237', 'user': 'root', 'pwd': 'Lilies09!'}

folder_fetcher_types_name = 'regions'

folder_fetcher_parent_type = 'evnironment'

folder_fetcher_id = '12345'

util_class_name = 'InventoryMgr'

util_jsonify = { "name": 'xxxxxx', }

env = 'WebEX-Mirantis@Cisco'

env_wrong = 'dummyenv'

ssh_conn = {'host': '10.81.85.108','user':'root','pwd':'Lilies09!'}
ssh_host_name = None

ssh_cmd = 'ls'

ssh_cmd_false= 'ls1'

logger_level = 'INFO'


dummy_value = 'xxxxx'

dummy_list=[]

conf_component = 'OpenStack'

config_name = 'OVS'

event_handler ={
        
         'host': 'node-24',
         'instance_id': '1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071',
         'environment': 'WebEX-Mirantis@Cisco',
         'payload': {'state_description': 'deleting', 'access_ip_v4': None, 'launched_at': '2016-09-12T22:00:42.000000', 'cell_name': '', 'progress': '', 'ramdisk_id': '', 'state': 'active', 'hostname': 'update-test1', 'terminated_at': '', 'audit_period_ending': '2016-10-04T23:36:38.918329', 'memory_mb': 64, 'availability_zone': None, 'vcpus': 1, 'root_gb': 0, 'instance_type_id': 6, 'new_task_state': 'deleting', 'os_type': None, 'kernel_id': '', 'image_meta': {'min_ram': '64', 'disk_format': 'qcow2', 'min_disk': '0', 'container_format': 'bare', 'base_image_ref': 'c6f490c4-3656-43c6-8d03-b4e66bd249f9'}, 'old_state': 'active', 'access_ip_v6': None, 'instance_id': 'a8374aad-1524-4db4-a2cd-45fa8c793f70', 'old_task_state': 'deleting', 'deleted_at': '', 'bandwidth': {}, 'host': 'node-5.cisco.com', 'node': 'node-5.cisco.com', 'instance_type': 'm1.micro', 'image_ref_url': 'http://172.16.0.4:9292/images/c6f490c4-3656-43c6-8d03-b4e66bd249f9', 'disk_gb': 0, 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'audit_period_beginning': '2016-10-01T00:00:00.000000', 'ephemeral_gb': 0, 'metadata': {}, 'created_at': '2016-09-12 22:08:17+00:00', 'user_id': '13baa553aae44adca6615e711fd2f6d9', 'display_name': 'update-test6', 'instance_flavor_id': 'f068e24b-5d7e-4819-b5ca-89a33834a918', 'reservation_id': 'r-2gx8fd3m', 'architecture': None},
    }

dummy_dict = {}

event_listener_coll = 'inventory'

dummy_db_id ='57c56c194a0a8a3fbe3bb7c0'

NONE =None

handle_type ='compute.instance.update'

event_listener_body = {'event_type':'compute.instance.update'}

EMPTY = ''

inventory_dummy_id = '329e0576da594c62a911d0dccb1238a7'

inventory_type = 'projects_folder'

clique_constraints =[ {
    "focal_point_type" : "instance",
    "focal_point" : "instance",
    "constraints" : [
        "network"
    ]
}]

clique_clique_type = 'instance'

inventory_items={

    "environment" : "WebEX-Mirantis@Cisco",
    "id" : "WebEX-Mirantis@Cisco-regions",
    "type" : "regions_folder",
    "name" : "Regions",
    "parent_type" : "environment",
    "text" : "Regions",
    "parent_id" : "WebEX-Mirantis@Cisco",

    "id_path" : "/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions",
    "object_name" : "Regions",
    "name_path" : "/WebEX-Mirantis@Cisco/Regions"
},

inv_base_url =  {'_id': '5808ad576d91c0e76b44c6c7', 'id': '1d3c8aad-0e78-49ba-a3bd-055ad5aee15b', 'network_id': '3efdf3ed-0bb5-4539-b1d5-4ed72d86c4dd'}


inv_create = {'env' : 'WebEX-Mirantis@Cisco',
    'host':'WebEX-Mirantis@Cisco', 'src':'57c54f4e4a0a8a3fbe3bb4a0', 'source_id':'5808ad566d91c0e76b44c6bc', 'target':'5808ad566d91c0e76b44c6bc', 'target_id':'080145e2-ccef-4946-b6ce-be633c88669e',
                    'link_type':'pnic-network', 'link_name':'Segment-1001', 'state':'up', 'link_weight':0,
                    'source_label':"", 'target_label':"",'extra_attributes':{}
            }

clique_finder_link = {'attributes':'test'}

clique_finder_link_not_attributes = {'attributes':'test'}

inv_delete_coll ='links'
inv_del_filter = {'type':'vnic1'}

inv_clear_value = {'object_type': 'Environment', 'obj': {'id': 'WebEX-Mirantis@Cisco'}, 'module_file': 'scan_environment', 'object_id': 'WebEX-Mirantis@Cisco',\
                    'scan_self': False, 'parent_id': '', 'inventory_only': False, 'id_field': 'id', 'scanner_class': 'ScanEnvironment', 'type_to_scan': '', \
                    'loglevel': 'INFO', 'child_type': None, 'cliques_only': False, 'clear': True, 'child_id': None, 'links_only': False, 'env': 'WebEX-Mirantis@Cisco', 'cgi': False}


inv_process_result =  [{'_id': '57c54f4a4a0a8a3fbe3bb438', 'type': 'project', 'parent_id': None}]

inv_base_urls = '/osdna_dev/discover.py?type=tree&id=329e0576da594c62a911d0dccb1238a7'

inv_get_by_field = [{'children_url': '/osdna_dev/discover.py?type=tree&id=329e0576da594c62a911d0dccb1238a7', 'type': 'project', '_id': '57c54f4a4a0a8a3fbe3bb438', 'parent_id': None}]

inv_check_filed = 'type'

inv_find_inv = [{'environment': 'Devstack-VPP-2', 'name': 'Projects', 'id_path': '/Devstack-VPP-2/Devstack-VPP-2-projects', 'id': 'Devstack-VPP-2-projects', 'show_in_tree': True, 'object_name': 'Projects', 'parent_type': 'environment', 'create_object': True, 'parent_id': 'Devstack-VPP-2', 'name_path': '/Devstack-VPP-2/Projects', 'text': 'Projects', '_id': '57c54fac4a0a8a3fbe3bb53e', 'type': 'projects_folder'}]

clique_types_find = [{'environment': 'Devstack-VPP-2', 'name': 'Projects', 'id_path': '/Devstack-VPP-2/Devstack-VPP-2-projects', 'id': 'Devstack-VPP-2-projects', 'show_in_tree': True, 'object_name': 'Projects', 'parent_type': 'environment', 'create_object': True, 'parent_id': 'Devstack-VPP-2', 'name_path': '/Devstack-VPP-2/Projects', 'text': 'Projects', '_id': '57c54fac4a0a8a3fbe3bb53e', 'type': 'projects_folder'}]

inv_finds_inv = [{'name': 'Projects', '_id': '57c54fac4a0a8a3fbe3bb53e', 'name_path': '/Devstack-VPP-2/Projects', 'id': 'Devstack-VPP-2-projects', 'parent_id': 'Devstack-VPP-2', 'text': 'Projects', 'object_name': 'Projects', 'parent_type': 'environment', 'environment': 'Devstack-VPP-2', 'show_in_tree': True, 'type': 'projects_folder', 'create_object': True, 'id_path': '/Devstack-VPP-2/Devstack-VPP-2-projects'}]

inv_set= {'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-projects', 'environment': 'WebEX-Mirantis@Cisco', 'show_in_tree': True, 'type': 'projects_folder', 'name_path': '/WebEX-Mirantis@Cisco/Projects', 'create_object': True, 'id': 'WebEX-Mirantis@Cisco-projects_muruga', 'text': 'Projects', 'name': 'Projects', 'parent_id': 'WebEX-Mirantis@Cisco', 'parent_type': 'environment'}

clique_finder_find =  [{'environment': 'Devstack-VPP-2', 'name': 'Projects', 'id_path': '/Devstack-VPP-2/Devstack-VPP-2-projects', 'id': 'Devstack-VPP-2-projects', 'show_in_tree': True, 'object_name': 'Projects', 'parent_type': 'environment', 'create_object': True, 'parent_id': 'Devstack-VPP-2', 'name_path': '/Devstack-VPP-2/Projects', 'text': 'Projects', '_id': '57c54fac4a0a8a3fbe3bb53e', 'type': 'projects_folder'}]

EVENT_PAYLOAD_INSTANCE_ADD = {
    'publisher_id': 'compute.node-6.cisco.com', '_context_resource_uuid': None,
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
              'new_task_state': None, 'old_display_name': 'name-change',
              'state_description': '',
              'old_state': 'building', 'ramdisk_id': '',
              'created_at': '2016-09-08 16:32:46+00:00',
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
              'host': 'node-5.cisco.com', 'vcpus': 1, 'state': 'active',
              'old_task_state': None,
              'architecture': None,
              'terminated_at': '', 'root_gb': 0,
              'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
              'node': 'node-5.cisco.com', 'bandwidth': {}, 'disk_gb': 0,
              'audit_period_ending': '2016-09-08T22:01:43.165282'},
    '_context_quota_class': None,
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

event_handler_get_by_id = {'type': 'project', 'children_url': {'network_id': '3efdf3ed-0bb5-4539-b1d5-4ed72d86c4dd', 'id': '1d3c8aad-0e78-49ba-a3bd-055ad5aee15b', '_id': '5808ad576d91c0e76b44c6c7'}, '_id': '57c54f4a4a0a8a3fbe3bb438', 'parent_id': None}

conf_find_env = [{'scanned': True, 'configuration': [{'port': 3306.0, 'password': 'BsfYNGxi', 'host': '10.56.20.83', 'name': 'mysql', 'schema': 'nova', 'user': 'root'}, {'port': '5000', 'host': '10.56.20.83', 'name': 'OpenStack', 'pwd': 'admin', 'user': 'admin', 'admin_token': 'vIhNb1l2'}, {'name': 'CLI', 'pwd': '', 'key': '/home/yarony/.ssh/id_rsa', 'host': '10.56.20.83', 'user': 'root'}, {'name': 'orchestrator', 'key': 'my-oauth', 'user': 'NFV-admin', 'host': '10.56.20.71'}, {'name': 'MQ', 'pwd': 'btE6JPF9', 'host': '10.56.20.83', 'user': 'nova'}], '_id': '5713e12008c1c518a0ac01ab', 'distribution': 'Mirantis-6.0', 'last_scanned:': '10/1/16', 'name': 'WebEX-Mirantis@Cisco', 'operational': 'yes', 'network_plugins': ['OVS'], 'type': 'environment'}]

conf_find_more_env = [{'scanned': True, 'configuration': [{'port': 3306.0, 'password': 'BsfYNGxi', 'host': '10.56.20.83', 'name': 'mysql', 'schema': 'nova', 'user': 'root'}, {'port': '5000', 'host': '10.56.20.83', 'name': 'OpenStack', 'pwd': 'admin', 'user': 'admin', 'admin_token': 'vIhNb1l2'}, {'name': 'CLI', 'pwd': '', 'key': '/home/yarony/.ssh/id_rsa', 'host': '10.56.20.83', 'user': 'root'}, {'name': 'orchestrator', 'key': 'my-oauth', 'user': 'NFV-admin', 'host': '10.56.20.71'}, {'name': 'MQ', 'pwd': 'btE6JPF9', 'host': '10.56.20.83', 'user': 'nova'}], '_id': '5713e12008c1c518a0ac01ab', 'distribution': 'Mirantis-6.0', 'last_scanned:': '10/1/16', 'name': 'WebEX-Mirantis@Cisco', 'operational': 'yes', 'network_plugins': ['OVS'], 'type': 'environment'},{'scanned': True, 'configuration': [{'port': 3306.0, 'password': 'BsfYNGxi', 'host': '10.56.20.83', 'name': 'mysql', 'schema': 'nova', 'user': 'root'}, {'port': '5000', 'host': '10.56.20.83', 'name': 'OpenStack', 'pwd': 'admin', 'user': 'admin', 'admin_token': 'vIhNb1l2'}, {'name': 'CLI', 'pwd': '', 'key': '/home/yarony/.ssh/id_rsa', 'host': '10.56.20.83', 'user': 'root'}, {'name': 'orchestrator', 'key': 'my-oauth', 'user': 'NFV-admin', 'host': '10.56.20.71'}, {'name': 'MQ', 'pwd': 'btE6JPF9', 'host': '10.56.20.83', 'user': 'nova'}], '_id': '5713e12008c1c518a0ac01ab', 'distribution': 'Mirantis-6.0', 'last_scanned:': '10/1/16', 'name': 'WebEX-Mirantis@Cisco', 'operational': 'yes', 'network_plugins': ['OVS'], 'type': 'environment'}]

inv_coll_name = 'links'