AGGREGATE = {
    "environment" : "Mirantis-Liberty-Xiaocong",
    "id" : "1",
    "id_path" : "/Mirantis-Liberty-Xiaocong/Mirantis-Liberty-Xiaocong-regions/RegionOne/RegionOne-aggregates/1",
    "name" : "osdna-agg",
    "name_path" : "/Mirantis-Liberty-Xiaocong/Regions/RegionOne/Aggregates/osdna-agg",
    "object_name" : "osdna-agg",
    "parent_id" : "RegionOne-aggregates",
    "parent_type" : "aggregates_folder",
    "show_in_tree" : True,
    "type" : "aggregate"
}

HOSTS = [
    {
        "id": "aggregate-osdna-agg-node-5.cisco.com",
        "name": "node-5.cisco.com"
    }
]

# functional test
INPUT = "1"
OUTPUT = [
    {
        "id": "aggregate-osdna-agg-node-5.cisco.com",
        "name": "node-5.cisco.com"
    }
]