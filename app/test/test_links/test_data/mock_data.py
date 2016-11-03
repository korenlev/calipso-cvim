vnics_env = 'WebEX-Mirantis@Cisco'
vnics_find_items = [{
        '_id': '57c54f574a0a8a3fbe3bb4cd',
        'network': '94c3762e-dd47-402f-bf5f-b743d695ef7d',
         'name': 'tapd82ef1bd-d8',
         'parent_id': '1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071-vnics',
         'source_bridge': 'qbrd82ef1bd-d8',
         'alias': {'@name': 'net0'},
         'source': {'@bridge': 'qbrd82ef1bd-d8'},
         'target': {'@dev': 'tapd82ef1bd-d8'},
         'show_in_tree': True,
         'id': 'tapd82ef1bd-d8',
         'instance_db_id': '57c54f524a0a8a3fbe3bb4b7',
         'parent_type': 'vnics_folder',
         'host': 'node-24',
         'mac': {'@address': 'fa:16:3e:f6:37:2a'},
         'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/WebEx-RTP-Zone/node-24/Instances/Webex-Test-VM-dave/vNICs/tapd82ef1bd-d8',
         '@type': 'bridge',
         'environment': 'WebEX-Mirantis@Cisco',
         'children_url': '/osdna_dev/discover.py?type=tree&id=tapd82ef1bd-d8',
         'type': 'vnic',
         'mac_address': 'fa:16:3e:f6:37:2a',
         'object_name': 'tapd82ef1bd-d8',
         'id_path':'/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/WebEx-RTP-Zone/node-24/node-24-instances/1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071/1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071-vnics/tapd82ef1bd-d8',
         'instance_id': '1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071',
         'model': {'@type': 'virtio'},
         'address': {'@type': 'pci', '@slot': '0x03', '@function': '0x0', '@domain': '0x0000', '@bus': '0x00'},
         'vnic_type': 'instance_vnic',
         'clique': True
    }]

oteps_env = 'Mirantis-Liberty'

oteps_find_items = {
    'udp_port': 4789,
     'name': 'node-6.cisco.com-otep', 
     'ip_address': '192.168.2.3',
     'children_url': '/osdna_dev/discover.py?type=tree&id=node-6.cisco.com-otep', 
     'show_in_tree': True,
     '_id': '57c56c194a0a8a3fbe3bb7c0',
     'overlay_type': 'vxlan',
     'parent_type': 'vedge',
     'type': 'otep',
     'ports': {'vxlan-c0a80202': {'options': {'in_key': 'flow', 'df_default': 'true', 'out_key': 'flow', 'remote_ip': '192.168.2.2', 'local_ip': '192.168.2.3'},'name': 'vxlan-c0a80202','type': 'vxlan','interface': 'vxlan-c0a80202'},
     'patch-int': {'options': {'peer': 'patch-tun'},'name': 'patch-int','type': 'patch','interface': 'patch-int'}, 
     'vxlan-c0a80201': {'options': {'in_key': 'flow', 'df_default': 'true', 'out_key': 'flow', 'remote_ip': '192.168.2.1', 'local_ip': '192.168.2.3'}, 'name': 'vxlan-c0a80201', 'type': 'vxlan', 'interface': 'vxlan-c0a80201'}, 'br-tun': {'name': 'br-tun', 'type': 'internal', 'interface': 'br-tun'}},
     'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/vEdges/node-6.cisco.com-OVS/node-6.cisco.com-otep',
     'vconnector': 'br-mesh',
     'id': 'node-6.cisco.com-otep', 
     'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-vedges/1764430c-c09e-4717-86fa-c04350b1fcbb/node-6.cisco.com-otep',
     'parent_id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
     'environment': 'Mirantis-Liberty',
     'host': 'node-6.cisco.com',
     'object_name': 'node-6.cisco.com-otep'
 }

oteps_add_otep_vconnector_link_wrong_param = {}

pnics_find_items = {
'Supports Wake-on': 'd',
 'MDI-X': 'off',
 'Advertised link modes': ['10baseT/Half 10baseT/Full','100baseT/Half 100baseT/Full', '1000baseT/Full'], 
 'Port': 'Twisted Pair',
 'type': 'pnic',
 '_id': '57c54f4e4a0a8a3fbe3bb4a0', 
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/internal/node-14/node-14-pnics/eth1-00:50:56:bd:4a:29',
 'Supported pause frame use': 'No',
 'data': 'Link encap:Ethernet  HWaddr 00:50:56:bd:4a:29\ninet6 addr: fe80::250:56ff:febd:4a29/64 Scope:Link\nUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\nRX packets:53 errors:0 dropped:0 overruns:0 frame:0\nTX packets:99 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:1000\nRX bytes:3582 (3.5 KB)  TX bytes:7156 (7.1 KB)\n', 
 'Transceiver': 'internal',
 'IPv6 Address': 'addr:',
 'children_url': '/osdna_dev/discover.py?type=tree&id=eth1-00:50:56:bd:4a:29',
 'Duplex': 'Full', 
 'name': 'eth1', 
 'Supports auto-negotiation': 'Yes',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/internal/node-14/pNICs/eth1', 
 'show_in_tree': True, 'id': 'eth1-00:50:56:bd:4a:29', 
 'Supported ports': '[ TP ]',
 'Wake-on': 'd',
 'Advertised pause frame use': 'No',
 'Speed': '1000Mb/s', 
 'host': 'node-14', 
 'mac_address': '00:50:56:bd:4a:29',
 'PHYAD': '0', 
 'parent_id': 'node-14-pnics', 
 'Supported link modes': ['10baseT/Half 10baseT/Full','100baseT/Half 100baseT/Full','1000baseT/Full'],
 'local_name': 'eth1', 
 'Current message level': ['0x00000007 (7)', 'drv probe link'], 
 'Advertised auto-negotiation': 'Yes',
 'parent_type': 'pnics_folder',
 'Link detected': 'yes',
 'Auto-negotiation': 'on', 
 'object_name': 'eth1',
 'environment': 'WebEX-Mirantis@Cisco'
 } 

