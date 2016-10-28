REGION = {
    "endpoints" : {
        "neutron" : {
            "id" : "8dc28584da224c4b9671171ead3c982a",
            "adminURL" : "http://192.168.0.2:9696",
            "service_type" : "network",
            "publicURL" : "http://172.16.0.3:9696",
            "internalURL" : "http://192.168.0.2:9696"
        },
        "cinderv2" : {
            "id" : "2c30937688e944889db4a64fab6816e6",
            "adminURL" : "http://192.168.0.2:8776/v2/8c1751e0ce714736a63fee3c776164da",
            "service_type" : "volumev2",
            "publicURL" : "http://172.16.0.3:8776/v2/8c1751e0ce714736a63fee3c776164da",
            "internalURL" : "http://192.168.0.2:8776/v2/8c1751e0ce714736a63fee3c776164da"
        },
        "swift_s3" : {
            "id" : "4f655c8f2bef46a0a7ba4a20bba53666",
            "adminURL" : "http://192.168.0.2:8080",
            "service_type" : "s3",
            "publicURL" : "http://172.16.0.3:8080",
            "internalURL" : "http://192.168.0.2:8080"
        },
        "cinder" : {
            "id" : "05643f2cf9094265b432376571851841",
            "adminURL" : "http://192.168.0.2:8776/v1/8c1751e0ce714736a63fee3c776164da",
            "service_type" : "volume",
            "publicURL" : "http://172.16.0.3:8776/v1/8c1751e0ce714736a63fee3c776164da",
            "internalURL" : "http://192.168.0.2:8776/v1/8c1751e0ce714736a63fee3c776164da"
        },
        "novav3" : {
            "id" : "1df917160dfb4ce5b469764fde22b3ab",
            "adminURL" : "http://192.168.0.2:8774/v3",
            "service_type" : "computev3",
            "publicURL" : "http://172.16.0.3:8774/v3",
            "internalURL" : "http://192.168.0.2:8774/v3"
        },
        "heat" : {
            "id" : "9e60268a5aaf422d9e42f0caab0a19b4",
            "adminURL" : "http://192.168.0.2:8004/v1/8c1751e0ce714736a63fee3c776164da",
            "service_type" : "orchestration",
            "publicURL" : "http://172.16.0.3:8004/v1/8c1751e0ce714736a63fee3c776164da",
            "internalURL" : "http://192.168.0.2:8004/v1/8c1751e0ce714736a63fee3c776164da"
        },
        "ceilometer" : {
            "id" : "617177a3dcb64560a5a79ab0a91a7225",
            "adminURL" : "http://192.168.0.2:8777",
            "service_type" : "metering",
            "publicURL" : "http://172.16.0.3:8777",
            "internalURL" : "http://192.168.0.2:8777"
        },
        "heat-cfn" : {
            "id" : "0f04ec6ed49f4940822161bf677bdfb2",
            "adminURL" : "http://192.168.0.2:8000/v1",
            "service_type" : "cloudformation",
            "publicURL" : "http://172.16.0.3:8000/v1",
            "internalURL" : "http://192.168.0.2:8000/v1"
        },
        "keystone" : {
            "id" : "404cceb349614eb39857742970408301",
            "adminURL" : "http://192.168.0.2:35357/v2.0",
            "service_type" : "identity",
            "publicURL" : "http://172.16.0.3:5000/v2.0",
            "internalURL" : "http://192.168.0.2:5000/v2.0"
        },
        "nova_ec2" : {
            "id" : "390dddc753cc4d378b489129d06c4b7d",
            "adminURL" : "http://192.168.0.2:8773/services/Admin",
            "service_type" : "ec2",
            "publicURL" : "http://172.16.0.3:8773/services/Cloud",
            "internalURL" : "http://192.168.0.2:8773/services/Cloud"
        },
        "nova" : {
            "id" : "274cbbd9fd6d4311b78e78dd3a1df51f",
            "adminURL" : "http://192.168.0.2:8774/v2/8c1751e0ce714736a63fee3c776164da",
            "service_type" : "compute",
            "publicURL" : "http://172.16.0.3:8774/v2/8c1751e0ce714736a63fee3c776164da",
            "internalURL" : "http://192.168.0.2:8774/v2/8c1751e0ce714736a63fee3c776164da"
        },
        "glance" : {
            "id" : "475c6c77a94e4e63a5a0f0e767f697a8",
            "adminURL" : "http://192.168.0.2:9292",
            "service_type" : "image",
            "publicURL" : "http://172.16.0.3:9292",
            "internalURL" : "http://192.168.0.2:9292"
        },
        "swift" : {
            "id" : "12e78e06595f48339baebdb5d4309c70",
            "adminURL" : "http://192.168.0.2:8080/v1/AUTH_8c1751e0ce714736a63fee3c776164da",
            "service_type" : "object-store",
            "publicURL" : "http://172.16.0.3:8080/v1/AUTH_8c1751e0ce714736a63fee3c776164da",
            "internalURL" : "http://192.168.0.2:8080/v1/AUTH_8c1751e0ce714736a63fee3c776164da"
        }
    },
    "environment" : "Mirantis-Liberty-Xiaocong",
    "id" : "RegionOne",
    "id_path" : "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne",
    "name" : "RegionOne",
    "name_path" : "/Mirantis-Liberty-Xiaocong/Regions/RegionOne",
    "object_name" : "RegionOne",
    "parent_id" : "Mirantis-Liberty-Xiaocong-regions",
    "parent_type" : "regions_folder",
    "show_in_tree" : True,
    "type" : "region"
}

OBJECTS_LIST = [
    {
        "id": 1,
        "name": "osdna-agg"
    }
]

# functional test
INPUT = "RegionOne"
RESULT = [
    {
        "id": 1,
        "name": "osdna-agg"
    }
]