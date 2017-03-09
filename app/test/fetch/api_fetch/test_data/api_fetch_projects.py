USERS_CORRECT_RESPONSE = {
    "links": {
        "next": None,
        "previous": None,
        "self": "http://10.56.20.239:35357/v3/users"
    },
    "users": [
        {
            "domain_id": "default",
            "email": "admin@localhost",
            "enabled": True,
            "id": "13baa553aae44adca6615e711fd2f6d9",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/13baa553aae44adca6615e711fd2f6d9"
            },
            "name": "admin"
        },
        {
            "domain_id": "default",
            "email": "heat-cfn@localhost",
            "enabled": True,
            "id": "181dd5d677b24e4fb1b7845f4e93c2df",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/181dd5d677b24e4fb1b7845f4e93c2df"
            },
            "name": "heat-cfn"
        },
        {
            "domain_id": "default",
            "email": "nova@localhost",
            "enabled": True,
            "id": "2288cc7ce383437ba7b9836dace96bdd",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/2288cc7ce383437ba7b9836dace96bdd"
            },
            "name": "nova"
        },
        {
            "domain_id": "default",
            "email": "heat@localhost",
            "enabled": True,
            "id": "36f8368ec4464ce2a45e71bad8640053",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/36f8368ec4464ce2a45e71bad8640053"
            },
            "name": "heat"
        },
        {
            "domain_id": "default",
            "email": "ceilometer@localhost",
            "enabled": True,
            "id": "38696bb0476b47249c631d1af0e31eac",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/38696bb0476b47249c631d1af0e31eac"
            },
            "name": "ceilometer"
        },
        {
            "domain_id": "default",
            "email": "cinder@localhost",
            "enabled": True,
            "id": "52f06abff3324311bc21cde81927adac",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/52f06abff3324311bc21cde81927adac"
            },
            "name": "cinder"
        },
        {
            "domain_id": "default",
            "email": "neutron@localhost",
            "enabled": True,
            "id": "73638a2687534f9794cd8057ba860637",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/73638a2687534f9794cd8057ba860637"
            },
            "name": "neutron"
        },
        {
            "domain_id": "default",
            "email": "swift@localhost",
            "enabled": True,
            "id": "9da1fd9cead04c1d97739a4bcda7827a",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/9da1fd9cead04c1d97739a4bcda7827a"
            },
            "name": "swift"
        },
        {
            "domain_id": "2eec75d80d594f5e9e472385a890c8b4",
            "email": "heat_admin@localhost",
            "enabled": True,
            "id": "bd7f332390d24cd795cfe835df19f4d5",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/bd7f332390d24cd795cfe835df19f4d5"
            },
            "name": "heat_admin"
        },
        {
            "domain_id": "default",
            "email": "glance@localhost",
            "enabled": True,
            "id": "d1e2fe2eefca4a15ad57532060d9d052",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/d1e2fe2eefca4a15ad57532060d9d052"
            },
            "name": "glance"
        },
        {
            "domain_id": "default",
            "enabled": True,
            "id": "f02cacb4e9954ed189869a78741d5047",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/f02cacb4e9954ed189869a78741d5047"
            },
            "name": "fuel_stats_user"
        }
    ]
}

USERS_RESPONSE_WITHOUT_USERS = {
    "links": {
        "next": None,
        "previous": None,
        "self": "http://10.56.20.239:35357/v3/users"
    }
}

USERS_RESPONSE_WITHOUT_MATCH = {
    "links": {
        "next": None,
        "previous": None,
        "self": "http://10.56.20.239:35357/v3/users"
    },
    "users": [
        {
            "domain_id": "default",
            "enabled": True,
            "id": "f02cacb4e9954ed189869a78741d5047",
            "links": {
                "self": "http://10.56.20.239:35357/v3/users/f02cacb4e9954ed189869a78741d5047"
            },
            "name": "fuel_stats_user"
        }
    ]
}

