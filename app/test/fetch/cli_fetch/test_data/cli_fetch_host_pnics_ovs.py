PNICS_FOLDER_ID = "node-6.cisco.com-pnics"
HOST_ID = "node-6.cisco.com"

NETWORK_NODE = {
    "host_type": [
        "Controller",
        "Network"
    ],
    "id": "node-6.cisco.com"
}

WRONG_NODE = {
    "host_type": [
            "Controller"
        ]
}

INTERFACE_LINES = [
    "lrwxrwxrwx 1 root 0 Jul  5 17:17 eno16777728 -> ../../devices/0000:02:00.0/net/eno16777728",
    "lrwxrwxrwx 1 root 0 Jul  5 17:17 eno33554952 -> ../../devices/0000:02:01.0/net/eno33554952"
]

INTERFACE_NAMES = ["eno16777728", "eno33554952"]

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

INTERFACES_GET_RESULTS = [INTERFACE]

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
