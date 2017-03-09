PROJECT_LIST = [
    {
        'enabled': True, 
        'object_name': 'OSDNA-project', 
        'description': '',
        '_id': '580680cd4a0a8a3fbe3bee10',
        'environment': 'Mirantis-Liberty-Xiaocong',
        'parent_id': 'Mirantis-Liberty-Xiaocong-projects'
        , 'name': 'OSDNA-project', 
        'id_path': '/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-projects/75c0eb79ff4a42b0ae4973c8375ddf40',
        'parent_type': 'projects_folder', 
        'children_url': '/osdna_dev/discover.py?type=tree&id=75c0eb79ff4a42b0ae4973c8375ddf40', 
        'name_path': '/Mirantis-Liberty-Xiaocong/Projects/OSDNA-project', 
        'show_in_tree': True, 
        'type': 'project',
        'id': '75c0eb79ff4a42b0ae4973c8375ddf40',
    }, 
    {
        'enabled': True, 
        'object_name': 'admin', 
        'description': 'admin tenant', 
        '_id': '580680cd4a0a8a3fbe3bee11', 
        'environment': 'Mirantis-Liberty-Xiaocong', 
        'parent_id': 'Mirantis-Liberty-Xiaocong-projects', 
        'name': 'admin', 'id_path': '/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-projects/8c1751e0ce714736a63fee3c776164da',
        'parent_type': 'projects_folder',
        'children_url': '/osdna_dev/discover.py?type=tree&id=8c1751e0ce714736a63fee3c776164da',
        'name_path': '/Mirantis-Liberty-Xiaocong/Projects/admin', 
        'show_in_tree': True, 
        'type': 'project',
        'id': '8c1751e0ce714736a63fee3c776164da', 
    }
]

HOST = {
    'parent_id': 'osdna-zone', 
    'os_id': '1',
    'object_name': 'node-5.cisco.com',
    '_id': '5806810e4a0a8a3fbe3bee3e', 
    'children_url': '/osdna_dev/discover.py?type=tree&id=node-5.cisco.com', 
    'services': {
        'nova-compute': 
            {
                'active': True,
                'available': True
            }
    }, 
    'environment': 'Mirantis-Liberty-Xiaocong',
    'host_type': ['Compute'], 
    'ip_address': '192.168.0.4', 
    'name': 'node-5.cisco.com',
    'host': 'node-5.cisco.com', 
    'parent_type': 'availability_zone', 
    'type': 'host',
    'name_path': '/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/osdna-zone/node-5.cisco.com',
    'show_in_tree': True,
    'zone': 'osdna-zone',
    'id': 'node-5.cisco.com', 
    'id_path': '/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/osdna-zone/node-5.cisco.com'
}

NON_COMPUTE_HOST = {
    'parent_id': 'osdna-zone',
    'os_id': '1',
    'object_name': 'node-5.cisco.com',
    '_id': '5806810e4a0a8a3fbe3bee3e',
    'children_url': '/osdna_dev/discover.py?type=tree&id=node-5.cisco.com',
    'services': {
        'nova-compute':
            {
                'active': True,
                'available': True
            }
    },
    'environment': 'Mirantis-Liberty-Xiaocong',
    'host_type': ['Compute'],
    'ip_address': '192.168.0.4',
    'name': 'node-5.cisco.com',
    'host': 'node-5.cisco.com',
    'parent_type': 'availability_zone',
    'type': 'host',
    'name_path': '/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/osdna-zone/node-5.cisco.com',
    'show_in_tree': True,
    'zone': 'osdna-zone',
    'id': 'node-5.cisco.com',
    'id_path': '/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/osdna-zone/node-5.cisco.com'
}

HOST_NAME = "node-5.cisco.com"

