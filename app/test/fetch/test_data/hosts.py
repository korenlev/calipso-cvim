HOSTS = [
            {
                "config": {
                    "dhcp_driver": "neutron.agent.linux.dhcp.Dnsmasq",
                    "dhcp_lease_duration": 120,
                    "networks": 5,
                    "ports": 13,
                    "subnets": 5,
                    "use_namespaces": True
                },
                "host": "node-14",
                "host_type": [
                    "Controller",
                    "Network"
                ],
                "id": "node-14",
                "name": "node-14",
                "parent_id": "internal",
                "parent_type": "availability_zone",
                "services": {
                    "nova-cert": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:12.000000"
                    },
                    "nova-conductor": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:10.000000"
                    },
                    "nova-consoleauth": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:10.000000"
                    },
                    "nova-scheduler": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:06.000000"
                    }
                },
                "zone": "internal"
            },
            {
                "host": "node-23",
                "host_type": [
                    "Compute"
                ],
                "id": "node-23",
                "ip_address": "192.168.100.6",
                "name": "node-23",
                "os_id": "4",
                "parent_id": "nova",
                "parent_type": "availability_zone",
                "services": {
                    "nova-compute": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:06.000000"
                    }
                },
                "zone": "nova"
            },
            {
                "host": "node-25",
                "host_type": [
                    "Compute"
                ],
                "id": "node-25",
                "ip_address": "192.168.100.10",
                "name": "node-25",
                "os_id": "5",
                "parent_id": "nova",
                "parent_type": "availability_zone",
                "services": {
                    "nova-compute": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-17T23:25:11.000000"
                    }
                },
                "zone": "nova"
            },
            {
                "host": "node-24",
                "host_type": [],
                "id": "node-24",
                "ip_address": "192.168.100.8",
                "name": "node-24",
                "os_id": "6",
                "parent_id": "WebEx-RTP-Zone",
                "parent_type": "availability_zone",
                "services": {
                    "nova-compute": {
                        "active": True,
                        "available": False,
                        "updated_at": "2016-10-04T20:53:11.000000"
                    }
                },
                "zone": "WebEx-RTP-Zone"
            }
]