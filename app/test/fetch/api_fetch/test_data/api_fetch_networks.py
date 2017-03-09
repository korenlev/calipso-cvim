NETWORKS_RESPONSE = {
    "networks": [
        {
            "admin_state_up": True,
            "id": "8673c48a-f137-4497-b25d-08b7b218fd17",
            "mtu": 1400,
            "name": "25",
            "port_security_enabled": True,
            "provider:network_type": "vxlan",
            "provider:physical_network": None,
            "provider:segmentation_id": 52,
            "router:external": False,
            "shared": False,
            "status": "ACTIVE",
            "subnets": [
                "cae3c81d-9a27-48c4-b8f6-32867ca03134"
            ],
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        }
    ]
}
WRONG_NETWORK_RESPONSE = {
}

SUBNETS_RESPONSE = {
    "subnets": [
        {
            "allocation_pools": [
                {
                    "end": "172.16.3.254",
                    "start": "172.16.3.2"
                }
            ],
            "cidr": "172.16.3.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.3.1",
            "host_routes": [],
            "id": "e86494e7-6404-4574-9af4-e03a7f3f58e7",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "osdna-Subnet1",
            "network_id": "7e59b726-d6f4-451a-a574-c67a920ff627",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.0.254",
                    "start": "172.16.0.130"
                }
            ],
            "cidr": "172.16.0.0/24",
            "dns_nameservers": [],
            "enable_dhcp": False,
            "gateway_ip": "172.16.0.1",
            "host_routes": [],
            "id": "a5336853-cbc0-49e8-8401-a093e8bab7bb",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "admin_floating_net__subnet",
            "network_id": "c64adb76-ad9d-4605-9f5e-bd6dbe325cfb",
            "subnetpool_id": None,
            "tenant_id": "8c1751e0ce714736a63fee3c776164da"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.4.254",
                    "start": "172.16.4.2"
                }
            ],
            "cidr": "172.16.4.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.4.1",
            "host_routes": [],
            "id": "f68b9dd3-4cb5-46aa-96b1-f9c8a7abc3aa",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "osdna-subnet4",
            "network_id": "b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.10.126",
                    "start": "172.16.10.2"
                }
            ],
            "cidr": "172.16.10.0/25",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.10.1",
            "host_routes": [],
            "id": "a73a52dc-bee3-4d1b-888b-3928b19ac4d7",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "the",
            "network_id": "413de095-01ed-49dc-aa50-4479f43d390e",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.2.254",
                    "start": "172.16.2.2"
                }
            ],
            "cidr": "172.16.2.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.2.1",
            "host_routes": [],
            "id": "2e9e2349-403e-4a5a-ba40-ac3db9a4e35c",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "osdna-subnet3",
            "network_id": "eb276a62-15a9-4616-a192-11466fdd147f",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.1.254",
                    "start": "172.16.1.2"
                }
            ],
            "cidr": "172.16.1.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.1.1",
            "host_routes": [],
            "id": "c1287696-224b-4a72-9f1d-d45176671bce",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "osdna-subnet2",
            "network_id": "a55ff1e8-3821-4e5f-bcfd-07df93720a4f",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.13.254",
                    "start": "172.16.13.2"
                }
            ],
            "cidr": "172.16.13.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.13.1",
            "host_routes": [],
            "id": "9a9c1848-ea23-4c5d-8c40-ae1def4c2de3",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "312",
            "network_id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "172.16.12.254",
                    "start": "172.16.12.2"
                }
            ],
            "cidr": "172.16.12.0/24",
            "dns_nameservers": [],
            "enable_dhcp": True,
            "gateway_ip": "172.16.12.1",
            "host_routes": [],
            "id": "cae3c81d-9a27-48c4-b8f6-32867ca03134",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "test23",
            "network_id": "0abe6331-0d74-4bbd-ad89-a5719c3793e4",
            "subnetpool_id": None,
            "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
        },
        {
            "allocation_pools": [
                {
                    "end": "192.168.111.254",
                    "start": "192.168.111.2"
                }
            ],
            "cidr": "192.168.111.0/24",
            "dns_nameservers": [
                "8.8.4.4",
                "8.8.8.8"
            ],
            "enable_dhcp": True,
            "gateway_ip": "192.168.111.1",
            "host_routes": [],
            "id": "29fdeba1-91de-4463-9675-a7697bf4b5c8",
            "ip_version": 4,
            "ipv6_address_mode": None,
            "ipv6_ra_mode": None,
            "name": "admin_internal_net__subnet",
            "network_id": "6504fcf7-41d7-40bb-aeb1-6a7658c105fc",
            "subnetpool_id": None,
            "tenant_id": "8c1751e0ce714736a63fee3c776164da"
        }
    ]
}

