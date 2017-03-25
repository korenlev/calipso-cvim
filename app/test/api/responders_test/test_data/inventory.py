URL = "/inventory"

ID = "RegionOne-aggregates"


OBJECTS_LIST = [
    {
        "id": "Mirantis-Liberty-regions",
        "name": "Regions",
        "name_path": "/Mirantis-Liberty-API/Regions"
    },
    {
        "id": "Mirantis-Liberty-projects",
        "name": "Projects",
        "name_path": "/Mirantis-Liberty-API/Projects"
    }
]

OBJECT_IDS_RESPONSE = {
    "objects": OBJECTS_LIST
}


OBJECTS = [{
  "environment": "Mirantis-Liberty-API",
  "id": "RegionOne-aggregates"
}]
