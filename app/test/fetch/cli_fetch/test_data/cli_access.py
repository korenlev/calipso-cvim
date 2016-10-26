HOST = {
    "config": {
        "interfaces": 4,
        "log_agent_heartbeats": False,
        "gateway_external_network_id": "",
        "router_id": "",
        "interface_driver": "neutron.agent.linux.interface.OVSInterfaceDriver",
        "ex_gw_ports": 2,
        "routers": 2,
        "handle_internal_only_routers": True,
        "floating_ips": 1,
        "external_network_bridge": "",
        "use_namespaces": True,
        "agent_mode": "legacy"
    },
    "environment": "Mirantis-Liberty-Xiaocong",
    "host": "node-6.cisco.com",
    "host_type": [
        "Controller",
        "Network"
    ],
    "id": "node-6.cisco.com",
    "id_path": "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com",
    "name": "node-6.cisco.com",
    "name_path": "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com",
    "object_name": "node-6.cisco.com",
    "parent_id": "internal",
    "parent_type": "availability_zone",
    "services": {
        "nova-scheduler": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:01:10.000000"
        },
        "nova-consoleauth": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:01:54.000000"
        },
        "nova-conductor": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:01:45.000000"
        },
        "nova-cert": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:01:56.000000"
        }
    },
    "show_in_tree": True,
    "type": "host",
    "zone": "internal"
}

COMPUTE_HOST = {
    "environment": "Mirantis-Liberty-Xiaocong",
    "host": "node-5.cisco.com",
    "host_type": [
        "Compute"
    ],
    "id": "node-5.cisco.com",
    "id_path": "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/osdna-zone/node-5.cisco.com",
    "ip_address": "192.168.0.4",
    "name": "node-5.cisco.com",
    "name_path": "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/osdna-zone/node-5.cisco.com",
    "object_name": "node-5.cisco.com",
    "os_id": "1",
    "parent_id": "osdna-zone",
    "parent_type": "availability_zone",
    "services": {
        "nova-compute": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:01:42.000000"
        }
    },
    "show_in_tree": True,
    "type": "host",
    "zone": "osdna-zone"
}

COMMAND = "virsh list"
CACHED_COMMAND = "ssh -o StrictHostKeyChecking=no " + COMPUTE_HOST['id'] + " sudo " + COMMAND

RUN_RESULT = " Id    Name                           State\n----------------------------------------------------\n 2     instance-00000002              running\n 27    instance-0000001c              running\n 38    instance-00000026              running"

LINES_FOR_FIX = [
    "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952",
    "\t\t\t\t\t\t\tp_ff798dba-0",
    "\t\t\t\t\t\t\tv_public",
    "\t\t\t\t\t\t\tv_vrouter_pub",
    "br-fw-admin\t\t8000.005056ace897\tno\t\teno16777728",
    "br-mesh\t\t8000.005056acc9a2\tno\t\teno33554952.103",
    "br-mgmt\t\t8000.005056ace897\tno\t\teno16777728.101",
    "\t\t\t\t\t\t\tmgmt-conntrd",
    "\t\t\t\t\t\t\tv_management",
    "\t\t\t\t\t\t\tv_vrouter",
    "br-storage\t\t8000.005056ace897\tno\t\teno16777728.102"
]

FIXED_LINES = [
    "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952,p_ff798dba-0,v_public,v_vrouter_pub",
    "br-fw-admin\t\t8000.005056ace897\tno\t\teno16777728",
    "br-mesh\t\t8000.005056acc9a2\tno\t\teno33554952.103",
    "br-mgmt\t\t8000.005056ace897\tno\t\teno16777728.101,mgmt-conntrd,v_management,v_vrouter",
    "br-storage\t\t8000.005056ace897\tno\t\teno16777728.102"
]

LINE_FOR_PARSE = "br-ex\t\t8000.005056acc9a2\tno\t\teno33554952,p_ff798dba-0,v_public,v_vrouter_pub"
PARSED_LINE = {
    "bridge_id": "8000.005056acc9a2",
    "bridge_name": "br-ex",
    "interfaces": "eno33554952,p_ff798dba-0,v_public,v_vrouter_pub",
    "stp_enabled": "no"
}
HEADERS = ["bridge_name", "bridge_id", "stp_enabled", "interfaces"]
# functional test