GET_INSTANCES_FROM_API = [
    {
        "host": "node-5.cisco.com",
        "id": "6f29c867-9150-4533-8e19-70d749b172fa",
        "local_name": "instance-00000002",
        "uuid": "6f29c867-9150-4533-8e19-70d749b172fa"
    },
    {
        "host": "node-5.cisco.com",
        "id": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9",
        "local_name": "instance-0000001c",
        "uuid": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9"
    },
    {
        "host": "node-5.cisco.com",
        "id": "bf0cb914-b316-486c-a4ce-f22deb453c52",
        "local_name": "instance-00000026",
        "uuid": "bf0cb914-b316-486c-a4ce-f22deb453c52"
    }
]

GET_SERVERS_RESPONSE = {
    "hypervisors": [
        {
            "hypervisor_hostname": "node-5.cisco.com",
            "id": 1,
            "servers": [
                {
                    "name": "instance-00000002",
                    "uuid": "6f29c867-9150-4533-8e19-70d749b172fa"
                },
                {
                    "name": "instance-0000001c",
                    "uuid": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9"
                },
                {
                    "name": "instance-00000026",
                    "uuid": "bf0cb914-b316-486c-a4ce-f22deb453c52"
                }
            ],
            "state": "up",
            "status": "enabled"
        }
    ]
}

GET_SERVERS_WITHOUT_HYPERVISORS_RESPONSE = {
    "text": "test"
}

GET_SERVERS_WITHOUT_SERVERS_RESPONSE = {
    "hypervisors": [
        {
            "hypervisor_hostname": "node-5.cisco.com",
            "id": 1
        }
    ]
}

INSTANCE_FOLDER_ID = "node-5.cisco.com-instances"

# FUNCTIONAL TEST
INPUT = {
    "create_object": True,
    "environment": "Mirantis-Liberty-Xiaocong",
    "id": "node-5.cisco.com-instances",
    "id_path": "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-availability_zones/osdna-zone/node-5.cisco.com/node-5.cisco.com-instances",
    "name": "Instances",
    "name_path": "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Availability Zones/osdna-zone/node-5.cisco.com/Instances",
    "object_name": "Instances",
    "parent_id": "node-5.cisco.com",
    "parent_type": "host",
    "show_in_tree": True,
    "text": "Instances",
    "type": "instances_folder"
}

