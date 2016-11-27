EVENT_PAYLOAD_PORT_INTERFACE_ADD = {
    '_context_project_name': 'OSDNA-project', '_context_timestamp': '2016-10-24 20:14:26.234774',
    '_context_is_admin': True, '_context_show_deleted': False, 'publisher_id': 'network.node-6.cisco.com',
    '_context_roles': ['_member_', 'admin'], '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_context_project_domain': None,
    '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_user_domain': None,
    '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'event_type': 'port.create.end',
    '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
    'timestamp': '2016-10-24 20:14:28.937765', '_context_read_only': False, '_context_resource_uuid': None,
    'message_id': '33102061-4ec3-461e-9e01-1b9a9d7185ab', 'payload': {
        'port': {'binding:vif_details': {}, 'binding:vif_type': 'unbound', 'allowed_address_pairs': [],
                 'dns_assignment': [
                     {'ip_address': '172.16.13.5', 'hostname': 'host-172-16-13-5',
                      'fqdn': 'host-172-16-13-5.openstacklocal.'}],
                 'device_id': '', 'network_id': '2e3b85f4-756c-49d9-b34c-f3db13212dbc',
                 'id': '18f029db-775d-462e-b877-55f98130f8c0', 'dns_name': '', 'binding:vnic_type': 'normal',
                 'binding:host_id': '', 'device_owner': '', 'binding:profile': {}, 'mac_address': 'fa:16:3e:1f:e1:74',
                 'name': '',
                 'fixed_ips': [{'ip_address': '172.16.13.5', 'subnet_id': '9a9c1848-ea23-4c5d-8c40-ae1def4c2de3'}],
                 'port_security_enabled': True, 'admin_state_up': True, 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                 'status': 'DOWN', 'security_groups': ['2dd5c169-1ff7-40e5-ad96-18924b6d23f1']}},
    '_context_user': '13baa553aae44adca6615e711fd2f6d9', '_unique_id': '4997ceb32d89405588ac9430f186de83',
    '_context_domain': None,
    '_context_auth_token': 'gAAAAABYDmmboPzjwNVOZHJ81_qQ72Qt0-rodeqwxDQ9k8S_ddPsgQtTVG9-UFy0n8INf1qbgsMz7K4wgm' +
                           'B_Gcsz_MuMs_3Y2nDanmUCyzpecdYioGBjWjVTV8KAC_J3ToRKDeMg2U75tZ0e55lpkwLLNkayX7GcGOaiX' +
                           'hS7ngGJW-qWKkbPTncg9AxSD6d0oiJzWe8lUPjv',
    '_context_request_id': 'req-d17797e7-dad8-4731-8664-b677b830bd63', '_context_tenant_name': 'OSDNA-project',
    '_context_user_name': 'admin', 'priority': 'INFO'}

