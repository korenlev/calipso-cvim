AVAILABILITY_ZONE_RESPONSE = {
    "availabilityZoneInfo": [
        {
            "hosts": {
                "node-6.cisco.com": {
                    "nova-cert": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-22T01:24:09.000000"
                    },
                    "nova-conductor": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-22T01:23:59.000000"
                    },
                    "nova-consoleauth": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-22T01:24:06.000000"
                    },
                    "nova-scheduler": {
                        "active": True,
                        "available": True,
                        "updated_at": "2016-10-22T01:23:37.000000"
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
                        "updated_at": "2016-10-22T01:23:43.000000"
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
                        "updated_at": "2016-10-22T01:23:47.000000"
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
GET_REGION_RESULT = [
    {
        "available": True,
        "hosts": {
            "node-6.cisco.com": {
                "nova-cert": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:46:11.000000"
                },
                "nova-conductor": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:45:59.000000"
                },
                "nova-consoleauth": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:46:08.000000"
                },
                "nova-scheduler": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:45:37.000000"
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
                    "updated_at": "2016-10-22T01:45:43.000000"
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
                    "updated_at": "2016-10-22T01:45:45.000000"
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
WITHOUT_AVAILABILITY_ZONE_RESPONSE = {"text": "test"}
WRONG_RESPONSE = {"status": 400}
EMPTY_AVAILABILITY_ZONE_RESPONSE = {
    "availabilityZoneInfo": []
}
ENDPOINT = "http://10.56.20.239:8774"
PROJECT = "admin"
TEST_PROJECT = "test"
REGION_NAME = "RegionOne"

# FUNCTIONAL TEST
INPUT = "admin"

RESULT = [
    {
        "available": True,
        "hosts": {
            "node-6.cisco.com": {
                "nova-cert": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:46:11.000000"
                },
                "nova-conductor": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:45:59.000000"
                },
                "nova-consoleauth": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:46:08.000000"
                },
                "nova-scheduler": {
                    "active": True,
                    "available": True,
                    "updated_at": "2016-10-22T01:45:37.000000"
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
                    "updated_at": "2016-10-22T01:45:43.000000"
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
                    "updated_at": "2016-10-22T01:45:45.000000"
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