PROJECTS_CORRECT_RESPONSE = {
    "links": {
        "next": None,
        "previous": None,
        "self": "http://10.56.20.239:35357/v3/users/13baa553aae44adca6615e711fd2f6d9/projects"
    },
    "projects": [
        {
            "description": "",
            "domain_id": "default",
            "enabled": None,
            "id": "75c0eb79ff4a42b0ae4973c8375ddf40",
            "is_domain": False,
            "links": {
                "self": "http://10.56.20.239:35357/v3/projects/75c0eb79ff4a42b0ae4973c8375ddf40"
            },
            "name": "OSDNA-project",
            "parent_id": None
        },
        {
            "description": "admin tenant",
            "domain_id": "default",
            "enabled": True,
            "id": "8c1751e0ce714736a63fee3c776164da",
            "is_domain": False,
            "links": {
                "self": "http://10.56.20.239:35357/v3/projects/8c1751e0ce714736a63fee3c776164da"
            },
            "name": "admin",
            "parent_id": None
        }
    ]
}

PROJECTS_RESPONSE_WITHOUT_PROJECTS = ""

REGION_PROJECTS = [
    {
        "description": "",
        "enabled": True,
        "id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "name": "OSDNA-project"
    },
    {
        "description": "admin tenant",
        "enabled": True,
        "id": "8c1751e0ce714736a63fee3c776164da",
        "name": "admin"
    }
]

USERS_PROJECTS = [
    "OSDNA-project",
    "admin"
]

REGION_URL_NOVER = "http://10.56.20.239:35357"

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

REGION_RESPONSE = {
    "tenants": [
        {
            "description": "",
            "enabled": True,
            "id": "75c0eb79ff4a42b0ae4973c8375ddf40",
            "name": "OSDNA-project"
        },
        {
            "description": "admin tenant",
            "enabled": True,
            "id": "8c1751e0ce714736a63fee3c776164da",
            "name": "admin"
        },
        {
            "description": "Tenant for the openstack services",
            "enabled": True,
            "id": "a83c8b0d2df24170a7c54f09f824230e",
            "name": "services"
        }
    ],
    "tenants_links": []
}

REGION_ERROR_RESPONSE = {
}

REGION_NAME = "RegionOne"

CONFIGURATIONS = {
    "configuration": [
        {
            "mock": "True",
            "host": "10.56.20.239",
            "name": "mysql",
            "password": "102QreDdiD5sKcvNf9qbHrmr",
            "port": 3307.0,
            "user": "root",
            "schema": "nova"
        },
        {
            "name": "OpenStack",
            "host": "10.56.20.239",
            "admin_token": "38MUh19YWcgQQUlk2VEFQ7Ec",
            "port": "5000",
            "user": "admin",
            "pwd": "admin"
        },
        {
            "host": "10.56.20.239",
            "key": "/Users/xiaocdon/.ssh/id_rsa",
            "name": "CLI",
            "pwd": "",
            "user": "root"
        },
        {
            "name": "AMQP",
            "host": "10.56.20.239",
            "port": "5673",
            "user": "nova",
            "password": "NF2nSv3SisooxPkCTr8fbfOa"
        }
    ],
    "distribution": "Mirantis-8.0",
    "last_scanned:": "5/8/16",
    "name": "Mirantis-Liberty-Xiaocong",
    "network_plugins": [
        "OVS"
    ],
    "operational": "yes",
    "type": "environment"
}