EVENT_PAYLOAD_PORT_INSTANCE_ADD = {
    '_context_user_id': '73638a2687534f9794cd8057ba860637', 'payload': {
        'port': {'port_security_enabled': True, 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                 'binding:vif_type': 'ovs',
                 'mac_address': 'fa:16:3e:21:a3:e8',
                 'fixed_ips': [{'subnet_id': '9a9c1848-ea23-4c5d-8c40-ae1def4c2de3', 'ip_address': '172.16.13.6'}],
                 'security_groups': ['2dd5c169-1ff7-40e5-ad96-18924b6d23f1'], 'allowed_address_pairs': [],
                 'binding:host_id': 'node-5.cisco.com', 'dns_name': '', 'status': 'DOWN',
                 'id': 'cf6089f4-ecb7-4467-bdcc-b3a0a18f4569', 'binding:profile': {}, 'admin_state_up': True,
                 'device_owner': 'compute:osdna-zone', 'device_id': 'e1de7561-8fdd-478c-8e7d-56514a0778a6',
                 'network_id': '2e3b85f4-756c-49d9-b34c-f3db13212dbc', 'name': '',
                 'binding:vif_details': {'ovs_hybrid_plug': True, 'port_filter': True}, 'extra_dhcp_opts': [],
                 'binding:vnic_type': 'normal'}}, '_context_project_domain': None, 'event_type': 'port.create.end',
    'message_id': '2e0da8dc-6d2d-4bde-9e52-c43ec4687864', 'publisher_id': 'network.node-6.cisco.com',
    '_context_domain': None, '_context_tenant_name': 'services', '_context_tenant': 'a83c8b0d2df24170a7c54f09f824230e',
    '_context_project_name': 'services', '_context_user': '73638a2687534f9794cd8057ba860637',
    '_context_user_name': 'neutron', 'priority': 'INFO', '_context_timestamp': '2016-10-24 21:29:52.127098',
    '_context_read_only': False, '_context_roles': ['admin'], '_context_is_admin': True, '_context_show_deleted': False,
    '_context_user_domain': None,
    '_context_auth_token': 'gAAAAABYDnRG3mhPMwyF17iUiIT4nYjtcSktNmmCKlMrUtmpHYsJWl44xU-boIaf4ChWcBsTjl6jOk6Msu7l17As' +
                           '1Y9vFc1rlmKMl86Eknqp0P22RV_Xr6SIobsl6Axl2Z_w-AB1cZ4pSsY4uscxeJdVkoxRb0aC9B7gllrvAgrfO9O' +
                           'GDqw2ILA',
    '_context_tenant_id': 'a83c8b0d2df24170a7c54f09f824230e', '_context_resource_uuid': None,
    '_context_request_id': 'req-3d6810d9-bee9-41b5-a224-7e9641689cc8', '_unique_id': 'b4f1ffae88b342c09658d9ed2829670c',
    'timestamp': '2016-10-24 21:29:56.383789', '_context_project_id': 'a83c8b0d2df24170a7c54f09f824230e',
    '_context_user_identity': '73638a2687534f9794cd8057ba860637 a83c8b0d2df24170a7c54f09f824230e - - -'}

EVENT_PAYLOAD_PORT_ADD_INTF = {
    '_context_timestamp': '2016-10-26 19:14:00.622705',
    '_context_tenant': 'a83c8b0d2df24170a7c54f09f824230e',
    'publisher_id': 'network.node-6.cisco.com', '_context_tenant_name': 'services',
    '_context_show_deleted': False, '_context_user_id': '73638a2687534f9794cd8057ba860637',
    '_context_project_name': 'services',
    '_context_project_id': 'a83c8b0d2df24170a7c54f09f824230e', '_context_user_domain': None,
    'event_type': 'port.create.end', '_context_resource_uuid': None,
    'message_id': '42438e1f-2477-4f1a-b5fc-c27446ea50b4',
    '_context_user': '73638a2687534f9794cd8057ba860637', '_context_roles': ['admin'],
    '_context_auth_token': 'gAAAAABYEPS6lqo8DUMw36Db097YQnGhh2k0Q4bizNxvfsrcpIZlwO4Y548HmdJK4JwbaCpgSfy11dL4aq5y0E62' +
                           '9RYYq6_Xy9xyYhrNn_IyFbQj1AAS5nFAp3m1QqtI1Q0azjQrkkPKTwh_BVp7D1uriWlsdGEWX5r3bdawNx5o' +
                           'FBFiRnAJhhM',
    '_context_is_admin': True, '_context_user_name': 'neutron', '_context_domain': None,
    '_context_project_domain': None,
    '_context_tenant_id': 'a83c8b0d2df24170a7c54f09f824230e', '_context_read_only': False,
    'payload': {'port': {'name': '', 'network_id': '2e3b85f4-756c-49d9-b34c-f3db13212dbc',
                         'binding:host_id': 'node-4.cisco.com', 'allowed_address_pairs': [],
                         'port_security_enabled': True,
                         'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                         'mac_address': 'fa:16:3e:33:00:4c', 'extra_dhcp_opts': [],
                         'status': 'DOWN', 'dns_name': '',
                         'security_groups': ['2dd5c169-1ff7-40e5-ad96-18924b6d23f1'],
                         'device_id': 'fec3fc2d-be50-4234-b41a-1f43069f3a67',
                         'binding:vif_type': 'ovs', 'binding:profile': {},
                         'binding:vnic_type': 'normal',
                         'binding:vif_details': {'ovs_hybrid_plug': True,
                                                 'port_filter': True},
                         'admin_state_up': True,
                         'id': '10e98e6d-72fc-45b0-931d-4a5c58953a15',
                         'device_owner': 'compute:None', 'fixed_ips': [
            {'subnet_id': '9a9c1848-ea23-4c5d-8c40-ae1def4c2de3',
             'ip_address': '172.16.13.7'}]}},
    '_unique_id': '4320656d70684a78a165767b15d50985', 'priority': 'INFO',
    'timestamp': '2016-10-26 19:14:02.086856',
    '_context_user_identity': '73638a2687534f9794cd8057ba860637 a83c8b0d2df24170a7c54f09f824230e - - -',
    '_context_request_id': 'req-c3963c6e-763b-47bf-99c5-6d335c3dd425'}

