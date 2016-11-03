EVENT_PAYLOAD_ROUTER_UPDATE = {
    '_context_request_id': 'req-da45908c-0765-4f8a-9fac-79246901de41', '_unique_id': '80723cc09a4748c6b13214dcb867719e',
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_context_user': '13baa553aae44adca6615e711fd2f6d9',
    '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_context_auth_token': 'gAAAAABYE7T7789XjB_Nir9PykWTIpDNI0VhgtVQJNyGVImHnug2AVRX9e2JDcXe8F73eNmFepASsoCfqvZet9q' +
                           'N38vrX6GqzL89Quf6pQyLxgRorMv6RlScSCDBQzE8Hj5szSYi_a7F_O2Lr77omUiLi2R_Ludt25mcMiuaMgPkn' +
                           'J2bjoAyV_-eE_8CrSbdJ5Dk1MaCSq5K',
    '_context_user_name': 'admin',
    '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
    '_context_timestamp': '2016-10-28 20:29:35.548123', 'message_id': '42c0ca64-cea1-4c89-a059-72abf7990c40',
    'payload': {
        'router': {'id': 'bde87a5a-7968-4f3b-952c-e87681a96078', 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                   'ha': False, 'distributed': False, 'name': 'abc', 'status': 'ACTIVE', 'external_gateway_info': None,
                   'admin_state_up': True, 'routes': []}}, '_context_resource_uuid': None,
    'event_type': 'router.update.end', '_context_project_name': 'OSDNA-project', 'priority': 'INFO',
    '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_roles': ['_member_', 'admin'],
    '_context_project_domain': None, '_context_user_domain': None, '_context_read_only': False,
    '_context_is_admin': True, '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_domain': None,
    '_context_show_deleted': False, '_context_tenant_name': 'OSDNA-project', 'publisher_id': 'network.node-6.cisco.com',
    'timestamp': '2016-10-28 20:29:39.986161'}

ROUTER_VSERVICE = {'host': 'node-6.cisco.com', 'service_type': 'router', 'name': '1234',
                   'id': 'qrouter-bde87a5a-7968-4f3b-952c-e87681a96078',
                   'local_service_id': 'qrouter-bde87a5a-7968-4f3b-952c-e87681a96078',
                   'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'status': 'ACTIVE',
                   'master_parent_type': 'vservices_folder',
                   'admin_state_up': 1, 'parent_type': 'vservice_routers_folder', 'enable_snat': 1,
                   'parent_text': 'Gateways',
                   'gw_port_id': 'e2f31c24-d0f9-499e-a8b1-883941543aa4',
                   'master_parent_id': 'node-6.cisco.com-vservices',
                   'parent_id': 'node-6.cisco.com-vservices-routers'}

ROUTER_DOCUMENT = {
    "admin_state_up": True,
    "children_url": "/osdna_dev/discover.py?type=tree&id=qrouter-bde87a5a-7968-4f3b-952c-e87681a96078",
    "enable_snat": 1,
    "environment": "Mirantis-Liberty-CL",
    "gw_port_id": "e2f31c24-d0f9-499e-a8b1-883941543aa4",
    "host": "node-6.cisco.com",
    "id": "qrouter-bde87a5a-7968-4f3b-952c-e87681a96078",
    "id_path": "/Mirantis-Liberty-CL/Mirantis-Liberty-CL-regions/RegionOne/RegionOne-availability_zones/internal" +
               "/node-6.cisco.com/node-6.cisco.com-vservices/node-6.cisco.com-vservices-routers/qrouter-bde87a5a" +
               "-7968-4f3b-952c-e87681a96078",
    "last_scanned": 0,
    "local_service_id": "qrouter-bde87a5a-7968-4f3b-952c-e87681a96078",
    "master_parent_id": "node-6.cisco.com-vservices",
    "master_parent_type": "vservices_folder",
    "name": "1234",
    "name_path": "/Mirantis-Liberty-CL/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/" +
                 "Vservices/Gateways/router-1234",
    "network": [
        "c64adb76-ad9d-4605-9f5e-bd6dbe325cfb"
    ],
    "object_name": "router-1234",
    "parent_id": "node-6.cisco.com-vservices-routers",
    "parent_text": "Gateways",
    "parent_type": "vservice_routers_folder",
    "service_type": "router",
    "show_in_tree": True,
    "status": "ACTIVE",
    "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
    "type": "vservice"
}

