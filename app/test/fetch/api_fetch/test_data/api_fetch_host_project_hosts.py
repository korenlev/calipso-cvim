HOST_DOC = {
    "host": "node-6.cisco.com",
    "host_type": [],
    "id": "node-6.cisco.com",
    "name": "node-6.cisco.com",
    "parent_id": "internal",
    "parent_type": "availability_zone",
    "services": {
        "nova-cert": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:12:56.000000"
        },
        "nova-conductor": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:12:46.000000"
        },
        "nova-consoleauth": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:12:54.000000"
        },
        "nova-scheduler": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:13:10.000000"
        }
    },
    "zone": "internal"
}

NONEXISTENT_TYPE = "nova"
COMPUTE_TYPE = "Compute"
ZONE = "internal"
HOST_ZONE = "Test"

TOKEN = {'tenant': {
    'description': 'admin tenant',
    'name': 'admin',
    'is_domain': False,
    'id': '8c1751e0ce714736a63fee3c776164da',
    'enabled': True,
    'parent_id': None
    },
    'issued_at': '2016-10-19T23:06:29.000000Z',
    'expires': '2016-10-20T00:06:28.615780Z',
    'id': 'gAAAAABYB_x10x_6AlA2Y5RJZ6HCcCDSXe0f8vfisKnOM_XCDZvwl2qiwzCQIOYX9mCmRyGojZ2JEjIb0vHL0f0hxqSq84g5jbZpN0h0Un_RkTZXSKf0K1uigbr3q__ilhctLvwWNem6XQSGrav1fQrec_DjdvUxSwuoBSSo82kKQ7SvPSdVwrA',
    'token_expiry_time': 1476921988,
    'audit_ids': ['2Ps0lRlHRIG80FWamMkwWg']
}

REGION_NAME = "RegionOne"
TEST_PROJECT_NAME = "Test"
PROJECT_NAME = "admin"

ENDPOINT = "http://10.56.20.239:8774/v2/8c1751e0ce714736a63fee3c776164da"
AVAILABILITY_ZONE_RESPONSE = {
    "availabilityZoneInfo": [
        {
            "hosts": {
                "node-6.cisco.com": {
                    "nova-cert": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:56.000000"
                    },
                    "nova-conductor": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:46.000000"
                    },
                    "nova-consoleauth": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:54.000000"
                    },
                    "nova-scheduler": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:10.000000"
                    }
                }
            },
            "zoneName": "internal",
            "zoneState": {
                "available": True
            }
        },
        {
            "hosts": {
                "node-5.cisco.com": {
                    "nova-compute": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:42.000000"
                    }
                }
            },
            "zoneName": "osdna-zone",
            "zoneState": {
                "available": True
            }
        },
        {
            "hosts": {
                "node-4.cisco.com": {
                    "nova-compute": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:44.000000"
                    }
                }
            },
            "zoneName": "nova",
            "zoneState": {
                "available": True
            }
        }
    ]
}

AVAILABILITY_ERROR_RESPONSE = {'status': 400}

HYPERVISORS_RESPONSE = {
    "hypervisors": [
        {
            "hypervisor_hostname": "node-5.cisco.com",
            "id": 1,
            "state": "up",
            "status": "enabled"
        },
        {
            "hypervisor_hostname": "node-4.cisco.com",
            "id": 2,
            "state": "up",
            "status": "enabled"
        }
    ]
}

HYPERVISORS_ERROR_RESPONSE = {'status': 400}

HOST_TO_BE_FETCHED_IP = {
    "host": "node-5.cisco.com",
    "host_type": [
        "Compute"
    ],
    "id": "node-5.cisco.com",
    "name": "node-5.cisco.com",
    "os_id": "1",
    "parent_id": "osdna-zone",
    "parent_type": "availability_zone",
    "services": {
        "nova-compute": {
            "active": True,
            "available": True,
            "updated_at": "2016-10-21T18:22:42.000000"
        }
    },
    "zone": "osdna-zone"
}

IP_ADDRESS_RESPONSE = [
    {
        "ip_address": "192.168.0.4"
    }
]

HOSTS_TO_BE_FETCHED_NETWORK_DETAILS = [
    {
        "host": "node-6.cisco.com",
        "host_type": [
            "Controller"
        ],
        "id": "node-6.cisco.com",
        "name": "node-6.cisco.com",
        "parent_id": "internal",
        "parent_type": "availability_zone",
        "services": {
            "nova-cert": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:56.000000"
            },
            "nova-conductor": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:46.000000"
            },
            "nova-consoleauth": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:54.000000"
            },
            "nova-scheduler": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:10.000000"
            }
        },
        "zone": "internal"
    },
    {
        "host": "node-5.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-5.cisco.com",
        "ip_address": "192.168.0.4",
        "name": "node-5.cisco.com",
        "os_id": "1",
        "parent_id": "osdna-zone",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:42.000000"
            }
        },
        "zone": "osdna-zone"
    },
    {
        "host": "node-4.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-4.cisco.com",
        "ip_address": "192.168.0.5",
        "name": "node-4.cisco.com",
        "os_id": "2",
        "parent_id": "nova",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:44.000000"
            }
        },
        "zone": "nova"
    }
]



