
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
        'router': {'id': '0ecbc349-a928-47e2-ab49-86a27df6be7f', 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                   'ha': False, 'distributed': False, 'name': 'abc', 'status': 'ACTIVE', 'external_gateway_info': None,
                   'admin_state_up': True, 'routes': []}}, '_context_resource_uuid': None,
    'event_type': 'router.update.end', '_context_project_name': 'OSDNA-project', 'priority': 'INFO',
    '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_roles': ['_member_', 'admin'],
    '_context_project_domain': None, '_context_user_domain': None, '_context_read_only': False,
    '_context_is_admin': True, '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_domain': None,
    '_context_show_deleted': False, '_context_tenant_name': 'OSDNA-project', 'publisher_id': 'network.node-6.cisco.com',
    'timestamp': '2016-10-28 20:29:39.986161'}


EVENT_PAYLOAD_ROUTER_SET_GATEWAY = {
    'publisher_id': 'network.node-6.cisco.com',
    '_context_request_id': 'req-79d53b65-47b8-46b2-9a72-3f4031e2d605',
    '_context_project_name': 'OSDNA-project', '_context_show_deleted': False,
    '_context_user_name': 'admin', '_context_timestamp': '2016-11-02 21:44:31.156447',
    '_context_user': '13baa553aae44adca6615e711fd2f6d9', 'payload': {
        'router': {'id': '7d086d81-9bd4-4839-bec3-97f6e8051b61', 'admin_state_up': True, 'routes': [],
                   'status': 'ACTIVE', 'ha': False, 'name': 'test_namespace', 'distributed': False,
                   'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'external_gateway_info': {'external_fixed_ips': [
                {'ip_address': '172.16.0.144', 'subnet_id': 'a5336853-cbc0-49e8-8401-a093e8bab7bb'}],
                'network_id': 'c64adb76-ad9d-4605-9f5e-bd6dbe325cfb',
                'enable_snat': True}}},
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_context_read_only': False,
    '_context_auth_token': 'gAAAAABYGlU6mEqntx5E9Nss203DIKH352JKSZP0RsJrAJQ_PfjyZEAzYcFvMh4FYVRDRWLvu0cSDsvUk1ILu'+
                           'nHkpNF28pwcvkBgVModV2Xd2_BW2QbBa2csCOXYiN0LE2uOo3BkrLDEcblvJVT0XTJdDhrBldfyCH0_xSfJ7_'+
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
