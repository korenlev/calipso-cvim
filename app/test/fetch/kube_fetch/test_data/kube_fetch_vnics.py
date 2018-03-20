from test.fetch.kube_fetch.test_data.kube_access import HOST_DOC

HOST_DOC = HOST_DOC.copy()
HOST_DOC['interfaces'] = {
    "vethd8ade2d8": {
        "lines": [
            "7: vethd8ade2d8@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue master cni0 state UP mode DEFAULT group default ",
            "    link/ether 66:3d:dc:96:6d:a1 brd ff:ff:ff:ff:ff:ff link-netnsid 0"
        ],
        "id": "vethd8ade2d8",
        "mac_address": "66:3d:dc:96:6d:a1",
        "index": "7",
        "state": "UP",
        "mtu": "1450"
    },
    "docker0": {
        "lines": [
            "4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default ",
            "    link/ether 02:42:c9:9c:d7:5d brd ff:ff:ff:ff:ff:ff"
        ],
        "id": "docker0",
        "mac_address": "02:42:c9:9c:d7:5d",
        "index": "4",
        "state": "DOWN",
        "mtu": "1500"
    },
}