EVENT_PAYLOAD_PORT_INTERFACE_ADD_1 = {
    '_context_timestamp': '2016-10-26 21:52:15.829792', '_context_project_name': 'OSDNA-project',
    'publisher_id': 'network.node-6.cisco.com', 'timestamp': '2016-10-26 21:52:18.429222',
    '_context_user_name': 'admin',
    '_context_roles': ['_member_', 'admin'], '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_unique_id': 'cff9b9ed7277410da6e2ec97a83c6bdc', 'priority': 'INFO',
    '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40',
    '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
    '_context_user_id': '13baa553aae44adca6615e711fd2f6d9', '_context_user_domain': None,
    '_context_show_deleted': False,
    '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_user': '13baa553aae44adca6615e711fd2f6d9',
    '_context_is_admin': True, 'message_id': '7d620314-b27a-429f-9cf5-5c4edd30dbd6', 'payload': {
    'port': {'status': 'DOWN', 'name': '', 'security_groups': ['2dd5c169-1ff7-40e5-ad96-18924b6d23f1'], 'device_id': '',
             'port_security_enabled': True, 'binding:profile': {}, 'device_owner': '',
             'mac_address': 'fa:16:3e:b5:d1:b5', 'network_id': '95d2a3bb-16b9-4241-ab51-449482fcb9b9',
             'binding:host_id': '', 'dns_assignment': [
            {'hostname': 'host-172-16-9-9', 'fqdn': 'host-172-16-9-9.openstacklocal.', 'ip_address': '172.16.9.9'}],
             'binding:vif_type': 'unbound', 'dns_name': '', 'binding:vif_details': {},
             'id': 'b3e4ea8a-75b6-4c05-9480-4bc648845c6f',
             'fixed_ips': [{'ip_address': '172.16.9.9', 'subnet_id': '6f6ef3b5-76c9-4f70-81e5-f3cc196db025'}],
             'admin_state_up': True, 'allowed_address_pairs': [], 'binding:vnic_type': 'normal',
             'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40'}}, '_context_domain': None, '_context_read_only': False,
    '_context_resource_uuid': None, 'event_type': 'port.create.end',
    '_context_request_id': 'req-86d18db1-ebe4-4673-b21a-6cc0831bbf6c', '_context_project_domain': None,
    '_context_tenant_name': 'OSDNA-project',
    '_context_auth_token': 'gAAAAABYERgkK8sR80wFsQywjt8vwG0caJW5oxfsWNURcDaYAxy0O6P0u2QQczoMuHBAZa-Ga8T1b'+
                           '3O-5p7pjw-vAyI1z5whuY7i-hJSl2II6WUX2-9dy7BALQgxhCGpe60atLcyTl-rW6o_TKc3f-ppvq'+
                           'tiul4UTlzH9OtYN7b-CezaywYDCIMuzGbThPARd9ilQR2B6DuE'}