REGIONS = {
            "RegionOne":
                        {
                            "endpoints": {
                                "cinder": {
                                    "adminURL": "http://192.168.0.2:8776/v1/329e0576da594c62a911d0dccb1238a7",
                                    "id": "7908c597eab64a368f3a4d49ca4b070e",
                                    "internalURL": "http://192.168.0.2:8776/v1/329e0576da594c62a911d0dccb1238a7",
                                    "publicURL": "http://172.16.0.2:8776/v1/329e0576da594c62a911d0dccb1238a7",
                                    "service_type": "volume"
                                },
                                "cinderv2": {
                                    "adminURL": "http://192.168.0.2:8776/v2/329e0576da594c62a911d0dccb1238a7",
                                    "id": "661202afe3e94ab0aa4cc42cd4e1a1b7",
                                    "internalURL": "http://192.168.0.2:8776/v2/329e0576da594c62a911d0dccb1238a7",
                                    "publicURL": "http://172.16.0.2:8776/v2/329e0576da594c62a911d0dccb1238a7",
                                    "service_type": "volumev2"
                                },
                                "glance": {
                                    "adminURL": "http://192.168.0.2:9292",
                                    "id": "161627ffd3034a4cb88bfb94f7b1b981",
                                    "internalURL": "http://192.168.0.2:9292",
                                    "publicURL": "http://172.16.0.2:9292",
                                    "service_type": "image"
                                },
                                "heat": {
                                    "adminURL": "http://192.168.0.2:8004/v1/329e0576da594c62a911d0dccb1238a7",
                                    "id": "4a2a3226ce524e8bb2aaf18e8cdc1c96",
                                    "internalURL": "http://192.168.0.2:8004/v1/329e0576da594c62a911d0dccb1238a7",
                                    "publicURL": "http://172.16.0.2:8004/v1/329e0576da594c62a911d0dccb1238a7",
                                    "service_type": "orchestration"
                                },
                                "heat-cfn": {
                                    "adminURL": "http://192.168.0.2:8000/v1/",
                                    "id": "6369228052f24bf99cb9f08bc337b86d",
                                    "internalURL": "http://192.168.0.2:8000/v1/",
                                    "publicURL": "http://172.16.0.2:8000/v1/",
                                    "service_type": "cloudformation"
                                },
                                "keystone": {
                                    "adminURL": "http://192.168.0.2:35357/v2.0",
                                    "id": "571cd0ea833f4efcbfbd3c8761e38a5a",
                                    "internalURL": "http://192.168.0.2:5000/v2.0",
                                    "publicURL": "http://172.16.0.2:5000/v2.0",
                                    "service_type": "identity"
                                },
                                "neutron": {
                                    "adminURL": "http://192.168.0.2:9696/",
                                    "id": "6ee61e4f01f448febfe73b91ac8ed950",
                                    "internalURL": "http://192.168.0.2:9696/",
                                    "publicURL": "http://172.16.0.2:9696/",
                                    "service_type": "network"
                                },
                                "nova": {
                                    "adminURL": "http://192.168.0.2:8774/v2/329e0576da594c62a911d0dccb1238a7",
                                    "id": "2c0bf9e97f1d42988566781a4a52c7f8",
                                    "internalURL": "http://192.168.0.2:8774/v2/329e0576da594c62a911d0dccb1238a7",
                                    "publicURL": "http://172.16.0.2:8774/v2/329e0576da594c62a911d0dccb1238a7",
                                    "service_type": "compute"
                                },
                                "nova_ec2": {
                                    "adminURL": "http://192.168.0.2:8773/services/Admin",
                                    "id": "05dea4fc9a1f41729c1dc6d9a3929dd0",
                                    "internalURL": "http://192.168.0.2:8773/services/Cloud",
                                    "publicURL": "http://172.16.0.2:8773/services/Cloud",
                                    "service_type": "ec2"
                                }
                            },
                            "id": "RegionOne",
                            "name": "RegionOne",
                            "parent_id": "WebEX-Mirantis@Cisco-regions",
                            "parent_type": "regions_folder"
                    }
}

# FUNCTIONAL TEST

INPUT = None

RESULT = [
    {
        "description": "",
        "enabled": True,
        "id": "75c0eb79ff4a42b0ae4973c8375ddf40",
        "name": "OSDNA-project"
    },
    {
        "description": "admin tenant",
        "enabled": True,
        "id": "8c1751e0ce714736a63fee3c776164da",
        "name": "admin"
    }
]