NETWORKS_DETAILS_RESPONSE = [
    {
        "configurations": "{\"subnets\": 9, \"use_namespaces\": true, \"dhcp_lease_duration\": 600, \"dhcp_driver\": \"neutron.agent.linux.dhcp.Dnsmasq\", \"ports\": 19, \"log_agent_heartbeats\": false, \"networks\": 9}",
        "host": "node-6.cisco.com",
        "id": "node-6.cisco.com"
    },
    {
        "configurations": "{\"log_agent_heartbeats\": false, \"nova_metadata_ip\": \"192.168.0.2\", \"nova_metadata_port\": 8775, \"metadata_proxy_socket\": \"/var/lib/neutron/metadata_proxy\"}",
        "host": "node-6.cisco.com",
        "id": "node-6.cisco.com"
    },
    {
        "configurations": "{\"router_id\": \"\", \"agent_mode\": \"legacy\", \"gateway_external_network_id\": \"\", \"handle_internal_only_routers\": true, \"use_namespaces\": true, \"routers\": 2, \"interfaces\": 4, \"floating_ips\": 1, \"interface_driver\": \"neutron.agent.linux.interface.OVSInterfaceDriver\", \"log_agent_heartbeats\": false, \"external_network_bridge\": \"\", \"ex_gw_ports\": 2}",
        "host": "node-6.cisco.com",
        "id": "node-6.cisco.com"
    }
]

REGION_URL = "http://192.168.0.2:8776/v2/329e0576da594c62a911d0dccb1238a7"
AVAILABILITY_ZONE = {
    "hosts": {
                "node-6.cisco.com": {
                    "nova-cert": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:56.000000"
                    },
                    "nova-conductor": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:46.000000"
                    },
                    "nova-consoleauth": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:54.000000"
                    },
                    "nova-scheduler": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-21T18:22:10.000000"
                    }
                }
            },
            "zoneName": "internal",
            "zoneState": {
                "available": True
            }
        }

HOST_NAME = "node-6.cisco.com"

GET_FOR_REGION_INFO = [
    {
        "config": {
            "agent_mode": "legacy",
            "ex_gw_ports": 2,
            "external_network_bridge": "",
            "floating_ips": 1,
            "gateway_external_network_id": "",
            "handle_internal_only_routers": True,
            "interface_driver": "neutron.agent.linux.interface.OVSInterfaceDriver",
            "interfaces": 4,
            "log_agent_heartbeats": False,
            "router_id": "",
            "routers": 2,
            "use_namespaces": True
        },
        "host": "node-6.cisco.com",
        "host_type": [
            "Controller",
            "Network"
        ],
        "id": "node-6.cisco.com",
        "name": "node-6.cisco.com",
        "parent_id": "internal",
        "parent_type": "availability_zone",
        "services": {
            "nova-cert": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:56.000000"
            },
            "nova-conductor": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:46.000000"
            },
            "nova-consoleauth": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:54.000000"
            },
            "nova-scheduler": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:10.000000"
            }
        },
        "zone": "internal"
    },
    {
        "host": "node-5.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-5.cisco.com",
        "ip_address": "192.168.0.4",
        "name": "node-5.cisco.com",
        "os_id": "1",
        "parent_id": "osdna-zone",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:42.000000"
            }
        },
        "zone": "osdna-zone"
    },
    {
        "host": "node-4.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-4.cisco.com",
        "ip_address": "192.168.0.5",
        "name": "node-4.cisco.com",
        "os_id": "2",
        "parent_id": "nova",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:22:44.000000"
            }
        },
        "zone": "nova"
    }
]

# FUNCTIONAL TEST
INPUT = "admin"

RESULT = [
    {
        "config": {
            "agent_mode": "legacy",
            "ex_gw_ports": 2,
            "external_network_bridge": "",
            "floating_ips": 1,
            "gateway_external_network_id": "",
            "handle_internal_only_routers": True,
            "interface_driver": "neutron.agent.linux.interface.OVSInterfaceDriver",
            "interfaces": 4,
            "log_agent_heartbeats": False,
            "router_id": "",
            "routers": 2,
            "use_namespaces": True
        },
        "host": "node-6.cisco.com",
        "host_type": [
            "Controller",
            "Network"
        ],
        "id": "node-6.cisco.com",
        "name": "node-6.cisco.com",
        "parent_id": "internal",
        "parent_type": "availability_zone",
        "services": {
            "nova-cert": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:12:56.000000"
            },
            "nova-conductor": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:12:46.000000"
            },
            "nova-consoleauth": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:12:54.000000"
            },
            "nova-scheduler": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:13:10.000000"
            }
        },
        "zone": "internal"
    },
    {
        "host": "node-5.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-5.cisco.com",
        "ip_address": "192.168.0.4",
        "name": "node-5.cisco.com",
        "os_id": "1",
        "parent_id": "osdna-zone",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:12:42.000000"
            }
        },
        "zone": "osdna-zone"
    },
    {
        "host": "node-4.cisco.com",
        "host_type": [
            "Compute"
        ],
        "id": "node-4.cisco.com",
        "ip_address": "192.168.0.5",
        "name": "node-4.cisco.com",
        "os_id": "2",
        "parent_id": "nova",
        "parent_type": "availability_zone",
        "services": {
            "nova-compute": {
                "active": True,
                "available": True,
                "updated_at": "2016-10-21T18:12:44.000000"
            }
        },
        "zone": "nova"
    }
]

