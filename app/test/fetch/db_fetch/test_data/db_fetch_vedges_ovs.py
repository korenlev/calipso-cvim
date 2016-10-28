VEDGES_FOLDER = {
    "create_object" : True,
    "environment" : "Mirantis-Liberty-Xiaocong",
    "id" : "node-6.cisco.com-vedges",
    "id_path" : "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-vedges",
    "name" : "vEdges",
    "name_path" : "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/vEdges",
    "object_name" : "vEdges",
    "parent_id" : "node-6.cisco.com",
    "parent_type" : "host",
    "show_in_tree" : True,
    "text" : "vEdges",
    "type" : "vedges_folder"
}
AGENT = [
    {
        'host': 'node-6.cisco.com',
        'admin_state_up': 1,
        'load': 0,
        'description': None,
        'agent_type': 'Open vSwitch agent',
        'binary': 'neutron-openvswitch-agent',
        'topic': 'N/A',
        'id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
        'configurations': '{"in_distributed_mode": false, "arp_responder_enabled": true, "tunneling_ip": "192.168.2.3", "devices": 22, "extensions": [], "l2_population": true, "tunnel_types": ["vxlan"], "log_agent_heartbeats": false, "enable_distributed_routing": false, "bridge_mappings": {"physnet1": "br-floating"}}',
    }
]
HOST = { 
    "config" : {
        "router_id" : "", 
        "ex_gw_ports" : 2, 
        "routers" : 2, 
        "agent_mode" : "legacy", 
        "interfaces" : 5, 
        "use_namespaces" : True, 
        "log_agent_heartbeats" : False, 
        "handle_internal_only_routers" : True, 
        "floating_ips" : 1, 
        "external_network_bridge" : "", 
        "interface_driver" : "neutron.agent.linux.interface.OVSInterfaceDriver", 
        "gateway_external_network_id" : ""
    }, 
    "environment" : "Mirantis-Liberty-Xiaocong", 
    "host" : "node-6.cisco.com", 
    "host_type" : [
        "Controller", 
        "Network"
    ], 
    "id" : "node-6.cisco.com", 
    "id_path" : "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com", 
    "name" : "node-6.cisco.com",
    "name_path" : "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com", 
    "object_name" : "node-6.cisco.com", 
    "parent_id" : "internal", 
    "parent_type" : "availability_zone", 
    "services" : {
        "nova-scheduler" : {
            "active" : True, 
            "available" : True, 
            "updated_at" : "2016-10-25T20:32:53.000000"
        }, 
        "nova-conductor" : {
            "active" : True, 
            "available" : True, 
            "updated_at" : "2016-10-25T20:32:41.000000"
        }, 
        "nova-consoleauth" : {
            "active" : True, 
            "available" : True, 
            "updated_at" : "2016-10-25T20:32:45.000000"
        }, 
        "nova-cert" : {
            "active" : True, 
            "available" : True, 
            "updated_at" : "2016-10-25T20:32:45.000000"
        }
    }, 
    "show_in_tree" : True, 
    "type" : "host", 
    "zone" : "internal"
}
WRONG_HOST = {
    "id": "node-6.cisco.com",
    "host_type":[

    ]
}
VSCTL_LINES = [
    "3b12f08e-4e13-4976-8da5-23314b268805",
    "    Bridge br-int",
    "        fail_mode: secure",
    "        Port \"qr-18f029db-77\"",
    "            tag: 105",
    "            Interface \"qr-18f029db-77\"",
    "                type: internal",
    "        Port \"tap16620a58-c4\"",
    "            tag: 6",
    "            Interface \"tap16620a58-c4\"",
    "                type: internal",
    "        Port \"tap702e9683-0c\"",
    "            tag: 118",
    "            Interface \"tap702e9683-0c\"",
    "                type: internal",
    "        Port int-br-floating",
    "            Interface int-br-floating",
    "                type: patch",
    "                options: {peer=phy-br-floating}",
    "        Port \"qg-be833afe-d5\"",
    "            tag: 2",
    "            Interface \"qg-be833afe-d5\"",
    "                type: internal",
    "        Port br-int",
    "            Interface br-int",
    "                type: internal",
    "        Port \"qg-63489f34-af\"",
    "            tag: 2",
    "            Interface \"qg-63489f34-af\"",
    "                type: internal",
    "        Port \"tap5f22f397-d8\"",
    "            tag: 3",
    "            Interface \"tap5f22f397-d8\"",
    "                type: internal",
    "        Port \"tap82d4992f-4d\"",
    "            tag: 5",
    "            Interface \"tap82d4992f-4d\"",
    "                type: internal",
    "        Port \"qr-bb9b8340-72\"",
    "            tag: 3",
    "            Interface \"qr-bb9b8340-72\"",
    "                type: internal",
    "        Port \"tapaf69959f-ef\"",
    "            tag: 105",
    "            Interface \"tapaf69959f-ef\"",
    "                type: internal",
    "        Port \"qr-3ff411a2-54\"",
    "            tag: 5",
    "            Interface \"qr-3ff411a2-54\"",
    "                type: internal",
    "        Port patch-tun",
    "            Interface patch-tun",
    "                type: patch",
    "                options: {peer=patch-int}",
    "        Port \"qr-8733cc5d-b3\"",
    "            tag: 4",
    "            Interface \"qr-8733cc5d-b3\"",
    "                type: internal",
    "        Port \"qg-2a1a5710-f4\"",
    "            tag: 2",
    "            Interface \"qg-2a1a5710-f4\"",
    "                type: internal",
    "        Port \"tap31c19fbe-5d\"",
    "            tag: 117",
    "            Interface \"tap31c19fbe-5d\"",
    "                type: internal",
    "        Port \"qr-ee6a402f-11\"",
    "            tag: 118",
    "            Interface \"qr-ee6a402f-11\"",
    "                type: internal",
    "        Port \"qg-e2f31c24-d0\"",
    "            tag: 2",
    "            Interface \"qg-e2f31c24-d0\"",
    "                type: internal",
    "        Port \"qr-a0f4d0f2-a1\"",
    "            tag: 117",
    "            Interface \"qr-a0f4d0f2-a1\"",
    "                type: internal",
    "        Port \"qr-b3e4ea8a-75\"",
    "            tag: 118",
    "            Interface \"qr-b3e4ea8a-75\"",
    "                type: internal",
    "        Port \"qr-f7b44150-99\"",
    "            tag: 1",
    "            Interface \"qr-f7b44150-99\"",
    "                type: internal",
    "        Port \"tapbf16c3ab-56\"",
    "            tag: 4",
    "            Interface \"tapbf16c3ab-56\"",
    "                type: internal",
    "        Port \"tapee8e5dbb-03\"",
    "            tag: 1",
    "            Interface \"tapee8e5dbb-03\"",
    "                type: internal",
    "        Port \"qg-57e65d34-3d\"",
    "            tag: 2",
    "            Interface \"qg-57e65d34-3d\"",
    "                type: internal",
    "        Port \"qr-bfa1d684-7c\"",
    "            tag: 105",
    "            Interface \"qr-bfa1d684-7c\"",
    "                type: internal",
    "    Bridge br-tun",
    "        fail_mode: secure",
    "        Port patch-int",
    "            Interface patch-int",
    "                type: patch",
    "                options: {peer=patch-tun}",
    "        Port \"vxlan-c0a80201\"",
    "            Interface \"vxlan-c0a80201\"",
    "                type: vxlan",
    "                options: {df_default=\"True\", in_key=flow, local_ip=\"192.168.2.3\", out_key=flow, remote_ip=\"192.168.2.1\"}",
    "        Port br-tun",
    "            Interface br-tun",
    "                type: internal",
    "        Port \"vxlan-c0a80202\"",
    "            Interface \"vxlan-c0a80202\"",
    "                type: vxlan",
    "                options: {df_default=\"True\", in_key=flow, local_ip=\"192.168.2.3\", out_key=flow, remote_ip=\"192.168.2.2\"}",
    "    Bridge br-floating",
    "        Port br-floating",
    "            Interface br-floating",
    "                type: internal",
    "        Port \"p_ff798dba-0\"",
    "            Interface \"p_ff798dba-0\"",
    "                type: internal",
    "        Port phy-br-floating",
    "            Interface phy-br-floating",
    "                type: patch",
    "                options: {peer=int-br-floating}",
    "    ovs_version: \"2.3.1\""
]

