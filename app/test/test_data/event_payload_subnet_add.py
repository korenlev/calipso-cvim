
EVENT_PAYLOAD_NETWORK_ADD = {
    'payload': {'network': {'provider:segmentation_id': 46, 'status': 'ACTIVE', 'provider:physical_network': None,
                         'admin_state_up': True, 'router:external': False, 'mtu': 1400,
                         'id': '0bb0ba6c-6863-4121-ac89-93f81a9da2b0', 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
                         'subnets': [], 'shared': False, 'provider:network_type': 'vxlan', 'name': 'testsubnetadd',
                         'port_security_enabled': True}}, '_context_domain': None,
 'timestamp': '2016-10-13 00:20:59.280329', '_context_project_domain': None, '_context_user_domain': None,
 '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'publisher_id': 'network.node-6.cisco.com',
 '_context_user': '13baa553aae44adca6615e711fd2f6d9', '_context_user_id': '13baa553aae44adca6615e711fd2f6d9',
 'event_type': 'network.create.end', 'message_id': '088354a1-4076-4a7b-9a5c-abcb9bfe1b28',
 '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_tenant_name': 'OSDNA-project',
 '_context_project_name': 'OSDNA-project', '_context_user_name': 'admin', '_context_resource_uuid': None,
 '_unique_id': 'b77990676891461fad12df3658c14282', '_context_request_id': 'req-7886786a-e5b2-4ee4-81da-e825eac31807',
 'priority': 'INFO', '_context_roles': ['_member_', 'admin'],
 '_context_auth_token': 'gAAAAABX_tLMEzC9KhdcD20novcuvgwmpQkwV9hOk86d4AZlsQwXSRbCwBZgUPQZco4VsuCg59_gFeM_scBVmIdDy' +
                        'sNUrAhZctDzXneM0cb5nBtjJTfJPpI2_kKgAuGDBARrHZpNs-vPg-SjMtu87w2rgTKfda6idTMKWG3ipe-jXrgNN7' +
                        'p-2kkJzGhZXbMaaeBs3XU-X_ew',
 '_context_read_only': False,
 '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
 '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_is_admin': True, '_context_show_deleted': False,
 '_context_timestamp': '2016-10-13 00:20:58.925642'}


EVENT_PAYLOAD_SUBNET_ADD = {
    'payload': {
    'subnet': {'dns_nameservers': [], 'ipv6_address_mode': None, 'ipv6_ra_mode': None, 'gateway_ip': '172.16.10.1',
               'allocation_pools': [{'start': '172.16.10.2', 'end': '172.16.10.126'}], 'enable_dhcp': True,
               'id': 'e950055d-231c-4380-983c-a258ea958d58', 'network_id': '0bb0ba6c-6863-4121-ac89-93f81a9da2b0',
               'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'ip_version': 4, 'cidr': '172.16.10.0/25',
               'subnetpool_id': None, 'name': 'testsubnetadd', 'host_routes': []}}, '_context_domain': None,
 'timestamp': '2016-10-13 00:20:59.776358', '_context_project_domain': None, '_context_user_domain': None,
 '_context_project_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'publisher_id': 'network.node-6.cisco.com',
 '_context_user': '13baa553aae44adca6615e711fd2f6d9', '_context_user_id': '13baa553aae44adca6615e711fd2f6d9',
 'event_type': 'subnet.create.end', 'message_id': '90581321-e9c9-4112-8fe6-38ebf57d5b6b',
 '_context_tenant': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_tenant_name': 'OSDNA-project',
 '_context_project_name': 'OSDNA-project', '_context_user_name': 'admin', '_context_resource_uuid': None,
 '_unique_id': 'e8b328229a724938a6bc63f9db737f49', '_context_request_id': 'req-20cfc138-4e1a-472d-b996-7f27ac58446d',
 'priority': 'INFO', '_context_roles': ['_member_', 'admin'],
 '_context_auth_token': 'gAAAAABX_tLMEzC9KhdcD20novcuvgwmpQkwV9hOk86d4AZlsQwXSRbCwBZgUPQZco4VsuCg59_gFeM_scBVmIdDys' +
                        'NUrAhZctDzXneM0cb5nBtjJTfJPpI2_kKgAuGDBARrHZpNs-vPg-SjMtu87w2rgTKfda6idTMKWG3ipe-jXrgNN7p-2'+
                        'kkJzGhZXbMaaeBs3XU-X_ew',
 '_context_read_only': False,
 '_context_user_identity': '13baa553aae44adca6615e711fd2f6d9 75c0eb79ff4a42b0ae4973c8375ddf40 - - -',
 '_context_tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', '_context_is_admin': True, '_context_show_deleted': False,
 '_context_timestamp': '2016-10-13 00:20:59.307917'}


