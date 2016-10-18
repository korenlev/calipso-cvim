NETWORK = {
                    "admin_state_up": True,
                    "cidrs": [
                        "172.16.102.0/24"
                    ],
                    "id": "080145e2-ccef-4946-b6ce-be633c88669e",
                    "master_parent_id": "9bb12590b58d4c729871dc0c41c5a0f3",
                    "master_parent_type": "project",
                    "name": "net-102",
                    "network": "080145e2-ccef-4946-b6ce-be633c88669e",
                    "parent_id": "9bb12590b58d4c729871dc0c41c5a0f3-networks",
                    "parent_text": "Networks",
                    "parent_type": "networks_folder",
                    "provider:network_type": "vlan",
                    "provider:physical_network": "physnet2",
                    "provider:segmentation_id": 1001,
                    "router:external": False,
                    "shared": False,
                    "status": "ACTIVE",
                    "subnets": {
                        "sub102": {
                            "allocation_pools": [
                                {
                                    "end": "172.16.102.254",
                                    "start": "172.16.102.2"
                                }
                            ],
                            "cidr": "172.16.102.0/24",
                            "dns_nameservers": [],
                            "enable_dhcp": True,
                            "gateway_ip": "172.16.102.1",
                            "host_routes": [],
                            "id": "7c512d57-f948-46e4-a0b0-e6287079bf00",
                            "ip_version": 4,
                            "ipv6_address_mode": None,
                            "ipv6_ra_mode": None,
                            "name": "sub102",
                            "network_id": "080145e2-ccef-4946-b6ce-be633c88669e",
                            "tenant_id": "9bb12590b58d4c729871dc0c41c5a0f3"
                        }
                    },
                    "tenant_id": "9bb12590b58d4c729871dc0c41c5a0f3"
                }