VERIFY_TAGS = {
    "qr-18f029db-77": "105",
    "tap16620a58-c4": "6",
    "tap702e9683-0c": "118",
    "tapaf69959f-ef": "105",
    "tapee8e5dbb-03": "1",
    "qg-57e65d34-3d": "2",
    "qr-bfa1d684-7c": "105"
}

PORTS_BEFORE_TAGS = {
    "br-floating": {
        "id": "14",
        "internal": True,
        "name": "br-floating"
    },
    "br-int": {
        "id": "3",
        "internal": True,
        "name": "br-int"
    },
    "br-tun": {
        "id": "13",
        "internal": True,
        "name": "br-tun"
    },
    "ovs-system": {
        "id": "0",
        "internal": True,
        "name": "ovs-system"
    },
    "p_ff798dba-0": {
        "id": "15",
        "internal": True,
        "name": "p_ff798dba-0"
    },
    "qg-2a1a5710-f4": {
        "id": "24",
        "internal": True,
        "name": "qg-2a1a5710-f4"
    },
    "qg-57e65d34-3d": {
        "id": "10",
        "internal": True,
        "name": "qg-57e65d34-3d"
    },
    "qg-63489f34-af": {
        "id": "8",
        "internal": True,
        "name": "qg-63489f34-af"
    },
    "qg-be833afe-d5": {
        "id": "22",
        "internal": True,
        "name": "qg-be833afe-d5"
    },
    "qg-e2f31c24-d0": {
        "id": "27",
        "internal": True,
        "name": "qg-e2f31c24-d0"
    },
    "qr-18f029db-77": {
        "id": "17",
        "internal": True,
        "name": "qr-18f029db-77"
    },
    "qr-3ff411a2-54": {
        "id": "7",
        "internal": True,
        "name": "qr-3ff411a2-54"
    },
    "qr-8733cc5d-b3": {
        "id": "2",
        "internal": True,
        "name": "qr-8733cc5d-b3"
    },
    "qr-a0f4d0f2-a1": {
        "id": "25",
        "internal": True,
        "name": "qr-a0f4d0f2-a1"
    },
    "qr-b3e4ea8a-75": {
        "id": "21",
        "internal": True,
        "name": "qr-b3e4ea8a-75"
    },
    "qr-bb9b8340-72": {
        "id": "1",
        "internal": True,
        "name": "qr-bb9b8340-72"
    },
    "qr-bfa1d684-7c": {
        "id": "26",
        "internal": True,
        "name": "qr-bfa1d684-7c"
    },
    "qr-ee6a402f-11": {
        "id": "23",
        "internal": True,
        "name": "qr-ee6a402f-11"
    },
    "qr-f7b44150-99": {
        "id": "4",
        "internal": True,
        "name": "qr-f7b44150-99"
    },
    "tap16620a58-c4": {
        "id": "16",
        "internal": True,
        "name": "tap16620a58-c4"
    },
    "tap31c19fbe-5d": {
        "id": "19",
        "internal": True,
        "name": "tap31c19fbe-5d"
    },
    "tap5f22f397-d8": {
        "id": "11",
        "internal": True,
        "name": "tap5f22f397-d8"
    },
    "tap702e9683-0c": {
        "id": "20",
        "internal": True,
        "name": "tap702e9683-0c"
    },
    "tap82d4992f-4d": {
        "id": "9",
        "internal": True,
        "name": "tap82d4992f-4d"
    },
    "tapaf69959f-ef": {
        "id": "18",
        "internal": True,
        "name": "tapaf69959f-ef"
    },
    "tapbf16c3ab-56": {
        "id": "5",
        "internal": True,
        "name": "tapbf16c3ab-56"
    },
    "tapee8e5dbb-03": {
        "id": "6",
        "internal": True,
        "name": "tapee8e5dbb-03"
    }
}
PORTS_AFTER_TAGS = {
    "br-floating": {
        "id": "14",
        "internal": True,
        "name": "br-floating"
    },
    "br-int": {
        "id": "3",
        "internal": True,
        "name": "br-int"
    },
    "br-tun": {
        "id": "13",
        "internal": True,
        "name": "br-tun"
    },
    "ovs-system": {
        "id": "0",
        "internal": True,
        "name": "ovs-system"
    },
    "p_ff798dba-0": {
        "id": "15",
        "internal": True,
        "name": "p_ff798dba-0"
    },
    "qg-2a1a5710-f4": {
        "id": "24",
        "internal": True,
        "name": "qg-2a1a5710-f4",
        "tag": "2"
    },
    "qg-57e65d34-3d": {
        "id": "10",
        "internal": True,
        "name": "qg-57e65d34-3d",
        "tag": "2"
    },
    "qg-63489f34-af": {
        "id": "8",
        "internal": True,
        "name": "qg-63489f34-af",
        "tag": "2"
    },
    "qg-be833afe-d5": {
        "id": "22",
        "internal": True,
        "name": "qg-be833afe-d5",
        "tag": "2"
    },
    "qg-e2f31c24-d0": {
        "id": "27",
        "internal": True,
        "name": "qg-e2f31c24-d0",
        "tag": "2"
    },
    "qr-18f029db-77": {
        "id": "17",
        "internal": True,
        "name": "qr-18f029db-77",
        "tag": "105"
    },
    "qr-3ff411a2-54": {
        "id": "7",
        "internal": True,
        "name": "qr-3ff411a2-54",
        "tag": "5"
    },
    "qr-8733cc5d-b3": {
        "id": "2",
        "internal": True,
        "name": "qr-8733cc5d-b3",
        "tag": "4"
    },
    "qr-a0f4d0f2-a1": {
        "id": "25",
        "internal": True,
        "name": "qr-a0f4d0f2-a1",
        "tag": "117"
    },
    "qr-b3e4ea8a-75": {
        "id": "21",
        "internal": True,
        "name": "qr-b3e4ea8a-75",
        "tag": "118"
    },
    "qr-bb9b8340-72": {
        "id": "1",
        "internal": True,
        "name": "qr-bb9b8340-72",
        "tag": "3"
    },
    "qr-bfa1d684-7c": {
        "id": "26",
        "internal": True,
        "name": "qr-bfa1d684-7c",
        "tag": "105"
    },
    "qr-ee6a402f-11": {
        "id": "23",
        "internal": True,
        "name": "qr-ee6a402f-11",
        "tag": "118"
    },
    "qr-f7b44150-99": {
        "id": "4",
        "internal": True,
        "name": "qr-f7b44150-99",
        "tag": "1"
    },
    "tap16620a58-c4": {
        "id": "16",
        "internal": True,
        "name": "tap16620a58-c4",
        "tag": "6"
    },
    "tap31c19fbe-5d": {
        "id": "19",
        "internal": True,
        "name": "tap31c19fbe-5d",
        "tag": "117"
    },
    "tap5f22f397-d8": {
        "id": "11",
        "internal": True,
        "name": "tap5f22f397-d8",
        "tag": "3"
    },
    "tap702e9683-0c": {
        "id": "20",
        "internal": True,
        "name": "tap702e9683-0c",
        "tag": "118"
    },
    "tap82d4992f-4d": {
        "id": "9",
        "internal": True,
        "name": "tap82d4992f-4d",
        "tag": "5"
    },
    "tapaf69959f-ef": {
        "id": "18",
        "internal": True,
        "name": "tapaf69959f-ef",
        "tag": "105"
    },
    "tapbf16c3ab-56": {
        "id": "5",
        "internal": True,
        "name": "tapbf16c3ab-56",
        "tag": "4"
    },
    "tapee8e5dbb-03": {
        "id": "6",
        "internal": True,
        "name": "tapee8e5dbb-03",
        "tag": "1"
    }
}
DPCTL_LINES = [
    "system@ovs-system:",
    "\tlookups: hit:14039304 missed:35687906 lost:0",
    "\tflows: 4",
    "\tmasks: hit:95173613 total:2 hit/pkt:1.91",
    "\tport 0: ovs-system (internal)",
    "\tport 1: qr-bb9b8340-72 (internal)",
    "\tport 2: qr-8733cc5d-b3 (internal)",
    "\tport 3: br-int (internal)",
    "\tport 4: qr-f7b44150-99 (internal)",
    "\tport 5: tapbf16c3ab-56 (internal)",
    "\tport 6: tapee8e5dbb-03 (internal)",
    "\tport 7: qr-3ff411a2-54 (internal)",
    "\tport 8: qg-63489f34-af (internal)",
    "\tport 9: tap82d4992f-4d (internal)",
    "\tport 10: qg-57e65d34-3d (internal)",
    "\tport 11: tap5f22f397-d8 (internal)",
    "\tport 12: vxlan_sys_4789 (vxlan: df_default=false, ttl=0)",
    "\tport 13: br-tun (internal)",
    "\tport 14: br-floating (internal)",
    "\tport 15: p_ff798dba-0 (internal)",
    "\tport 16: tap16620a58-c4 (internal)",
    "\tport 17: qr-18f029db-77 (internal)",
    "\tport 18: tapaf69959f-ef (internal)",
    "\tport 19: tap31c19fbe-5d (internal)",
    "\tport 20: tap702e9683-0c (internal)",
    "\tport 21: qr-b3e4ea8a-75 (internal)",
    "\tport 22: qg-be833afe-d5 (internal)",
    "\tport 23: qr-ee6a402f-11 (internal)",
    "\tport 24: qg-2a1a5710-f4 (internal)",
    "\tport 25: qr-a0f4d0f2-a1 (internal)",
    "\tport 26: qr-bfa1d684-7c (internal)",
    "\tport 27: qg-e2f31c24-d0 (internal)"
]
DOC_TO_GET_OVERLAY = {
    'name': 'node-6.cisco.com-OVS',
    'host': 'node-6.cisco.com',
    'load': 0,
    'agent_type': 'Open vSwitch agent',
    'configurations': {
        'tunnel_types': ['vxlan'],
        'tunneling_ip': '192.168.2.3',
        'log_agent_heartbeats': False,
        'in_distributed_mode': False,
        'arp_responder_enabled': True,
        'bridge_mappings': {
            'physnet1': 'br-floating'
        },
        'devices': 22,
        'extensions': [],
        'enable_distributed_routing': False,
        'l2_population': True
    },
    'binary': 'neutron-openvswitch-agent',
    'topic': 'N/A',
    'id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
    'ports': {
    "br-floating": {
        "id": "14",
        "internal": True,
        "name": "br-floating"
    },
    "br-int": {
        "id": "3",
        "internal": True,
        "name": "br-int"
    },
    "br-tun": {
        "id": "13",
        "internal": True,
        "name": "br-tun"
    },
    "ovs-system": {
        "id": "0",
        "internal": True,
        "name": "ovs-system"
    },
    "p_ff798dba-0": {
        "id": "15",
        "internal": True,
        "name": "p_ff798dba-0"
    },
    "qg-2a1a5710-f4": {
        "id": "24",
        "internal": True,
        "name": "qg-2a1a5710-f4",
        "tag": "2"
    },
    "qg-57e65d34-3d": {
        "id": "10",
        "internal": True,
        "name": "qg-57e65d34-3d",
        "tag": "2"
    },
    "qg-63489f34-af": {
        "id": "8",
        "internal": True,
        "name": "qg-63489f34-af",
        "tag": "2"
    },
    "qg-be833afe-d5": {
        "id": "22",
        "internal": True,
        "name": "qg-be833afe-d5",
        "tag": "2"
    },
    "qg-e2f31c24-d0": {
        "id": "27",
        "internal": True,
        "name": "qg-e2f31c24-d0",
        "tag": "2"
    },
    "qr-18f029db-77": {
        "id": "17",
        "internal": True,
        "name": "qr-18f029db-77",
        "tag": "105"
    },
    "qr-3ff411a2-54": {
        "id": "7",
        "internal": True,
        "name": "qr-3ff411a2-54",
        "tag": "5"
    },
    "qr-8733cc5d-b3": {
        "id": "2",
        "internal": True,
        "name": "qr-8733cc5d-b3",
        "tag": "4"
    },
    "qr-a0f4d0f2-a1": {
        "id": "25",
        "internal": True,
        "name": "qr-a0f4d0f2-a1",
        "tag": "117"
    },
    "qr-b3e4ea8a-75": {
        "id": "21",
        "internal": True,
        "name": "qr-b3e4ea8a-75",
        "tag": "118"
    },
    "qr-bb9b8340-72": {
        "id": "1",
        "internal": True,
        "name": "qr-bb9b8340-72",
        "tag": "3"
    },
    "qr-bfa1d684-7c": {
        "id": "26",
        "internal": True,
        "name": "qr-bfa1d684-7c",
        "tag": "105"
    },
    "qr-ee6a402f-11": {
        "id": "23",
        "internal": True,
        "name": "qr-ee6a402f-11",
        "tag": "118"
    },
    "qr-f7b44150-99": {
        "id": "4",
        "internal": True,
        "name": "qr-f7b44150-99",
        "tag": "1"
    },
    "tap16620a58-c4": {
        "id": "16",
        "internal": True,
        "name": "tap16620a58-c4",
        "tag": "6"
    },
    "tap31c19fbe-5d": {
        "id": "19",
        "internal": True,
        "name": "tap31c19fbe-5d",
        "tag": "117"
    },
    "tap5f22f397-d8": {
        "id": "11",
        "internal": True,
        "name": "tap5f22f397-d8",
        "tag": "3"
    },
    "tap702e9683-0c": {
        "id": "20",
        "internal": True,
        "name": "tap702e9683-0c",
        "tag": "118"
    },
    "tap82d4992f-4d": {
        "id": "9",
        "internal": True,
        "name": "tap82d4992f-4d",
        "tag": "5"
    },
    "tapaf69959f-ef": {
        "id": "18",
        "internal": True,
        "name": "tapaf69959f-ef",
        "tag": "105"
    },
    "tapbf16c3ab-56": {
        "id": "5",
        "internal": True,
        "name": "tapbf16c3ab-56",
        "tag": "4"
    },
    "tapee8e5dbb-03": {
        "id": "6",
        "internal": True,
        "name": "tapee8e5dbb-03",
        "tag": "1"
    }
},
    'admin_state_up': 1,
    'description': None
}

