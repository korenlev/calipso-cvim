import datetime

NETWORK_AGENT_FOLDER = {
    "create_object" : True,
    "environment" : "Mirantis-Liberty-Xiaocong",
    "id" : "node-6.cisco.com-network_agents",
    "id_path" : "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-network_agents",
    "name" : "Network agents",
    "name_path" : "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/Network agents",
    "object_name" : "Network agents",
    "parent_id" : "node-6.cisco.com",
    "parent_type" : "host",
    "show_in_tree" : True,
    "text" : "Network agents",
    "type" : "network_agents_folder"
}
HOST = {
    "config" : {
        "metadata_proxy_socket" : "/opt/stack/data/neutron/metadata_proxy",
        "nova_metadata_ip" : "192.168.20.14",
        "log_agent_heartbeats" : False
    },
    "environment" : "Devstack-VPP-2",
    "host" : "ubuntu0",
    "host_type" : [
        "Controller",
        "Compute",
        "Network"
    ],
    "id" : "ubuntu0",
    "id_path" : "/Devstack-VPP-2/Devstack-VPP-2-regions/RegionOne/RegionOne-availability_zones/nova/ubuntu0",
    "ip_address" : "192.168.20.14",
    "name" : "ubuntu0",
    "name_path" : "/Devstack-VPP-2/Regions/RegionOne/Availability Zones/nova/ubuntu0",
    "object_name" : "ubuntu0",
    "os_id" : "1",
    "parent_id" : "nova",
    "parent_type" : "availability_zone",
    "services" : {
        "nova-conductor" : {
            "available" : True,
            "active" : True,
            "updated_at" : "2016-08-30T09:18:58.000000"
        },
        "nova-scheduler" : {
            "available" : True,
            "active" : True,
            "updated_at" : "2016-08-30T09:18:54.000000"
        },
        "nova-consoleauth" : {
            "available" : True,
            "active" : True,
            "updated_at" : "2016-08-30T09:18:54.000000"
        }
    },
    "show_in_tree" : True,
    "type" : "host",
    "zone" : "nova"
}
NETWORK_AGENT = [
    {
        'configurations': '{"in_distributed_mode": false, "arp_responder_enabled": true, "tunneling_ip": "192.168.2.3", "devices": 22, "extensions": [], "l2_population": true, "tunnel_types": ["vxlan"], "log_agent_heartbeats": false, "enable_distributed_routing": false, "bridge_mappings": {"physnet1": "br-floating"}}',
        'description': None,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 34),
        'agent_type': 'Open vSwitch agent',
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 33),
        'id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
        'host': 'node-6.cisco.com',
        'admin_state_up': 1,
        'topic': 'N/A',
        'created_at': datetime.datetime(2016, 4, 17, 14, 7, 5),
        'binary': 'neutron-openvswitch-agent',
        'load': 0
    },
    {
        'configurations': '{"subnets": 8, "use_namespaces": true, "dhcp_lease_duration": 600, "dhcp_driver": "neutron.agent.linux.dhcp.Dnsmasq", "ports": 28, "log_agent_heartbeats": false, "networks": 8}',
        'description': None,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 41),
        'agent_type': 'DHCP agent',
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 27),
        'id': '2c2ddfee-91f9-47da-bd65-aceecd998b7c',
        'host': 'node-6.cisco.com',
        'admin_state_up': 1,
        'topic': 'dhcp_agent',
        'created_at': datetime.datetime(2016, 4, 17, 14, 9, 9),
        'binary': 'neutron-dhcp-agent', 'load': 8
    },
    {
        'configurations': '{"log_agent_heartbeats": false, "nova_metadata_ip": "192.168.0.2", "nova_metadata_port": 8775, "metadata_proxy_socket": "/var/lib/neutron/metadata_proxy"}',
        'description': None,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 48),
        'agent_type': 'Metadata agent',
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 28),
        'id': '4b929bd3-7ce8-42b9-8c60-89b29ce5aadc',
        'host': 'node-6.cisco.com',
        'admin_state_up': 1,
        'topic': 'N/A',
        'created_at': datetime.datetime(2016, 4, 17, 14, 9, 44),
        'binary': 'neutron-metadata-agent', 'load': 0
    },
    {
        'configurations': '{"router_id": "", "agent_mode": "legacy", "gateway_external_network_id": "", "handle_internal_only_routers": true, "use_namespaces": true, "routers": 5, "interfaces": 9, "floating_ips": 1, "interface_driver": "neutron.agent.linux.interface.OVSInterfaceDriver", "log_agent_heartbeats": false, "external_network_bridge": "", "ex_gw_ports": 5}',
        'description': None,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 25),
        'agent_type': 'L3 agent',
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 27),
        'id': 'ed11ec68-e6e0-4c55-90f3-a217643309aa',
        'host': 'node-6.cisco.com',
        'admin_state_up': 1,
        'topic': 'l3_agent',
        'created_at': datetime.datetime(2016, 4, 17, 14, 8, 28), 'binary': 'neutron-l3-agent', 'load': 0
    }
]

