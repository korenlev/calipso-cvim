INSTANCES_FROM_API = [
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

INSTANCES_FROM_DB = [
    {
        "host": "node-5.cisco.com",
        "id": "6f29c867-9150-4533-8e19-70d749b172fa",
        "ip_address": "192.168.0.4",
        "name": "osdna-vm2",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.1.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.1.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.1.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.1.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"a55ff1e8-3821-4e5f-bcfd-07df93720a4f\", \"label\": \"osdna-net2\"}, \"devname\": \"tap2cb9fefc-e2\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:1f:b3:15\", \"active\": true, \"type\": \"ovs\", \"id\": \"2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-5.cisco.com",
        "id": "79e20dbf-a46d-46ee-870b-e0c9f7b357d9",
        "ip_address": "192.168.0.4",
        "name": "yaron-test-notify2",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"44b12004-6308-4e03-93bf-fa8be5916dfb\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.3.28\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.3.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.3.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.3.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"7e59b726-d6f4-451a-a574-c67a920ff627\", \"label\": \"osdna-net1\"}, \"devname\": \"tap44b12004-63\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:69:dd:8e\", \"active\": true, \"type\": \"ovs\", \"id\": \"44b12004-6308-4e03-93bf-fa8be5916dfb\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-5.cisco.com",
        "id": "bf0cb914-b316-486c-a4ce-f22deb453c52",
        "ip_address": "192.168.0.4",
        "name": "test",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"1f72bd15-8ab2-43cb-94d7-e823dd845255\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.4\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"2e3b85f4-756c-49d9-b34c-f3db13212dbc\", \"label\": \"123456\"}, \"devname\": \"tap1f72bd15-8a\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:e8:7f:04\", \"active\": true, \"type\": \"ovs\", \"id\": \"1f72bd15-8ab2-43cb-94d7-e823dd845255\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-5.cisco.com",
        "id": "e1de7561-8fdd-478c-8e7d-56514a0778a6",
        "ip_address": "192.168.0.4",
        "name": "testport",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"cf6089f4-ecb7-4467-bdcc-b3a0a18f4569\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.6\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"2e3b85f4-756c-49d9-b34c-f3db13212dbc\", \"label\": \"123456\"}, \"devname\": \"tapcf6089f4-ec\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:21:a3:e8\", \"active\": true, \"type\": \"ovs\", \"id\": \"cf6089f4-ecb7-4467-bdcc-b3a0a18f4569\", \"qbg_params\": null}, {\"profile\": {}, \"ovs_interfaceid\": \"045dcc18-5616-45f0-a3e3-9f9346ebcf32\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"241e2900-6e4f-4fdf-b8b2-52e3462274ee\", \"label\": \"abcs\"}, \"devname\": \"tap045dcc18-56\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:7a:f5:00\", \"active\": true, \"type\": \"ovs\", \"id\": \"045dcc18-5616-45f0-a3e3-9f9346ebcf32\", \"qbg_params\": null}, {\"profile\": {}, \"ovs_interfaceid\": \"9802cced-4bb2-4d74-b43f-0b54f1d37e18\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.8\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"2e3b85f4-756c-49d9-b34c-f3db13212dbc\", \"label\": \"123456\"}, \"devname\": \"tap9802cced-4b\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:29:45:c5\", \"active\": true, \"type\": \"ovs\", \"id\": \"9802cced-4bb2-4d74-b43f-0b54f1d37e18\", \"qbg_params\": null}, {\"profile\": {}, \"ovs_interfaceid\": \"38ff2940-0e2d-4be8-ab79-5a01fc4527e5\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.4\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"241e2900-6e4f-4fdf-b8b2-52e3462274ee\", \"label\": \"abcs\"}, \"devname\": \"tap38ff2940-0e\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:f1:a7:5d\", \"active\": true, \"type\": \"ovs\", \"id\": \"38ff2940-0e2d-4be8-ab79-5a01fc4527e5\", \"qbg_params\": null}, {\"profile\": {}, \"ovs_interfaceid\": \"7cf00abd-62a5-47b2-9b9c-d84ec03fe5e3\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.9.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.9.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.9.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.9.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"95d2a3bb-16b9-4241-ab51-449482fcb9b9\", \"label\": \"aaaa\"}, \"devname\": \"tap7cf00abd-62\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:c3:42:6b\", \"active\": true, \"type\": \"ovs\", \"id\": \"7cf00abd-62a5-47b2-9b9c-d84ec03fe5e3\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-4.cisco.com",
        "id": "a84c6479-832b-42f0-a3e9-632ebc3baae3",
        "ip_address": "192.168.0.5",
        "name": "osdna-vm1",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"3367afd1-317e-4598-8712-fdd542a7bfa6\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"floating\", \"address\": \"172.16.0.132\"}], \"address\": \"172.16.3.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.3.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.3.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.3.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"7e59b726-d6f4-451a-a574-c67a920ff627\", \"label\": \"osdna-net1\"}, \"devname\": \"tap3367afd1-31\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:1e:8b:a6\", \"active\": true, \"type\": \"ovs\", \"id\": \"3367afd1-317e-4598-8712-fdd542a7bfa6\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-4.cisco.com",
        "id": "72da423b-6c2a-4267-86f1-e3be96dacdbd",
        "ip_address": "192.168.0.5",
        "name": "osdna-vm3",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"3671a6ee-f263-49ee-b8d0-e93b2823f3ba\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.2.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.2.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.2.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.2.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"eb276a62-15a9-4616-a192-11466fdd147f\", \"label\": \"osdna-net3\"}, \"devname\": \"tap3671a6ee-f2\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:b0:62:db\", \"active\": true, \"type\": \"ovs\", \"id\": \"3671a6ee-f263-49ee-b8d0-e93b2823f3ba\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    },
    {
        "host": "node-4.cisco.com",
        "id": "fec3fc2d-be50-4234-b41a-1f43069f3a67",
        "ip_address": "192.168.0.5",
        "name": "test2",
        "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"97bf60ea-507c-4eb5-8277-9afd8b04be81\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.4.8\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.4.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.4.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.4.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"b6fd5175-4b22-4256-9b1a-9fc4b9dce1fe\", \"label\": \"osdna-met4\"}, \"devname\": \"tap97bf60ea-50\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:b6:11:d2\", \"active\": true, \"type\": \"ovs\", \"id\": \"97bf60ea-507c-4eb5-8277-9afd8b04be81\", \"qbg_params\": null}, {\"profile\": {}, \"ovs_interfaceid\": \"10e98e6d-72fc-45b0-931d-4a5c58953a15\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.13.7\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.13.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.13.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.13.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"2e3b85f4-756c-49d9-b34c-f3db13212dbc\", \"label\": \"123456\"}, \"devname\": \"tap10e98e6d-72\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:33:00:4c\", \"active\": true, \"type\": \"ovs\", \"id\": \"10e98e6d-72fc-45b0-931d-4a5c58953a15\", \"qbg_params\": null}]",
        "project": "OSDNA-project",
        "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
    }
]

INSTANCES_FOR_DETAILS = {
    "host": "node-5.cisco.com",
    "id": "6f29c867-9150-4533-8e19-70d749b172fa",
    "ip_address": "192.168.0.4",
    "name": "osdna-vm2",
    "network_info": "[{\"profile\": {}, \"ovs_interfaceid\": \"2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd\", \"preserve_on_delete\": false, \"network\": {\"bridge\": \"br-int\", \"subnets\": [{\"ips\": [{\"meta\": {}, \"version\": 4, \"type\": \"fixed\", \"floating_ips\": [], \"address\": \"172.16.1.3\"}], \"version\": 4, \"meta\": {\"dhcp_server\": \"172.16.1.2\"}, \"dns\": [], \"routes\": [], \"cidr\": \"172.16.1.0/24\", \"gateway\": {\"meta\": {}, \"version\": 4, \"type\": \"gateway\", \"address\": \"172.16.1.1\"}}], \"meta\": {\"injected\": false, \"tenant_id\": \"75c0eb79ff4a42b0ae4973c8375ddf40\"}, \"id\": \"a55ff1e8-3821-4e5f-bcfd-07df93720a4f\", \"label\": \"osdna-net2\"}, \"devname\": \"tap2cb9fefc-e2\", \"vnic_type\": \"normal\", \"qbh_params\": null, \"meta\": {}, \"details\": {\"port_filter\": true, \"ovs_hybrid_plug\": true}, \"address\": \"fa:16:3e:1f:b3:15\", \"active\": true, \"type\": \"ovs\", \"id\": \"2cb9fefc-e279-4ee5-a921-e6ce8e7ce6fd\", \"qbg_params\": null}]",
    "project": "OSDNA-project",
    "project_id": "75c0eb79ff4a42b0ae4973c8375ddf40"
}
# functional test
INPUT = [
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

OUTPUT = [
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