vconnector_find_items ={
'connector_type': 'bridge',
 'host': 'node-23',
 'environment': 'WebEX-Mirantis@Cisco',
 '_id': '57c54f504a0a8a3fbe3bb4a9',
 'show_in_tree': True,
 'object_name': 'qbr6afa6a5d-85',
 'interfaces': {'tap6afa6a5d-85': {'name': 'tap6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}, 'qvb6afa6a5d-85': {'name': 'qvb6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}}, 'parent_id': 'node-23-vconnectors',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vConnectors/qbr6afa6a5d-85',
 'network': '94c3762e-dd47-402f-bf5f-b743d695ef7d',
 'name': 'qbr6afa6a5d-85',
 'type': 'vconnector',
 'interfaces_names': ['tap6afa6a5d-85', 'qvb6afa6a5d-85'],
 'children_url': '/osdna_dev/discover.py?type=tree&id=8000.3afad747e246',
 'parent_type': 'vconnectors_folder',
 'id': '8000.3afad747e246',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vconnectors/8000.3afad747e246',
 'clique': True,
 'stp_enabled': 'no'
 }

vconnector_add_vnic_vconnector_link_vconnector_arg ={
'show_in_tree': True,
 'id': '8000.3afad747e246',
 'host': 'node-23',
 'name': 'qbr6afa6a5d-85',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vconnectors/8000.3afad747e246',
 'clique': True,
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vConnectors/qbr6afa6a5d-85',
 'stp_enabled': 'no',
 'connector_type': 'bridge',
 'children_url': '/osdna_dev/discover.py?type=tree&id=8000.3afad747e246',
 'object_name': 'qbr6afa6a5d-85',
 'environment': 'WebEX-Mirantis@Cisco',
 'network': '94c3762e-dd47-402f-bf5f-b743d695ef7d',
 'parent_type': 'vconnectors_folder',
 'type': 'vconnector',
 'interfaces_names': ['tap6afa6a5d-85', 'qvb6afa6a5d-85'],
 'parent_id': 'node-23-vconnectors',
 'interfaces': {'tap6afa6a5d-85': {'name': 'tap6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}, 'qvb6afa6a5d-85': {'name': 'qvb6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}},
 '_id': '57c54f504a0a8a3fbe3bb4a9'
 }

vconnector_add_vnic_vconnector_link_interface_arg = 'tap6afa6a5d-85'