EVENT_PAYLOAD_ROUTER_SET_GATEWAY = {
    'publisher_id': 'network.node-6.cisco.com',
    '_context_request_id': 'req-79d53b65-47b8-46b2-9a72-3f4031e2d605',
    '_context_project_name': 'OSDNA-project', '_context_show_deleted': False,
    '_context_user_name': 'admin', '_context_timestamp': '2016-11-02 21:44:31.156447',
    '_context_user': '13baa553aae44adca6615e711fd2f6d9', 'payload': {
        'router': {'id': 'bde87a5a-7968-4f3b-952c-e87681a96078', 'admin_state_up': True, 'routes': [],
                   'status': 'ACTIVE', 'ha': False, 'name': 'test_namespace', 'distributed': False,
                   'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'external_gateway_info': {'external_fixed_ips': [
                {'ip_address': '172.16.0.144', 'subnet_id': 'a5336853-cbc0-49e8-8401-a093e8bab7bb'}],
                'network_id': 'c64adb76-ad9d-4605-9f5e-bd6dbe325cfb',
                'enable_snat': True}}},
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_context_read_only': False,
    '_context_auth_token': 'gAAAAABYGlU6mEqntx5E9Nss203DIKH352JKSZP0RsJrAJQ_PfjyZEAzYcFvMh4FYVRDRWLvu0cSDsvUk1ILu' +
                           'nHkpNF28pwcvkBgVModV2Xd2_BW2QbBa2csCOXYiN0LE2uOo3BkrLDEcblvJVT0XTJdDhrBldfyCH0_xSfJ7_' +
                           'wzdy8bB34HwHq2w0S3Okp8Tk_Zx_-xpIqB',
    'priority': 'INFO', 'timestamp': '2016-11-02 21:44:35.627776',
    '_context_roles': ['_member_', 'admin'], '_context_resource_uuid': None,
    '_context_user_domain': None, '_context_project_domain': None,
    '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
    'message_id': '71889925-14ce-40c3-a3dc-f26731b10b26',
    'event_type': 'router.update.end',
    '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_unique_id': '9e6ab72c5901451f81748e0aa654ae25',
    '_context_tenant_name': 'OSDNA-project', '_context_is_admin': True,
    '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_domain': None}

EVENT_PAYLOAD_ROUTER_DEL_GATEWAY = {
    '_context_show_deleted': False, '_context_timestamp': '2016-11-03 18:48:40.420170', '_context_read_only': False,
    'publisher_id': 'network.node-6.cisco.com',
    '_context_auth_token': 'gAAAAABYG4UUGbe9bykUJUPY0lKye578aF0RrMCc7nA21eLbhpwcsh5pWWqz6hnOi7suUCUtr1DPTbqF1M8CVJ' +
                           '9FT2EevbqiahcyphrV2VbmP5_tebOcIHIPJ_f_K3KYJM1C6zgcWgdf9KFu_8t_G99wd1MwWBrZyUUElXgSNv48' +
                           'W4uaCKcbYclnZW78lgXVik5x6WLT_j5V',
    '_context_user_name': 'admin',
    '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
    '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_unique_id': '266f2bb0ab2c4a328ae0759d01b0035b',
    'timestamp': '2016-11-03 18:48:41.634214', '_context_roles': ['_member_', 'admin'],
    'event_type': 'router.update.end',
    '_context_user_domain': None, '_context_user': '13baa553aae44adca6615e711fd2f6d9', '_context_is_admin': True,
    '_context_tenant_name': 'OSDNA-project', '_context_project_domain': None, '_context_domain': None,
    'priority': 'INFO',
    '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'message_id': '5272cd90-7151-4d13-8c1f-e8ff2db773a1',
    '_context_project_name': 'OSDNA-project', '_context_resource_uuid': None, 'payload': {
        'router': {'id': 'bde87a5a-7968-4f3b-952c-e87681a96078', 'external_gateway_info': None, 'distributed': False,
                   'name': 'TEST_AAA', 'routes': [], 'ha': False, 'admin_state_up': True,
                   'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'status': 'ACTIVE'}},
    '_context_request_id': 'req-d7e73189-4709-4234-8b4c-fb6b4dc2017b'}
