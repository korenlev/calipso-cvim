VEDGES_FOLDER = {
    "create_object" : True,
    "environment" : "Devstack-VPP-2",
    "id" : "ubuntu0-vedges",
    "id_path" : "/Devstack-VPP-2/Devstack-VPP-2-regions/RegionOne/RegionOne-availability_zones/nova/ubuntu0/ubuntu0-vedges",
    "name" : "vEdges",
    "name_path" : "/Devstack-VPP-2/Regions/RegionOne/Availability Zones/nova/ubuntu0/vEdges",
    "object_name" : "vEdges",
    "parent_id" : "ubuntu0",
    "parent_type" : "host",
    "show_in_tree" : True,
    "text" : "vEdges",
    "type" : "vedges_folder"
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
WRONG_HOST = {
    "host_type": [

    ]
}
VERSION = [
    "vpp v16.09-rc0~157-g203c632 built by localadmin on ubuntu0 at Sun Jun 26 16:35:15 PDT 2016\n"
]
INTERFACES = [
    "              Name               Idx       State          Counter          Count     ",
    "TenGigabitEthernetc/0/0           5         up       rx packets                502022",
    "                                                     rx bytes               663436206",
    "                                                     tx packets                 81404",
    "                                                     tx bytes                 6366378",
    "                                                     drops                       1414",
    "                                                     punts                          1",
    "                                                     rx-miss                    64525",
    "TenGigabitEthernetd/0/0           6        down      ",
    "VirtualEthernet0/0/0              7         up       tx packets                 31496",
    "                                                     tx bytes                 2743185",
    "VirtualEthernet0/0/1              8         up       tx packets                 31511",
    "                                                     tx bytes                 2748315",
    "VirtualEthernet0/0/2              9         up       rx packets                 20506",
    "                                                     rx bytes                 1410466",
    "                                                     tx packets                172021",
    "                                                     tx bytes               219009458",
    "                                                     drops                       3686",
    "VirtualEthernet0/0/3              10        up       tx packets                 28911",
    "                                                     tx bytes                 2298211",
    "VirtualEthernet0/0/4              11        up       tx packets                 23832",
    "                                                     tx bytes                 1816600",
    "VirtualEthernet0/0/5              12        up       tx packets                 28911",
    "                                                     tx bytes                 2298211",
    "VirtualEthernet0/0/6              13        up       tx packets                 23832",
    "                                                     tx bytes                 1816600",
    "VirtualEthernet0/0/7              14        up       tx packets                 21698",
    "                                                     tx bytes                 1574542",
    "VirtualEthernet0/0/8              15        up       tx packets                 21698",
    "                                                     tx bytes                 1574542",
    "local0                            0        down      ",
    "pg/stream-0                       1        down      ",
    "pg/stream-1                       2        down      ",
    "pg/stream-2                       3        down      ",
    "pg/stream-3                       4        down      "
]
PORTS = {
    "TenGigabitEthernetc/0/0": {
        "id": "5",
        "name": "TenGigabitEthernetc/0/0",
        "state": "up"
    },
    "TenGigabitEthernetd/0/0": {
        "id": "6",
        "name": "TenGigabitEthernetd/0/0",
        "state": "down"
    },
    "VirtualEthernet0/0/0": {
        "id": "7",
        "name": "VirtualEthernet0/0/0",
        "state": "up"
    },
    "VirtualEthernet0/0/1": {
        "id": "8",
        "name": "VirtualEthernet0/0/1",
        "state": "up"
    },
    "VirtualEthernet0/0/2": {
        "id": "9",
        "name": "VirtualEthernet0/0/2",
        "state": "up"
    },
    "VirtualEthernet0/0/3": {
        "id": "10",
        "name": "VirtualEthernet0/0/3",
        "state": "up"
    },
    "VirtualEthernet0/0/4": {
        "id": "11",
        "name": "VirtualEthernet0/0/4",
        "state": "up"
    },
    "VirtualEthernet0/0/5": {
        "id": "12",
        "name": "VirtualEthernet0/0/5",
        "state": "up"
    },
    "VirtualEthernet0/0/6": {
        "id": "13",
        "name": "VirtualEthernet0/0/6",
        "state": "up"
    },
    "VirtualEthernet0/0/7": {
        "id": "14",
        "name": "VirtualEthernet0/0/7",
        "state": "up"
    },
    "VirtualEthernet0/0/8": {
        "id": "15",
        "name": "VirtualEthernet0/0/8",
        "state": "up"
    },
    "local0": {
        "id": "0",
        "name": "local0",
        "state": "down"
    },
    "pg/stream-0": {
        "id": "1",
        "name": "pg/stream-0",
        "state": "down"
    },
    "pg/stream-1": {
        "id": "2",
        "name": "pg/stream-1",
        "state": "down"
    },
    "pg/stream-2": {
        "id": "3",
        "name": "pg/stream-2",
        "state": "down"
    },
    "pg/stream-3": {
        "id": "4",
        "name": "pg/stream-3",
        "state": "down"
    }
}
# functional test
INPUT = "ubuntu0-vedges"
OUTPUT = [
    {
        "agent_type": "VPP",
        "binary": "vpp v16.09-rc0~157-g203c632",
        "host": "ubuntu0",
        "id": "ubuntu0-VPP",
        "name": "VPP-ubuntu0",
        "ports": {
            "TenGigabitEthernetc/0/0": {
                "id": "5",
                "name": "TenGigabitEthernetc/0/0",
                "state": "up"
            },
            "TenGigabitEthernetd/0/0": {
                "id": "6",
                "name": "TenGigabitEthernetd/0/0",
                "state": "down"
            },
            "VirtualEthernet0/0/0": {
                "id": "7",
                "name": "VirtualEthernet0/0/0",
                "state": "up"
            },
            "VirtualEthernet0/0/1": {
                "id": "8",
                "name": "VirtualEthernet0/0/1",
                "state": "up"
            },
            "VirtualEthernet0/0/2": {
                "id": "9",
                "name": "VirtualEthernet0/0/2",
                "state": "up"
            },
            "VirtualEthernet0/0/3": {
                "id": "10",
                "name": "VirtualEthernet0/0/3",
                "state": "up"
            },
            "VirtualEthernet0/0/4": {
                "id": "11",
                "name": "VirtualEthernet0/0/4",
                "state": "up"
            },
            "VirtualEthernet0/0/5": {
                "id": "12",
                "name": "VirtualEthernet0/0/5",
                "state": "up"
            },
            "VirtualEthernet0/0/6": {
                "id": "13",
                "name": "VirtualEthernet0/0/6",
                "state": "up"
            },
            "VirtualEthernet0/0/7": {
                "id": "14",
                "name": "VirtualEthernet0/0/7",
                "state": "up"
            },
            "VirtualEthernet0/0/8": {
                "id": "15",
                "name": "VirtualEthernet0/0/8",
                "state": "up"
            },
            "local0": {
                "id": "0",
                "name": "local0",
                "state": "down"
            },
            "pg/stream-0": {
                "id": "1",
                "name": "pg/stream-0",
                "state": "down"
            },
            "pg/stream-1": {
                "id": "2",
                "name": "pg/stream-1",
                "state": "down"
            },
            "pg/stream-2": {
                "id": "3",
                "name": "pg/stream-2",
                "state": "down"
            },
            "pg/stream-3": {
                "id": "4",
                "name": "pg/stream-3",
                "state": "down"
            }
        }
    }
]