# functional test
INPUT = "node-6.cisco.com-network_agents"
OUTPUT = [
    {
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 33),
        'admin_state_up': 1,
        'configurations': {
            'l2_population': True,
            'tunnel_types': ['vxlan'],
            'devices': 22,
            'bridge_mappings': {
                'physnet1': 'br-floating'
            },
            'extensions': [],
            'in_distributed_mode': False,
            'tunneling_ip': '192.168.2.3',
            'enable_distributed_routing': False,
            'arp_responder_enabled': True,
            'log_agent_heartbeats': False
        }
      , 'binary': 'neutron-openvswitch-agent',
        'id': 'OVS-1764430c-c09e-4717-86fa-c04350b1fcbb',
        'agent_type': 'Open vSwitch agent',
        'host': 'node-6.cisco.com',
        'load': 0,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 34),
        'name': 'neutron-openvswitch-agent',
        'description': None,
        'topic': 'N/A',
        'created_at': datetime.datetime(2016, 4, 17, 14, 7, 5)
    },
    {
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 27),
        'admin_state_up': 1,
        'configurations': {
            'subnets': 8,
            'networks': 8,
            'dhcp_lease_duration': 600,
            'dhcp_driver': 'neutron.agent.linux.dhcp.Dnsmasq',
            'ports': 28,
            'use_namespaces': True,
            'log_agent_heartbeats': False
        },
        'binary': 'neutron-dhcp-agent',
        'id': 'OVS-2c2ddfee-91f9-47da-bd65-aceecd998b7c',
        'agent_type': 'DHCP agent',
        'host': 'node-6.cisco.com',
        'load': 8,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 41),
        'name': 'neutron-dhcp-agent',
        'description': None,
        'topic': 'dhcp_agent',
        'created_at': datetime.datetime(2016, 4, 17, 14, 9, 9)
    },
    {
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 28),
        'admin_state_up': 1,
        'configurations': {
            'nova_metadata_port': 8775,
            'metadata_proxy_socket': '/var/lib/neutron/metadata_proxy',
            'nova_metadata_ip': '192.168.0.2',
            'log_agent_heartbeats': False
        },
        'binary': 'neutron-metadata-agent',
        'id': 'OVS-4b929bd3-7ce8-42b9-8c60-89b29ce5aadc',
        'agent_type': 'Metadata agent',
        'host': 'node-6.cisco.com',
        'load': 0,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 48),
        'name': 'neutron-metadata-agent',
        'description': None,
        'topic': 'N/A',
        'created_at': datetime.datetime(2016, 4, 17, 14, 9, 44)
    },
    {
        'heartbeat_timestamp': datetime.datetime(2016, 10, 28, 0, 51, 27),
        'admin_state_up': 1,
        'configurations': {
            'gateway_external_network_id': '',
            'interface_driver': 'neutron.agent.linux.interface.OVSInterfaceDriver',
            'floating_ips': 1,
            'router_id': '',
            'routers': 5,
            'external_network_bridge': '',
            'interfaces': 9,
            'agent_mode': 'legacy',
            'handle_internal_only_routers': True,
            'use_namespaces': True,
            'ex_gw_ports': 5,
            'log_agent_heartbeats': False
        },
        'binary': 'neutron-l3-agent',
        'id': 'OVS-ed11ec68-e6e0-4c55-90f3-a217643309aa',
        'agent_type': 'L3 agent',
        'host': 'node-6.cisco.com',
        'load': 0,
        'started_at': datetime.datetime(2016, 5, 16, 13, 38, 25),
        'name': 'neutron-l3-agent',
        'description': None,
        'topic': 'l3_agent',
        'created_at': datetime.datetime(2016, 4, 17, 14, 8, 28)
    }
]