ENDPOINT = "http://10.56.20.239:9696"
WRONG_SUBNETS_RESPONSE = {}

GET_FOR_REGION = [{
        "admin_state_up": True,
        "cidrs": [
            "172.16.13.0/24"
        ],
        "id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "123456",
        "network": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 21,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "312": {
                "allocation_pools": [
                    {
                        "end": "172.16.13.254",
                        "start": "172.16.13.2"
                    }
                ],
                "cidr": "172.16.13.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.13.1",
                "host_routes": [],
                "id": "9a9c1848-ea23-4c5d-8c40-ae1def4c2de3",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "312",
                "network_id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    }]

PROJECT = {
        "description": "",
        "enabled": True,
        "id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "name": "OSDNA-project"
    }

REGION_NAME = "RegionOne"
# FUNCTION TEST

INPUT = None

result = [{
        "admin_state_up": True,
        "cidrs": [
            "172.16.13.0/24"
        ],
        "id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "123456",
        "network": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 21,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "312": {
                "allocation_pools": [
                    {
                        "end": "172.16.13.254",
                        "start": "172.16.13.2"
                    }
                ],
                "cidr": "172.16.13.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.13.1",
                "host_routes": [],
                "id": "9a9c1848-ea23-4c5d-8c40-ae1def4c2de3",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "312",
                "network_id": "2e3b85f4-756c-49d9-b34c-f3db13212dbc",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },{
        "admin_state_up": True,
        "cidrs": [
            "172.16.1.0/24"
        ],
        "id": "a55ff1e8-3821-4e5f-bcfd-07df93720a4f",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "osdna-net2",
        "network": "a55ff1e8-3821-4e5f-bcfd-07df93720a4f",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 51,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "osdna-subnet2": {
                "allocation_pools": [
                    {
                        "end": "172.16.1.254",
                        "start": "172.16.1.2"
                    }
                ],
                "cidr": "172.16.1.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.1.1",
                "host_routes": [],
                "id": "c1287696-224b-4a72-9f1d-d45176671bce",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "osdna-subnet2",
                "network_id": "a55ff1e8-3821-4e5f-bcfd-07df93720a4f",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    }, {
        "admin_state_up": True,
        "cidrs": [
            "172.16.10.0/25"
        ],
        "id": "413de095-01ed-49dc-aa50-4479f43d390e",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "aiya",
        "network": "413de095-01ed-49dc-aa50-4479f43d390e",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 50,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "the": {
                "allocation_pools": [
                    {
                        "end": "172.16.10.126",
                        "start": "172.16.10.2"
                    }
                ],
                "cidr": "172.16.10.0/25",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.10.1",
                "host_routes": [],
                "id": "a73a52dc-bee3-4d1b-888b-3928b19ac4d7",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "the",
                "network_id": "413de095-01ed-49dc-aa50-4479f43d390e",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },  {
        "admin_state_up": True,
        "cidrs": [
            "172.16.4.0/24"
        ],
        "id": "b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "osdna-met4",
        "network": "b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 96,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "osdna-subnet4": {
                "allocation_pools": [
                    {
                        "end": "172.16.4.254",
                        "start": "172.16.4.2"
                    }
                ],
                "cidr": "172.16.4.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.4.1",
                "host_routes": [],
                "id": "f68b9dd3-4cb5-46aa-96b1-f9c8a7abc3aa",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "osdna-subnet4",
                "network_id": "b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },  {
        "admin_state_up": True,
        "cidrs": [
            "172.16.3.0/24"
        ],
        "id": "7e59b726-d6f4-451a-a574-c67a920ff627",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "osdna-net1",
        "network": "7e59b726-d6f4-451a-a574-c67a920ff627",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 47,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "osdna-Subnet1": {
                "allocation_pools": [
                    {
                        "end": "172.16.3.254",
                        "start": "172.16.3.2"
                    }
                ],
                "cidr": "172.16.3.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.3.1",
                "host_routes": [],
                "id": "e86494e7-6404-4574-9af4-e03a7f3f58e7",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "osdna-Subnet1",
                "network_id": "7e59b726-d6f4-451a-a574-c67a920ff627",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },   {
        "admin_state_up": True,
        "cidrs": [
            "172.16.0.0/24"
        ],
        "id": "c64adb76-ad9d-4605-9f5e-bd6dbe325cfb",
        "master_parent_id": "8c1751e0ce714736a63fee3c776164da",
        "master_parent_type": "project",
        "mtu": 1500,
        "name": "admin_floating_net",
        "network": "c64adb76-ad9d-4605-9f5e-bd6dbe325cfb",
        "parent_id": "8c1751e0ce714736a63fee3c776164da-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "flat",
        "provider:physical_network": "physnet1",
        "provider:segmentation_id": None,
        "router:external": True,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "admin_floating_net__subnet": {
                "allocation_pools": [
                    {
                        "end": "172.16.0.254",
                        "start": "172.16.0.130"
                    }
                ],
                "cidr": "172.16.0.0/24",
                "dns_nameservers": [],
                "enable_dhcp": False,
                "gateway_ip": "172.16.0.1",
                "host_routes": [],
                "id": "a5336853-cbc0-49e8-8401-a093e8bab7bb",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "admin_floating_net__subnet",
                "network_id": "c64adb76-ad9d-4605-9f5e-bd6dbe325cfb",
                "subnetpool_id": None,
                "tenant_id": "8c1751e0ce714736a63fee3c776164da"
            }
        },
        "tenant_id": "8c1751e0ce714736a63fee3c776164da"
    },   {
        "admin_state_up": True,
        "cidrs": [
            "172.16.2.0/24"
        ],
        "id": "eb276a62-15a9-4616-a192-11466fdd147f",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "osdna-net3",
        "network": "eb276a62-15a9-4616-a192-11466fdd147f",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 14,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "osdna-subnet3": {
                "allocation_pools": [
                    {
                        "end": "172.16.2.254",
                        "start": "172.16.2.2"
                    }
                ],
                "cidr": "172.16.2.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.2.1",
                "host_routes": [],
                "id": "2e9e2349-403e-4a5a-ba40-ac3db9a4e35c",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "osdna-subnet3",
                "network_id": "eb276a62-15a9-4616-a192-11466fdd147f",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },   {
        "admin_state_up": True,
        "id": "8673c48a-f137-4497-b25d-08b7b218fd17",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "25",
        "network": "8673c48a-f137-4497-b25d-08b7b218fd17",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 52,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": [],
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },   {
        "admin_state_up": True,
        "cidrs": [
            "172.16.12.0/24"
        ],
        "id": "0abe6331-0d74-4bbd-ad89-a5719c3793e4",
        "master_parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "test123",
        "network": "0abe6331-0d74-4bbd-ad89-a5719c3793e4",
        "parent_id": "75c0eb79ff4a42b0ae4973c8375ddf40-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 4,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "test23": {
                "allocation_pools": [
                    {
                        "end": "172.16.12.254",
                        "start": "172.16.12.2"
                    }
                ],
                "cidr": "172.16.12.0/24",
                "dns_nameservers": [],
                "enable_dhcp": True,
                "gateway_ip": "172.16.12.1",
                "host_routes": [],
                "id": "cae3c81d-9a27-48c4-b8f6-32867ca03134",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "test23",
                "network_id": "0abe6331-0d74-4bbd-ad89-a5719c3793e4",
                "subnetpool_id": None,
                "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
            }
        },
        "tenant_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },  {
        "admin_state_up": True,
        "cidrs": [
            "192.168.111.0/24"
        ],
        "id": "6504fcf7-41d7-40bb-aeb1-6a7658c105fc",
        "master_parent_id": "8c1751e0ce714736a63fee3c776164da",
        "master_parent_type": "project",
        "mtu": 1400,
        "name": "admin_internal_net",
        "network": "6504fcf7-41d7-40bb-aeb1-6a7658c105fc",
        "parent_id": "8c1751e0ce714736a63fee3c776164da-networks",
        "parent_text": "Networks",
        "parent_type": "networks_folder",
        "port_security_enabled": True,
        "provider:network_type": "vxlan",
        "provider:physical_network": None,
        "provider:segmentation_id": 2,
        "router:external": False,
        "shared": False,
        "status": "ACTIVE",
        "subnets": {
            "admin_internal_net__subnet": {
                "allocation_pools": [
                    {
                        "end": "192.168.111.254",
                        "start": "192.168.111.2"
                    }
                ],
                "cidr": "192.168.111.0/24",
                "dns_nameservers": [
                    "8.8.4.4",
                    "8.8.8.8"
                ],
                "enable_dhcp": True,
                "gateway_ip": "192.168.111.1",
                "host_routes": [],
                "id": "29fdeba1-91de-4463-9675-a7697bf4b5c8",
                "ip_version": 4,
                "ipv6_address_mode": None,
                "ipv6_ra_mode": None,
                "name": "admin_internal_net__subnet",
                "network_id": "6504fcf7-41d7-40bb-aeb1-6a7658c105fc",
                "subnetpool_id": None,
                "tenant_id": "8c1751e0ce714736a63fee3c776164da"
            }
        },
        "tenant_id": "8c1751e0ce714736a63fee3c776164da"
    }
]

