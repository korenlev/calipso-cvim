###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
AVAILABILITY_ZONE_RESPONSE = {
    "availabilityZoneInfo": [
        {
            "hosts": {
                "node-6.cisco.com": {
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
                }
            },
            "zoneName": "osdna-zone",
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
            }
        },
        "id": "osdna-zone",
        "master_parent_id": "RegionOne",
        "master_parent_type": "region",
        "name": "osdna-zone",
        "parent_id": "RegionOne-availability_zones",
        "parent_text": "Availability Zones",
        "parent_type": "availability_zones_folder"
    }
]
RESPONSE_WITHOUT_AVAILABILITY_ZONE = {"text": "test"}
WRONG_RESPONSE = {"status": 400}
EMPTY_AVAILABILITY_ZONE_RESPONSE = {
    "availabilityZoneInfo": []
}
ENDPOINT = "http://10.56.20.239:8774"
PROJECT = "admin"
REGION_NAME = "RegionOne"
