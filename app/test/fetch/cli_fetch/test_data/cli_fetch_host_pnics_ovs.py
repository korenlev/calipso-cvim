PNICS_FOLDER = {
    "create_object": True,
    "environment": "Mirantis-Liberty-Xiaocong",
    "id": "node-6.cisco.com-pnics",
    "id_path": "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/internal/node-6.cisco.com/node-6.cisco.com-pnics",
    "name": "pNICs",
    "name_path": "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/internal/node-6.cisco.com/pNICs",
    "object_name": "pNICs",
    "parent_id": "node-6.cisco.com",
    "parent_type": "host",
    "show_in_tree": True,
    "text": "pNICs",
    "type": "pnics_folder"
}

NETWORK_NODE = {
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

WRONG_NODE = {
    "host_type": [
            "Controller"
        ]
}

INTERFACES_NAMES = [
    "eno16777728",
    "eno33554952",
    "eno33554952.103@eno33554952",
    "eno16777728.101@eno16777728",
    "eno16777728.102@eno16777728"
]

IFCONFIG_CM_RESULT = [
    "eno16777728 Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97  ",
    "          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1",
    "          RX packets:409056348 errors:0 dropped:0 overruns:0 frame:0",
    "          TX packets:293898173 errors:0 dropped:0 overruns:0 carrier:0",
    "          collisions:0 txqueuelen:1000 ",
    "          RX bytes:103719003730 (103.7 GB)  TX bytes:165090993470 (165.0 GB)",
    ""
]

RAW_INTERFACE = {
    "host": "node-6.cisco.com",
    "lines": [],
    "local_name": "eno16777728",
    "name": "eno16777728"
}

INTERFACE_FOR_SET = {
    "host": "node-6.cisco.com",
    "id": "eno16777728-00:50:56:ac:e8:97",
    "lines": [
        "Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97",
        "UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1",
        "RX packets:409135553 errors:0 dropped:0 overruns:0 frame:0",
        "TX packets:293954493 errors:0 dropped:0 overruns:0 carrier:0",
        "collisions:0 txqueuelen:1000",
        "RX bytes:103738298160 (103.7 GB)  TX bytes:165123015807 (165.1 GB)",
        ""
    ],
    "local_name": "eno16777728",
    "mac_address": "00:50:56:ac:e8:97",
    "name": "eno16777728"
}

INTERFACE = {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97\nUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\nRX packets:408989052 errors:0 dropped:0 overruns:0 frame:0\nTX packets:293849880 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:1000\nRX bytes:103702814216 (103.7 GB)  TX bytes:165063440009 (165.0 GB)\n",
        "host": "node-6.cisco.com",
        "id": "eno16777728-00:50:56:ac:e8:97",
        "local_name": "eno16777728",
        "mac_address": "00:50:56:ac:e8:97",
        "name": "eno16777728"
    }

MAC_ADDRESS_LINE = "eno16777728 Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97  "
MAC_ADDRESS = "00:50:56:ac:e8:97"
IPV6_ADDRESS_LINE = "          inet6 addr: fe80::f816:3eff:fea1:eb73/64 Scope:Link"
IPV6_ADDRESS = "fe80::f816:3eff:fea1:eb73/64"
IPV4_ADDRESS_LINE = "          inet addr:172.16.13.2  Bcast:172.16.13.255  Mask:255.255.255.0"
IPV4_ADDRESS = "172.16.13.2"

ETHTOOL_RESULT = [
    "Settings for eno16777728:",
    "\tSupported ports: [ TP ]",
    "\tSupported link modes:   10baseT/Half 10baseT/Full ",
    "\t                        100baseT/Half 100baseT/Full ",
    "\t                        1000baseT/Full ",
    "\tSupported pause frame use: No",
    "\tSupports auto-negotiation: Yes",
    "\tAdvertised link modes:  10baseT/Half 10baseT/Full ",
    "\t                        100baseT/Half 100baseT/Full ",
    "\t                        1000baseT/Full ",
    "\tAdvertised pause frame use: No",
    "\tAdvertised auto-negotiation: Yes",
    "\tSpeed: 1000Mb/s",
    "\tDuplex: Full",
    "\tPort: Twisted Pair",
    "\tPHYAD: 0",
    "\tTransceiver: internal",
    "\tAuto-negotiation: on",
    "\tMDI-X: off (auto)",
    "\tSupports Wake-on: d",
    "\tWake-on: d",
    "\tCurrent message level: 0x00000007 (7)",
    "\t\t\t       drv probe link",
    "\tLink detected: yes"
]

TEST_ATTRIBUTE1 = "Supported ports"
EXPECTED_VALUE1 = "[ TP ]"
TEST_ATTRIBUTE2 = "Supported link modes"
EXPECTED_VALUE2 = [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ]
# functional test
INPUT = "node-6.cisco.com-pnics"
OUTPUT = [
    {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97\nUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\nRX packets:408989052 errors:0 dropped:0 overruns:0 frame:0\nTX packets:293849880 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:1000\nRX bytes:103702814216 (103.7 GB)  TX bytes:165063440009 (165.0 GB)\n",
        "host": "node-6.cisco.com",
        "id": "eno16777728-00:50:56:ac:e8:97",
        "local_name": "eno16777728",
        "mac_address": "00:50:56:ac:e8:97",
        "name": "eno16777728"
    },
    {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:c9:a2\nUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\nRX packets:44120811 errors:0 dropped:1 overruns:0 frame:0\nTX packets:13995981 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:1000\nRX bytes:5101624086 (5.1 GB)  TX bytes:1756695018 (1.7 GB)\n",
        "host": "node-6.cisco.com",
        "id": "eno33554952-00:50:56:ac:c9:a2",
        "local_name": "eno33554952",
        "mac_address": "00:50:56:ac:c9:a2",
        "name": "eno33554952"
    },
    {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "IPv6 Address": "addr:",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:c9:a2\ninet6 addr: fe80::250:56ff:feac:c9a2/64 Scope:Link\nUP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1\nRX packets:4216095 errors:0 dropped:0 overruns:0 frame:0\nTX packets:4233921 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:1074595656 (1.0 GB)  TX bytes:1138534482 (1.1 GB)\n",
        "host": "node-6.cisco.com",
        "id": "eno33554952.103@eno33554952-00:50:56:ac:c9:a2",
        "local_name": "eno33554952.103@eno33554952",
        "mac_address": "00:50:56:ac:c9:a2",
        "name": "eno33554952.103@eno33554952"
    },
    {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "IPv6 Address": "addr:",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97\ninet6 addr: fe80::250:56ff:feac:e897/64 Scope:Link\nUP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1\nRX packets:163378685 errors:0 dropped:0 overruns:0 frame:0\nTX packets:165076981 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:40222427817 (40.2 GB)  TX bytes:50062912587 (50.0 GB)\n",
        "host": "node-6.cisco.com",
        "id": "eno16777728.101@eno16777728-00:50:56:ac:e8:97",
        "local_name": "eno16777728.101@eno16777728",
        "mac_address": "00:50:56:ac:e8:97",
        "name": "eno16777728.101@eno16777728"
    },
    {
        "Advertised auto-negotiation": "Yes",
        "Advertised link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Advertised pause frame use": "No",
        "Auto-negotiation": "on",
        "Current message level": [
            "0x00000007 (7)",
            "drv probe link"
        ],
        "Duplex": "Full",
        "IPv6 Address": "addr:",
        "Link detected": "yes",
        "MDI-X": "off (auto)",
        "PHYAD": "0",
        "Port": "Twisted Pair",
        "Speed": "1000Mb/s",
        "Supported link modes": [
            "10baseT/Half 10baseT/Full",
            "100baseT/Half 100baseT/Full",
            "1000baseT/Full"
        ],
        "Supported pause frame use": "No",
        "Supported ports": "[ TP ]",
        "Supports Wake-on": "d",
        "Supports auto-negotiation": "Yes",
        "Transceiver": "internal",
        "Wake-on": "d",
        "data": "Link encap:Ethernet  HWaddr 00:50:56:ac:e8:97\ninet6 addr: fe80::250:56ff:feac:e897/64 Scope:Link\nUP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1\nRX packets:187 errors:0 dropped:0 overruns:0 frame:0\nTX packets:219 errors:0 dropped:0 overruns:0 carrier:0\ncollisions:0 txqueuelen:0\nRX bytes:15480 (15.4 KB)  TX bytes:20654 (20.6 KB)\n",
        "host": "node-6.cisco.com",
        "id": "eno16777728.102@eno16777728-00:50:56:ac:e8:97",
        "local_name": "eno16777728.102@eno16777728",
        "mac_address": "00:50:56:ac:e8:97",
        "name": "eno16777728.102@eno16777728"
    }
]