vconnector_add_vnic_vconnector_link_wrong_interface_arg ={
'show_in_tree': True,
 'id': '8000.3afad747e246',
 'host': 'node-23',
 'name': 'qbr6afa6a5d-85',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vconnectors/8000.3afad747e246',
 'clique': True,
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vConnectors/qbr6afa6a5d-85',
 'stp_enabled': 'no',
 'connector_type': 'bridge',
 'children_url': '/osdna_dev/discover.py?type=tree&id=8000.3afad747e246',
 'object_name': 'qbr6afa6a5d-85',
 'environment': 'WebEX-Mirantis@Cisco',
 'network': '94c3762e-dd47-402f-bf5f-b743d695ef7d',
 'parent_type': 'vconnectors_folder',
 'type': 'vconnector',
 'interfaces_names': ['ethtap6afa6a5d-85', 'qvb6afa6a5d-85'],
 'parent_id': 'node-23-vconnectors',
 'interfaces': {'tap6afa6a5d-85': {'name': 'tap6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}, 'qvb6afa6a5d-85': {'name': 'qvb6afa6a5d-85', 'mac_address': 'fa:16:3e:c9:80:95'}},
 '_id': '57c54f504a0a8a3fbe3bb4a9'
 }


vservice_find_items = {

'children_url': '/osdna_dev/discover.py?type=tree&id=tapa0f357d9-65',
'cidr': '172.16.101.0/24',
 'parent_text': 'vNICs', 
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/internal/node-14/Vservices/DHCP servers/dhcp-net-101/vNICs/tapa0f357d9-65', 
 'host': 'node-14', 
 'parent_id': 'qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f-vnics', 
 'parent_type': 'vnics_folder', 
 'object_name': 'tapa0f357d9-65',
'id_path':'/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/internal/node-14/node-14-vservices/node-14-vservices-dhcps/qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f/qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f-vnics/tapa0f357d9-65',
 'data': 'Link encap:Ethernet  HWaddr fa:16:3e:54:9d:7b\ninet addr:172.16.101.3  Bcast:172.16.101.255  Mask:255.255.255.0\ninet6 addr: fe80::f816:3eff:fe54:9d7b/64 Scope:Link\nUP BROADCAST RUNNING  MTU:1500  Metric:1\nRX packets:407770 errors:0 dropped:0 overruns:0 frame:0\nTX packets:279939 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:101157738 (101.1 MB)  TX bytes:53554986 (53.5 MB)\n', 
 'IP Address': '172.16.101.3',
 'netmask': '255.255.255.0',
 'environment': 'WebEX-Mirantis@Cisco',
 'IPv6 Address': 'fe80::f816:3eff:fe54:9d7b/64',
 'name': 'tapa0f357d9-65',
 '_id': '57c54f4d4a0a8a3fbe3bb47e',
 'vnic_type': 'vservice_vnic',
 'id': 'tapa0f357d9-65', 
 'show_in_tree': True,
 'network': 'a588da43-dd61-4f9a-800e-38831ccdd58f',
 'mac_address': 'fa:16:3e:54:9d:7b',
 'type': 'vnic'
 
 }


vedges_find_items =[{
'tunnel_ports': {},
 'environment': 'WebEX-Mirantis@Cisco',
 'admin_state_up': 1,
 'parent_type': 'vedges_folder',
 'name': 'node-23-OVS',
 'host': 'node-23',
 'ports': {'eth1': {'id': '3', 'internal': False, 'name': 'eth1'}, 'br-mgmt': {'id': '9', 'internal': True, 'name': 'br-mgmt'}, 'ovs-system': {'id': '0', 'internal': True, 'name': 'ovs-system'}, 'eth0': {'id': '7', 'internal': False, 'name': 'eth0'}, 'br-eth0': {'id': '8', 'internal': True, 'name': 'br-eth0'}, 'br-int': {'id': '6', 'internal': True, 'name': 'br-int'}, 'br-prv': {'id': '5', 'internal': True, 'name': 'br-prv'}, 'qvo6afa6a5d-85': {'id': '10', 'internal': False, 'tag': '1', 'name': 'qvo6afa6a5d-85'}, 'br-eth1': {'id': '2', 'internal': True, 'name': 'br-eth1'}, 'br-fw-admin': {'id': '4', 'internal': True, 'name': 'br-fw-admin'}, 'br-storage': {'id': '1', 'internal': True, 'name': 'br-storage'}},
 'id': '0865a97e-715b-41f4-87dc-4d7d4dc871a8',
 'pnic': 'eth0',

 'parent_id': 'node-23-vedges',
 'configurations': {'tunneling_ip': '', 'l2_population': False, 'devices': 1, 'tunnel_types': [], 'enable_distributed_routing': False, 'arp_responder_enabled': False, 'bridge_mappings': {'physnet2': 'br-prv'}},
 'object_name': 'node-23-OVS',

 'topic': 'N/A',
 'show_in_tree': True,
 'children_url': '/osdna_dev/discover.py?type=tree&id=0865a97e-715b-41f4-87dc-4d7d4dc871a8', 
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vedges/0865a97e-715b-41f4-87dc-4d7d4dc871a8',
 'binary': 'neutron-openvswitch-agent',
 'agent_type': 'Open vSwitch agent',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vEdges/node-23-OVS',
 '_id': '57c54f504a0a8a3fbe3bb4aa',
 'description': None,
 'type': 'vedge'
 }]

vedges_add_link_vedge_arg = {
'binary': 'neutron-openvswitch-agent',
 '_id': '57c54f504a0a8a3fbe3bb4aa',
 'pnic': 'eth0',
 'children_url': '/osdna_dev/discover.py?type=tree&id=0865a97e-715b-41f4-87dc-4d7d4dc871a8',
 'admin_state_up': 1,
 'object_name': 'node-23-OVS',
 'type': 'vedge',
 'agent_type': 'Open vSwitch agent',
 'configurations': {'tunnel_types': [], 'l2_population': False, 'devices': 1, 'enable_distributed_routing': False, 'bridge_mappings': {'physnet2': 'br-prv'}, 'tunneling_ip': '', 'arp_responder_enabled': False},
 'name': 'node-23-OVS',
 'parent_type': 'vedges_folder',

 'parent_id': 'node-23-vedges',

 'id': '0865a97e-715b-41f4-87dc-4d7d4dc871a8',
 'show_in_tree': True,
 'environment': 'WebEX-Mirantis@Cisco',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vEdges/node-23-OVS',
 'description': None,
 'topic': 'N/A',
 'ports': {'br-eth0': {'name': 'br-eth0', 'internal': True, 'id': '8'},'br-int': {'name': 'br-int', 'internal': True, 'id': '6'}, 'eth1': {'name': 'eth1', 'internal': False, 'id': '3'}, 'br-eth1': {'name': 'br-eth1', 'internal': True, 'id': '2'}, 'br-storage': {'name': 'br-storage', 'internal': True, 'id': '1'}, 'br-mgmt': {'name': 'br-mgmt', 'internal': True, 'id': '9'}, 'qvo6afa6a5d-85': {'name': 'qvo6afa6a5d-85', 'tag': '1', 'internal': False, 'id': '10'}, 'br-fw-admin': {'name': 'br-fw-admin', 'internal': True, 'id': '4'}, 'br-prv': {'name': 'br-prv', 'internal': True, 'id': '5'}, 'ovs-system': {'name': 'ovs-system', 'internal': True, 'id': '0'}, 'eth0': {'name': 'eth0', 'internal': False, 'id': '7'}},
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vedges/0865a97e-715b-41f4-87dc-4d7d4dc871a8',
 'host': 'node-23',
 'tunnel_ports': {}
 }

vedges_add_link_port_arg={'name': 'br-eth0', 'internal': True, 'id': '8'}


link_instance_vnics_get_by_id_instance = {
'object_name': 'Webex-Test-VM-dave',
 '_id': '57c54f524a0a8a3fbe3bb4b7',
 'projects': ['Webex-Dev'],
 'host': 'node-24',
 'project_id': '9bb12590b58d4c729871dc0c41c5a0f3',
 'network': ['94c3762e-dd47-402f-bf5f-b743d695ef7d'],
 'type': 'instance',
 'ip_address': '192.168.100.8',
 'show_in_tree': True,
 'id': '1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071',
 'network_info': [{'meta': {}, 'network': {'subnets': [{'meta': {}, 'cidr': '172.16.103.0/24', 'gateway': {'meta': {}, 'address': '172.16.103.1', 'type': 'gateway', 'version': 4}, 'dns': [], 'ips': [{'address': '172.16.103.3', 'meta': {}, 'floating_ips': [], 'type': 'fixed', 'version': 4}], 'routes': [], 'version': 4}], 'meta': {'injected': False, 'tenant_id': '9bb12590b58d4c729871dc0c41c5a0f3'}, 'id': '94c3762e-dd47-402f-bf5f-b743d695ef7d', 'label': 'net-103', 'bridge': 'br-int'}, 'vnic_type': 'normal', 'details': {'port_filter': True, 'ovs_hybrid_plug': True}, 'qbg_params': None, 'address': 'fa:16:3e:f6:37:2a', 'qbh_params': None, 'devname': 'tapd82ef1bd-d8', 'active': True, 'id': 'd82ef1bd-d83a-46ca-aa99-b3d17160321b', 'profile': {}, 'ovs_interfaceid': 'd82ef1bd-d83a-46ca-aa99-b3d17160321b', 'type': 'ovs'}],
 'mac_address': 'fa:16:3e:f6:37:2a',
 'name': 'Webex-Test-VM-dave',
 'children_url': '/osdna_dev/discover.py?type=tree&id=1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071',
 'uuid': '1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071',
 'parent_type': 'instances_folder',
 'environment': 'WebEX-Mirantis@Cisco',
 'local_name': 'instance-0000003c',
 'parent_id': 'node-24-instances',
 'clique': True,
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/WebEx-RTP-Zone/node-24/Instances/Webex-Test-VM-dave',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/WebEx-RTP-Zone/node-24/node-24-instances/1ab3e2f6-4e15-4a4a-b55d-fc0a18d2c071'
 }

link_instance_vnics_get_by_id_host ={
'_id': '57c54f4b4a0a8a3fbe3bb464',
 'children_url': '/osdna_dev/discover.py?type=tree&id=node-24',
 'zone': 'WebEx-RTP-Zone',
 'id': 'node-24',
 'show_in_tree': True,
 'environment': 'WebEX-Mirantis@Cisco',
 'ip_address': '192.168.100.8',
 'host': 'node-24',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/WebEx-RTP-Zone/node-24',
 'parent_type': 'availability_zone',
 'name': 'node-24',
 'os_id': '6',
 'object_name': 'node-24',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/WebEx-RTP-Zone/node-24',
 'type': 'host',
 'parent_id': 'WebEx-RTP-Zone',
 'services': {'nova-compute': {'active': True, 'updated_at': '2016-09-11T20:46:07.000000', 'available': True}},
 'host_type': ['Compute']
 }

vservice_find_items = [{
    'network': 'a588da43-dd61-4f9a-800e-38831ccdd58f',
    'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/internal/node-14/Vservices/DHCP servers/dhcp-net-101/vNICs/tapa0f357d9-65',
    'type': 'vnic',
    'vnic_type': 'vservice_vnic',
    'IPv6 Address': 'fe80::f816:3eff:fe54:9d7b/64',
    'data': 'Link encap:Ethernet  HWaddr fa:16:3e:54:9d:7b\ninet addr:172.16.101.3  Bcast:172.16.101.255  Mask:255.255.255.0\ninet6 addr: fe80::f816:3eff:fe54:9d7b/64 Scope:Link\nUP BROADCAST RUNNING  MTU:1500  Metric:1\nRX packets:407770 errors:0 dropped:0 overruns:0 frame:0\nTX packets:279939 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:101157738 (101.1 MB)  TX bytes:53554986 (53.5 MB)\n',
    'environment': 'WebEX-Mirantis@Cisco',
    'mac_address': 'fa:16:3e:54:9d:7b',
    'parent_id': 'qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f-vnics',
    'children_url': '/osdna_dev/discover.py?type=tree&id=tapa0f357d9-65',
    'id_path':'/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/internal/node-14/node-14-vservices/node-14-vservices-dhcps/qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f/qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f-vnics/tapa0f357d9-65',
    'id': 'tapa0f357d9-65',
    'cidr': '172.16.101.0/24',
    'netmask': '255.255.255.0',
    'name': 'tapa0f357d9-65',
    'parent_text': 'vNICs',
    'show_in_tree': True,
    'IP Address': '172.16.101.3',
    '_id': '57c54f4d4a0a8a3fbe3bb47e',
    'host': 'node-14',
    'parent_type': 'vnics_folder',
    'object_name': 'tapa0f357d9-65'
    }]


vedge_port= {'id': '7', 'internal': False, 'name': 'eth0'}

vservice_host= {
'host_type': ['Controller', 'Network'],
 'services': {'nova-conductor': {'active': True, 'available': True, 'updated_at': '2016-09-11T20:46:11.000000'}, 'nova-consoleauth': {'active': True, 'available': True, 'updated_at': '2016-09-11T20:46:10.000000'}, 'nova-cert': {'active': True, 'available': True, 'updated_at': '2016-09-11T20:46:09.000000'}, 'nova-scheduler': {'active': True, 'available': True, 'updated_at': '2016-09-11T20:46:07.000000'}},
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/internal/node-14',
 'id': 'node-14',
 'children_url': '/osdna_dev/discover.py?type=tree&id=node-14',
 'name': 'node-14',
 'type': 'host',
 'config': {'use_namespaces': True, 'dhcp_lease_duration': 120, 'networks': 5, 'dhcp_driver': 'neutron.agent.linux.dhcp.Dnsmasq', 'ports': 13, 'subnets': 5},
 'show_in_tree': True,
 'parent_id': 'internal',
 '_id': '57c54f4b4a0a8a3fbe3bb461',
 'host': 'node-14',
 'environment': 'WebEX-Mirantis@Cisco',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/internal/node-14',
 'zone': 'internal',
 'parent_type': 'availability_zone',
 'object_name': 'node-14',

 }

vservice_network= {
'network': 'a588da43-dd61-4f9a-800e-38831ccdd58f',
 'name_path': '/WebEX-Mirantis@Cisco/Projects/Webex-Dev/Networks/net-101',
 'status': 'ACTIVE',
 'provider:segmentation_id': 1000,
 'subnets': {'sub101': {'tenant_id': '9bb12590b58d4c729871dc0c41c5a0f3', 'dns_nameservers': [], 'id': 'e157baad-e113-48e9-b479-41435590c9a9', 'cidr': '172.16.101.0/24', 'name': 'sub101', 'ipv6_ra_mode': None, 'network_id': 'a588da43-dd61-4f9a-800e-38831ccdd58f', 'gateway_ip': '172.16.101.1', 'ipv6_address_mode': None, 'enable_dhcp': True, 'allocation_pools': [{'end': '172.16.101.254', 'start': '172.16.101.2'}], 'ip_version': 4, 'host_routes': []}},
 'cidrs': ['172.16.101.0/24'],
 'parent_id': '9bb12590b58d4c729871dc0c41c5a0f3-networks',
 'router:external': False,
 'environment': 'WebEX-Mirantis@Cisco',
 'provider:network_type': 'vlan',
 'clique': True,
 'name': 'net-101',
 'children_url': '/osdna_dev/discover.py?type=tree&id=a588da43-dd61-4f9a-800e-38831ccdd58f',
 'tenant_id': '9bb12590b58d4c729871dc0c41c5a0f3',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-projects/9bb12590b58d4c729871dc0c41c5a0f3/9bb12590b58d4c729871dc0c41c5a0f3-networks/a588da43-dd61-4f9a-800e-38831ccdd58f',
 'id': 'a588da43-dd61-4f9a-800e-38831ccdd58f',
 'project': 'Webex-Dev',
 'type': 'network',
 'parent_text': 'Networks',
 'show_in_tree': True,
 'provider:physical_network': 'physnet2',
 '_id': '57c54f4a4a0a8a3fbe3bb444',
 'shared': False,
 'admin_state_up': True,
 'parent_type': 'networks_folder', 
 'object_name': 'net-101'
 }

vservice_vservice= {
'network': ['a588da43-dd61-4f9a-800e-38831ccdd58f'],
 'service_type': 'dhcp',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/internal/node-14/Vservices/DHCP servers/dhcp-net-101',
 'id': 'qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f',
 'type': 'vservice',
 'parent_text': 'DHCP servers',
 'show_in_tree': True,
 'parent_id': 'node-14-vservices-dhcps',
 '_id': '57c54f4c4a0a8a3fbe3bb472',
 'host': 'node-14',
 'environment': 'WebEX-Mirantis@Cisco',
 'local_service_id': 'qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f',
 'clique': True,
 'parent_type': 'vservice_dhcps_folder',
 'name': 'dhcp-net-101',
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/internal/node-14/node-14-vservices/node-14-vservices-dhcps/qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f',
 'object_name': 'dhcp-net-101',
 'children_url': '/osdna_dev/discover.py?type=tree&id=qdhcp-a588da43-dd61-4f9a-800e-38831ccdd58f'
 }

pnics_find_items=[{
    'name': 'eno33554952.103@eno33554952',
    'Supported pause frame use': 'No',
    'Transceiver': 'internal',
    'local_name': 'eno33554952.103@eno33554952',
    'Advertised pause frame use': 'No',
    '_id': '57c56c0b4a0a8a3fbe3bb79a',
    'object_name': 'eno33554952.103@eno33554952',
    'children_url': '/osdna_dev/discover.py?type=tree&id=eno33554952.103@eno33554952-00:50:56:ac:c9:a2',
    'Speed': '1000Mb/s',
    'Current message level': ['0x00000007 (7)', 'drv probe link'],
    'mac_address': '00:50:56:ac:c9:a2',
    'id': 'eno33554952.103@eno33554952-00:50:56:ac:c9:a2',
    'parent_id': 'node-6.cisco.com-pnics',
    'PHYAD': '0',
    'environment': 'Mirantis-Liberty',
    'Advertised auto-negotiation': 'Yes',
    'show_in_tree': True,
    'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-pnics/eno33554952.103@eno33554952-00:50:56:ac:c9:a2',
    'Link detected': 'yes',
    'Supports Wake-on': 'd',
    'MDI-X': 'off (auto)',
    'Port': 'Twisted Pair',
    'IPv6 Address': 'addr:',
    'type': 'pnic',
    'data': 'Link encap:Ethernet  HWaddr 00:50:56:ac:c9:a2\ninet6 addr: fe80::250:56ff:feac:c9a2/64 Scope:Link\nUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\nRX packets:405772 errors:0 dropped:0 overruns:0 frame:0\nTX packets:404734 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:56960427 (56.9 MB)  TX bytes:65035071 (65.0 MB)\n', 'Wake-on': 'd',
    'Auto-negotiation': 'on',
    'Duplex': 'Full',
    'host': 'node-6.cisco.com',
    'clique': True,
    'Supported ports': '[ TP ]',
    'Advertised link modes': ['10baseT/Half 10baseT/Full','100baseT/Half 100baseT/Full','1000baseT/Full'],
    'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/pNICs/eno33554952.103@eno33554952',
    'Supports auto-negotiation': 'Yes',
    'Supported link modes': ['10baseT/Half 10baseT/Full','100baseT/Half 100baseT/Full','1000baseT/Full'],
    'parent_type': 'pnics_folder'
    }]


pnics_ports = [{'network_id': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe', '_id': '57c56bfb4a0a8a3fbe3bb747', 'id': '16620a58-c48c-4195-b9c1-779a8ba2e6f8', 'children_url': '/osdna_dev/discover.py?type=tree&id=16620a58-c48c-4195-b9c1-779a8ba2e6f8'}]


pnics_network={'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40',
 'cidrs': ['172.16.4.0/24'],
 'show_in_tree': True,
 'mtu': 1400,
 'provider:physical_network': None,
 'provider:network_type': 'vxlan',
 'id_path': '/Mirantis-Liberty/Mirantis-Liberty-projects/75c0eb79ff4a42b0ae4973c8375ddf40/75c0eb79ff4a42b0ae4973c8375ddf40-networks/b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'parent_type': 'networks_folder',
 'router:external': False,
 'network': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'name_path': '/Mirantis-Liberty/Projects/OSDNA-project/Networks/osdna-met4',
 'status': 'ACTIVE',
 'project': 'OSDNA-project',
 'name': 'osdna-met4',
 'environment': 'Mirantis-Liberty',
 'children_url': '/osdna_dev/discover.py?type=tree&id=b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'admin_state_up': True,
 '_id': '57c56bfb4a0a8a3fbe3bb740',
 'parent_text': 'Networks',
 'shared': False,
 'object_name': 'osdna-met4',
 'id': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'provider:segmentation_id': 96,
 'port_security_enabled': True,
 'type': 'network',
 'subnets': {'osdna-subnet4': {'ipv6_ra_mode': None, 'tenant_id': '75c0eb79ff4a42b0ae4973c8375ddf40', 'gateway_ip': '172.16.4.1', 'id': 'f68b9dd3-4cb5-46aa-96b1-f9c8a7abc3aa', 'ip_version': 4, 'subnetpool_id': None, 'ipv6_address_mode': None, 'host_routes': [], 'network_id': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe', 'dns_nameservers': [], 'enable_dhcp': True, 'cidr': '172.16.4.0/24', 'name': 'osdna-subnet4', 'allocation_pools': [{'end': '172.16.4.254', 'start': '172.16.4.2'}]}},
 'parent_id': '75c0eb79ff4a42b0ae4973c8375ddf40-networks'
 }

otep_find_items = [{'id': 'node-6.cisco.com-otep',
    'name': 'node-6.cisco.com-otep',
    'parent_id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
    'overlay_type': 'vxlan',
    'host': 'node-6.cisco.com',
    'ip_address': '192.168.2.3',
    'ports': {'patch-int': {'interface': 'patch-int', 'options': {'peer': 'patch-tun'}, 'name': 'patch-int', 'type': 'patch'}, 'br-tun': {'interface': 'br-tun', 'name': 'br-tun', 'type': 'internal'}, 'vxlan-c0a80202': {'interface': 'vxlan-c0a80202', 'options': {'df_default': 'true', 'in_key': 'flow', 'out_key': 'flow', 'local_ip': '192.168.2.3', 'remote_ip': '192.168.2.2'}, 'name': 'vxlan-c0a80202', 'type': 'vxlan'}, 'vxlan-c0a80201': {'interface': 'vxlan-c0a80201', 'options': {'df_default': 'true', 'in_key': 'flow', 'out_key': 'flow', 'local_ip': '192.168.2.3', 'remote_ip': '192.168.2.1'}, 'name': 'vxlan-c0a80201', 'type': 'vxlan'}},
    'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/vEdges/node-6.cisco.com-OVS/node-6.cisco.com-otep',
    'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-vedges/1764430c-c09e-4717-86fa-c04350b1fcbb/node-6.cisco.com-otep',
    'show_in_tree': True,
    'parent_type': 'vedge',
    '_id': '57c56c194a0a8a3fbe3bb7c0',
    'udp_port': 4789,
    'object_name': 'node-6.cisco.com-otep',
    'children_url': '/osdna_dev/discover.py?type=tree&id=node-6.cisco.com-otep',
    'environment': 'Mirantis-Liberty',
    'type': 'otep',
    'vconnector': 'br-mesh'
    }]

otep_link_vedge ={
'id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
 'children_url': '/osdna_dev/discover.py?type=tree&id=1764430c-c09e-4717-86fa-c04350b1fcbb',
 'environment': 'Mirantis-Liberty',
 'admin_state_up': 1,
 'name': 'neutron-openvswitch-agent',
 'load': 0,
 'agent_type': 'Open vSwitch agent',
 'host': 'node-6.cisco.com',
 'binary': 'neutron-openvswitch-agent',
 'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-network_agents/1764430c-c09e-4717-86fa-c04350b1fcbb',
 'show_in_tree': True,
 'parent_id': 'node-6.cisco.com-network_agents',
 'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/Network agents/neutron-openvswitch-agent',
 'configurations': {'bridge_mappings': {'physnet1': 'br-floating'}, 'tunneling_ip': '192.168.2.3', 'in_distributed_mode': False, 'arp_responder_enabled': True, 'log_agent_heartbeats': False, 'devices': 11, 'l2_population': True, 'tunnel_types': ['vxlan'], 'extensions': [], 'enable_distributed_routing': False}, 
 'type': 'network_agent',
 'description': None,
 'object_name': 'neutron-openvswitch-agent',
 'parent_type': 'network_agents_folder',
 'topic': 'N/A',
 '_id': '57c56c0c4a0a8a3fbe3bb7a0'
 }

vconnector_link_vconnectors=[{
'environment': 'Mirantis-Liberty',
 'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/vConnectors/br-mesh',
 'connector_type': 'bridge',
 'show_in_tree': True,
 'parent_type': 'vconnectors_folder',
 'interfaces': {'eno33554952.103': {'mac_address': '', 'name': 'eno33554952.103'}},
 'host': 'node-6.cisco.com',
 'children_url': '/osdna_dev/discover.py?type=tree&id=8000.005056acc9a2',
 'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-vconnectors/8000.005056acc9a2',
 'id': '8000.005056acc9a2',
 'object_name': 'br-mesh',
 'network': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'stp_enabled': 'no',
 'interfaces_names': ['eno33554952.103'],
 'type': 'vconnector', 
 'name': 'br-mesh',
 '_id': '57c56c0b4a0a8a3fbe3bb79d',
 'parent_id': 'node-6.cisco.com-vconnectors'
 }]

vconnector_interface = 'eth6afa6a5d-85'

vconnector_interface_ifname = '6afa6a5d-85'

vconnector_vnic = {
'parent_type': 'vnics_folder',
 'instance_db_id': '57c54f4f4a0a8a3fbe3bb4a6',
 'mac': {'@address': 'fa:16:3e:c9:80:95'},
 'model': {'@type': 'virtio'},
 'instance_id': '64283350-0537-4835-a3be-a41b47429fcc',
 '@type': 'bridge',
 'source_bridge': 'qbr6afa6a5d-85',
 'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/Instances/koren-vm-test2/vNICs/tap6afa6a5d-85',
 'environment': 'WebEX-Mirantis@Cisco',
 'source': {'@bridge': 'qbr6afa6a5d-85'},
 'mac_address': 'fa:16:3e:c9:80:95',
 'network': '94c3762e-dd47-402f-bf5f-b743d695ef7d',
 'alias': {'@name': 'net0'},
 'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-instances/64283350-0537-4835-a3be-a41b47429fcc/64283350-0537-4835-a3be-a41b47429fcc-vnics/tap6afa6a5d-85',
 'clique': True,
 '_id': '57c54f554a0a8a3fbe3bb4c8',
 'type': 'vnic',
 'children_url': '/osdna_dev/discover.py?type=tree&id=tap6afa6a5d-85',
 'address': {'@bus': '0x00', '@domain': '0x0000', '@type': 'pci', '@function': '0x0', '@slot': '0x03'},
 'parent_id': '64283350-0537-4835-a3be-a41b47429fcc-vnics',
 'object_name': 'tap6afa6a5d-85',
 'name': 'tap6afa6a5d-85',
 'show_in_tree': True,
 'host': 'node-23',
 'vnic_type': 'instance_vnic',
 'target': {'@dev': 'tap6afa6a5d-85'},
 'id': 'tap6afa6a5d-85'
 }

vconnector_interface_dict = {'mac_address':None,'test':'unittest'}

vconnector_interface_dummy = {'test':'unittest'}


vconnector_link_vconnector={
'environment': 'Mirantis-Liberty',
 'name_path': '/Mirantis-Liberty/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/vConnectors/br-mesh',
 'connector_type': 'bridge',
 'show_in_tree': True,
 'parent_type': 'vconnectors_folder',
 'interfaces': {'eno33554952.103': {'mac_address': '', 'name': 'eno33554952.103'}},
 'host': 'node-6.cisco.com',
 'children_url': '/osdna_dev/discover.py?type=tree&id=8000.005056acc9a2',
 'id_path': '/Mirantis-Liberty/Mirantis-Liberty-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-vconnectors/8000.005056acc9a2',
 'id': '8000.005056acc9a2',
 'object_name': 'br-mesh',
 'network': 'b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe',
 'stp_enabled': 'no',
 'interfaces_names': ['eno33554952.103'],
 'type': 'vconnector', 
 'name': 'br-mesh',
 '_id': '57c56c0b4a0a8a3fbe3bb79d',
 'parent_id': 'node-6.cisco.com-vconnectors'
 }


vedge_vedges= [{
    'parent_id': 'node-23-vedges',
    'host': 'node-23',
    'environment': 'WebEX-Mirantis@Cisco',
    'type': 'vedge',
    'object_name': 'node-23-OVS',
    'children_url': '/osdna_dev/discover.py?type=tree&id=0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'ports': {'eth0': {'id': '7', 'internal': False, 'name': 'eth0'}, 'eth1': {'id': '3', 'internal': False, 'name': 'eth1'}, 'br-storage': {'id': '1', 'internal': True, 'name': 'br-storage'}, 'br-fw-admin': {'id': '4', 'internal': True, 'name': 'br-fw-admin'}, 'br-mgmt': {'id': '9', 'internal': True, 'name': 'br-mgmt'}, 'br-eth0': {'id': '8', 'internal': True, 'name': 'br-eth0'}, 'br-prv': {'id': '5', 'internal': True, 'name': 'br-prv'}, 'qvo6afa6a5d-85': {'id': '10', 'tag': '1', 'internal': False, 'name': 'qvo6afa6a5d-85'}, 'ovs-system': {'id': '0', 'internal': True, 'name': 'ovs-system'}, 'br-eth1': {'id': '2', 'internal': True, 'name': 'br-eth1'}, 'br-int': {'id': '6', 'internal': True, 'name': 'br-int'}},
    'parent_type': 'vedges_folder',
    'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vedges/0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'show_in_tree': True, 
    'description': None, 
    'name': 'node-23-OVS',
    'pnic': 'eth0',
    'admin_state_up': 1,
    'mac_address':None,
    'tunnel_ports': {},
    'agent_type': 'Open vSwitch agent',
    'configurations': {'devices': 1, 'enable_distributed_routing': False, 'bridge_mappings': {'physnet2': 'br-prv'}, 'tunnel_types': [], 'l2_population': False, 'arp_responder_enabled': False, 'tunneling_ip': ''},
    '_id': '57c54f504a0a8a3fbe3bb4aa',
    'binary': 'neutron-openvswitch-agent',
    'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vEdges/node-23-OVS',
    'id': '0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'topic': 'N/A'
    }]


vedge_vedge= {
    'parent_id': 'node-23-vedges',
    'host': 'node-23',
    'environment': 'WebEX-Mirantis@Cisco',
    'type': 'vedge',
    'object_name': 'node-23-OVS',
    'children_url': '/osdna_dev/discover.py?type=tree&id=0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'ports': {'eth0': {'id': '7', 'internal': False, 'name': 'eth0'}, 'eth1': {'id': '3', 'internal': False, 'name': 'eth1'}, 'br-storage': {'id': '1', 'internal': True, 'name': 'br-storage'}, 'br-fw-admin': {'id': '4', 'internal': True, 'name': 'br-fw-admin'}, 'br-mgmt': {'id': '9', 'internal': True, 'name': 'br-mgmt'}, 'br-eth0': {'id': '8', 'internal': True, 'name': 'br-eth0'}, 'br-prv': {'id': '5', 'internal': True, 'name': 'br-prv'}, 'qvo6afa6a5d-85': {'id': '10', 'tag': '1', 'internal': False, 'name': 'qvo6afa6a5d-85'}, 'ovs-system': {'id': '0', 'internal': True, 'name': 'ovs-system'}, 'br-eth1': {'id': '2', 'internal': True, 'name': 'br-eth1'}, 'br-int': {'id': '6', 'internal': True, 'name': 'br-int'}},
    'parent_type': 'vedges_folder',
    'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vedges/0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'show_in_tree': True, 
    'description': None, 
    'name': 'node-23-OVS',
    'pnic': 'eth0',
    'mac_address':None,
    'admin_state_up': 1,
    'Link detected':None,
    'interfaces':{},
    'tunnel_ports': {},
    'agent_type': 'Open vSwitch agent',
    'configurations': {'devices': 1, 'enable_distributed_routing': False, 'bridge_mappings': {'physnet2': 'br-prv'}, 'tunnel_types': [], 'l2_population': False, 'arp_responder_enabled': False, 'tunneling_ip': ''},
    '_id': '57c54f504a0a8a3fbe3bb4aa',
    'binary': 'neutron-openvswitch-agent',
    'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vEdges/node-23-OVS',
    'id': '0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'topic': 'N/A'
    }

vedge_port_negative_case= {'id': '7', 'internal': False, 'name': 'xxxxxeth0'}


vedge_vedge_pname_negative_case= {
    'parent_id': 'node-23-vedges',
    'host': 'node-23',
    'environment': 'WebEX-Mirantis@Cisco',
    'type': 'vedge',
    'object_name': 'node-23-OVS',
    'children_url': '/osdna_dev/discover.py?type=tree&id=0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'ports': {'eth0': {'id': '7', 'internal': False, 'name': 'eth0'}, 'eth1': {'id': '3', 'internal': False, 'name': 'eth1'}, 'br-storage': {'id': '1', 'internal': True, 'name': 'br-storage'}, 'br-fw-admin': {'id': '4', 'internal': True, 'name': 'br-fw-admin'}, 'br-mgmt': {'id': '9', 'internal': True, 'name': 'br-mgmt'}, 'br-eth0': {'id': '8', 'internal': True, 'name': 'br-eth0'}, 'br-prv': {'id': '5', 'internal': True, 'name': 'br-prv'}, 'qvo6afa6a5d-85': {'id': '10', 'tag': '1', 'internal': False, 'name': 'qvo6afa6a5d-85'}, 'ovs-system': {'id': '0', 'internal': True, 'name': 'ovs-system'}, 'br-eth1': {'id': '2', 'internal': True, 'name': 'br-eth1'}, 'br-int': {'id': '6', 'internal': True, 'name': 'br-int'}},
    'parent_type': 'vedges_folder',
    'id_path': '/WebEX-Mirantis@Cisco/WebEX-Mirantis@Cisco-regions/RegionOne/RegionOne-availability_zones/nova/node-23/node-23-vedges/0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'show_in_tree': True, 
    'description': None, 
    'name': 'node-23-OVS',
    'pnic': 'xxxxxeth0',
    'mac_address':None,
    'admin_state_up': 1,
    'Link detected':None,
    'tunnel_ports': {},
    'agent_type': 'Open vSwitch agent',
    'configurations': {'devices': 1, 'enable_distributed_routing': False, 'bridge_mappings': {'physnet2': 'br-prv'}, 'tunnel_types': [], 'l2_population': False, 'arp_responder_enabled': False, 'tunneling_ip': ''},
    '_id': '57c54f504a0a8a3fbe3bb4aa',
    'binary': 'neutron-openvswitch-agent',
    'name_path': '/WebEX-Mirantis@Cisco/Regions/RegionOne/Availability Zones/nova/node-23/vEdges/node-23-OVS',
    'id': '0865a97e-715b-41f4-87dc-4d7d4dc871a8',
    'topic': 'N/A'
    }

false = False

true = True

vedge_port_pname_check= {'id': '7', 'internal': False, 'name': 'qveth0'}