tunnel_ports = {
    "br-tun": {
        "interface": "br-tun",
        "name": "br-tun",
        "type": "internal"
    },
    "patch-int": {
        "interface": "patch-int",
        "name": "patch-int",
        "options": {
            "peer": "patch-tun"
        },
        "type": "patch"
    },
    "vxlan-c0a80201": {
        "interface": "vxlan-c0a80201",
        "name": "vxlan-c0a80201",
        "options": {
            "df_default": "True",
            "in_key": "flow",
            "local_ip": "192.168.2.3",
            "out_key": "flow",
            "remote_ip": "192.168.2.1"
        },
        "type": "vxlan"
    },
    "vxlan-c0a80202": {
        "interface": "vxlan-c0a80202",
        "name": "vxlan-c0a80202",
        "options": {
            "df_default": "True",
            "in_key": "flow",
            "local_ip": "192.168.2.3",
            "out_key": "flow",
            "remote_ip": "192.168.2.2"
        },
        "type": "vxlan"
    }
}

# functional test
INPUT = "node-6.cisco.com-vedges"
OUTPUT = {
    'load': 0,
    'id': '1764430c-c09e-4717-86fa-c04350b1fcbb',
    'ports':
        {
            'qr-a0f4d0f2-a1': {
                'internal': True,
                'tag': '117',
                'id': '25',
                'name': 'qr-a0f4d0f2-a1'
            },
            'qr-18f029db-77': {
                'internal': True,
                 'tag': '105',
                'id': '17',
                'name': 'qr-18f029db-77'
            },
            'qg-2a1a5710-f4': {
                'internal': True,
                'tag': '2',
                'id': '24',
                'name': 'qg-2a1a5710-f4'
            },
            'qg-e2f31c24-d0': {
                'internal': True,
                'tag': '2',
                'id': '27',
                'name': 'qg-e2f31c24-d0'
            },
            'tapbf16c3ab-56': {
                'internal': True,
                'tag': '4',
                'id': '5',
                'name': 'tapbf16c3ab-56'
            },
            'tap5f22f397-d8': {
                'internal': True,
                'tag': '3',
                'id': '11',
                'name': 'tap5f22f397-d8'
            },
            'tap702e9683-0c': {
                'internal': True,
                'tag': '118',
                'id': '20',
                'name': 'tap702e9683-0c'
            },
            'qr-f7b44150-99': {
                'internal': True,
                'tag': '1',
                'id': '4',
                'name': 'qr-f7b44150-99'
            },
            'tap82d4992f-4d': {
                'internal': True,
                'tag': '5',
                'id': '9',
                'name': 'tap82d4992f-4d'
            },
            'qg-be833afe-d5': {
                'internal': True,
                'tag': '2',
                'id': '22',
                'name': 'qg-be833afe-d5'
            },
            'qg-57e65d34-3d': {
                'internal': True,
                'tag': '2',
                'id': '10',
                'name': 'qg-57e65d34-3d'
            },
            'qr-b3e4ea8a-75': {
                'internal': True,
                'tag': '118',
                'id': '21',
                'name': 'qr-b3e4ea8a-75'
            },
            'br-int': {
                'internal': True,
                'id': '3',
                'name': 'br-int'
            },
            'qg-63489f34-af': {
                'internal': True,
                'tag': '2',
                'id': '8',
                'name': 'qg-63489f34-af'
            },
            'qr-3ff411a2-54': {
                'internal': True,
                'tag': '5',
                'id': '7',
                'name': 'qr-3ff411a2-54'
            },
            'br-floating': {
                'internal': True,
                'id': '14',
                'name': 'br-floating'
            },
            'ovs-system': {
                'internal': True,
                'id': '0',
                'name': 'ovs-system'
            },
            'tapee8e5dbb-03': {
                'internal': True,
                'tag': '1',
                'id': '6',
                'name': 'tapee8e5dbb-03'
            },
            'tap31c19fbe-5d': {
                'internal': True,
                'tag': '117',
                'id': '19',
                'name': 'tap31c19fbe-5d'
            },
            'qr-bfa1d684-7c': {
                'internal': True,
                'tag': '105',
                'id': '26',
                'name': 'qr-bfa1d684-7c'
            },
            'qr-bb9b8340-72': {
                'internal': True,
                'tag': '3',
                'id': '1',
                'name': 'qr-bb9b8340-72'
            },
            'tapaf69959f-ef': {
                'internal': True,
                'tag': '105',
                'id': '18',
                'name': 'tapaf69959f-ef'
            },
            'qr-8733cc5d-b3': {
                'internal': True,
                'tag': '4',
                'id': '2',
                'name': 'qr-8733cc5d-b3'
            },
            'tap16620a58-c4': {
                'internal': True,
                'tag': '6',
                'id': '16',
                'name': 'tap16620a58-c4'
            },
            'p_ff798dba-0': {
                'internal': True,
                'id': '15',
                'name': 'p_ff798dba-0'
            },
            'br-tun': {
                'internal': True,
                'id': '13',
                'name': 'br-tun'
            },
            'qr-ee6a402f-11': {
                'internal': True,
                'tag': '118',
                'id': '23',
                'name': 'qr-ee6a402f-11'
            }
        },
    'admin_state_up': 1,
    'tunnel_ports': {
        'vxlan-c0a80201':
            {
                'options': {
                    'df_default': 'True',
                    'remote_ip': '192.168.2.1',
                    'local_ip': '192.168.2.3',
                    'in_key': 'flow',
                    'out_key': 'flow'
                },
                'type': 'vxlan',
                'name': 'vxlan-c0a80201',
                'interface': 'vxlan-c0a80201'
            },
        'br-tun': {
            'type': 'internal',
            'name': 'br-tun',
            'interface': 'br-tun'
        },
        'patch-int': {
            'options': {
                'peer': 'patch-tun'
            },
            'type': 'patch',
            'name': 'patch-int',
            'interface': 'patch-int'
        },
        'vxlan-c0a80202': {
            'options': {
                'df_default': 'True',
                'remote_ip': '192.168.2.2',
                'local_ip': '192.168.2.3',
                'in_key': 'flow',
                'out_key': 'flow'
            },
            'type': 'vxlan',
            'name': 'vxlan-c0a80202',
            'interface': 'vxlan-c0a80202'
        }
    },
    'agent_type': 'Open vSwitch agent',
    'binary': 'neutron-openvswitch-agent',
    'configurations': {
        'bridge_mappings': {
            'physnet1': 'br-floating'
        },
        'l2_population': True,
        'enable_distributed_routing': False,
        'extensions': [],
        'log_agent_heartbeats': False,
        'tunnel_types': ['vxlan'],
        'arp_responder_enabled': True,
        'in_distributed_mode': False,
        'tunneling_ip': '192.168.2.3',
        'devices': 22}
    ,
    'host': 'node-6.cisco.com',
    'topic': 'N/A',
    'description': None,
    'name': 'node-6.cisco.com-OVS'
}


