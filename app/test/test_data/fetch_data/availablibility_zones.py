AVAILABILITY_ZONES = [
    {
        "available": True,
        "hosts": {
            "node-6.cisco.com": {
                "nova-cert": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:59.000000"
                },
                "nova-conductor": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:12.000000"
                },
                "nova-consoleauth": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:09.000000"
                },
                "nova-scheduler": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:30.000000"
                }
            }
        },
        "id": "internal",
        "master_parent_id": "RegionOne",
        "master_parent_type": "region",
        "name": "internal",
        "parent_id": "RegionOne-availability_zones",
        "parent_text": "Availability Zones",
        "parent_type": "availability_zones_folder"
    },
    {
        "available": True,
        "hosts": {
            "node-5.cisco.com": {
                "nova-compute": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:47.000000"
                }
            }
        },
        "id": "osdna-zone",
        "master_parent_id": "RegionOne",
        "master_parent_type": "region",
        "name": "osdna-zone",
        "parent_id": "RegionOne-availability_zones",
        "parent_text": "Availability Zones",
        "parent_type": "availability_zones_folder"
    },
    {
        "available": True,
        "hosts": {
            "node-4.cisco.com": {
                "nova-compute": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-15T03:33:51.000000"
                }
            }
        },
        "id": "nova",
        "master_parent_id": "RegionOne",
        "master_parent_type": "region",
        "name": "nova",
        "parent_id": "RegionOne-availability_zones",
        "parent_text": "Availability Zones",
        "parent_type": "availability_zones_folder"
    }
]