RESULT = [
    {
        "host": "node-5.cisco.com",
        "id": "6f29c867-9150-4533-8e19-70d749b172fa",
        "in_project-OSDNA-project": "1",
        "ip_address": "192.168.0.4",
        "local_name": "instance-00000002",
        "name": "osdna-vm2",
        "network": [
            "a55ff1e8-3821-4e5f-bcfd-07df93720a4f"
        ],
        "network_info": [
            {
                "active": True,
                "address": "fa:16:3e:1f:b3:15",
                "details": {
                    "ovs_hybrid_plug": True,
                    "port_filter": True
                },
                "devname": "tap2cb9fefc-e2",
                "id": "2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd",
                "meta": {},
                "network": {
                    "bridge": "br-int",
                    "id": "a55ff1e8-3821-4e5f-bcfd-07df93720a4f",
                    "label": "osdna-net2",
                    "meta": {
                        "injected": False,
                        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
                    },
                    "subnets": [
                        {
                            "cidr": "172.16.1.0/24",
                            "dns": [],
                            "gateway": {
                                "address": "172.16.1.1",
                                "meta": {},
                                "type": "gateway",
                                "version": 4
                            },
                            "ips": [
                                {
                                    "address": "172.16.1.3",
                                    "floating_ips": [],
                                    "meta": {},
                                    "type": "fixed",
                                    "version": 4
                                }
                            ],
                            "meta": {
                                "dhcp_server": "172.16.1.2"
                            },
                            "routes": [],
                            "version": 4
                        }
                    ]
                },
                "ovs_interfaceid": "2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd",
                "preserve_on_delete": False,
                "profile": {},
                "qbg_params": None,
                "qbh_params": None,
                "type": "ovs",
                "vnic_type": "normal"
            }
        ],
        "parent_id": "node-5.cisco.com-instances",
        "parent_type": "instances_folder",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "type": "instance",
        "uuid": "6f29c867-9150-4533-8e19-70d749b172fa"
    },
    {
        "host": "node-5.cisco.com",
        "id": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9",
        "in_project-OSDNA-project": "1",
        "ip_address": "192.168.0.4",
        "local_name": "instance-0000001c",
        "name": "yaron-test-notify2",
        "network": [
            "7e59b726-d6f4-451a-a574-c67a920ff627"
        ],
        "network_info": [
            {
                "active": True,
                "address": "fa:16:3e:69:dd:8e",
                "details": {
                    "ovs_hybrid_plug": True,
                    "port_filter": True
                },
                "devname": "tap44b12004-63",
                "id": "44b12004-6308-4e03-93bf-fa8be5916dfb",
                "meta": {},
                "network": {
                    "bridge": "br-int",
                    "id": "7e59b726-d6f4-451a-a574-c67a920ff627",
                    "label": "osdna-net1",
                    "meta": {
                        "injected": False,
                        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
                    },
                    "subnets": [
                        {
                            "cidr": "172.16.3.0/24",
                            "dns": [],
                            "gateway": {
                                "address": "172.16.3.1",
                                "meta": {},
                                "type": "gateway",
                                "version": 4
                            },
                            "ips": [
                                {
                                    "address": "172.16.3.28",
                                    "floating_ips": [],
                                    "meta": {},
                                    "type": "fixed",
                                    "version": 4
                                }
                            ],
                            "meta": {
                                "dhcp_server": "172.16.3.2"
                            },
                            "routes": [],
                            "version": 4
                        }
                    ]
                },
                "ovs_interfaceid": "44b12004-6308-4e03-93bf-fa8be5916dfb",
                "preserve_on_delete": False,
                "profile": {},
                "qbg_params": None,
                "qbh_params": None,
                "type": "ovs",
                "vnic_type": "normal"
            }
        ],
        "parent_id": "node-5.cisco.com-instances",
        "parent_type": "instances_folder",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "type": "instance",
        "uuid": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9"
    },
    {
        "host": "node-5.cisco.com",
        "id": "bf0cb914-b316-486c-a4ce-f22deb453c52",
        "in_project-OSDNA-project": "1",
        "ip_address": "192.168.0.4",
        "local_name": "instance-00000026",
        "name": "test",
        "network": [
            "2e3b85f4-756c-49d9-b34c-f3db13212dbc"
        ],
        "network_info": [
            {
                "active": True,
                "address": "fa:16:3e:e8:7f:04",
                "details": {
                    "ovs_hybrid_plug": True,
                    "port_filter": True
                },
                "devname": "tap1f72bd15-8a",
                "id": "1f72bd15-8ab2-43cb-94d7-e823dd845255",
                "meta": {},
                "network": {
                    "bridge": "br-int",
                    "id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
                    "label": "123456",
                    "meta": {
                        "injected": False,
                        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
                    },
                    "subnets": [
                        {
                            "cidr": "172.16.13.0/24",
                            "dns": [],
                            "gateway": {
                                "address": "172.16.13.1",
                                "meta": {},
                                "type": "gateway",
                                "version": 4
                            },
                            "ips": [
                                {
                                    "address": "172.16.13.4",
                                    "floating_ips": [],
                                    "meta": {},
                                    "type": "fixed",
                                    "version": 4
                                }
                            ],
                            "meta": {
                                "dhcp_server": "172.16.13.2"
                            },
                            "routes": [],
                            "version": 4
                        }
                    ]
                },
                "ovs_interfaceid": "1f72bd15-8ab2-43cb-94d7-e823dd845255",
                "preserve_on_delete": False,
                "profile": {},
                "qbg_params": None,
                "qbh_params": None,
                "type": "ovs",
                "vnic_type": "normal"
            }
        ],
        "parent_id": "node-5.cisco.com-instances",
        "parent_type": "instances_folder",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "type": "instance",
        "uuid": "bf0cb914-b316-486c-a4ce-f22deb453c52"
    }
]

