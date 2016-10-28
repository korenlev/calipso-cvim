from config.local_config import ENV_CONFIG

types_of_fetches = [
    {
        "type": "aggregate",
        "fetcher": "DbFetchAggregates",
        "children_scanner": "ScanAggregate"
    }
]

obj = {
    'id': ENV_CONFIG,
    'id_path': "/Mirantis-Liberty-NVK/Mirantis-Liberty-NVK-regions/RegionOne/RegionOne-availability_zones/",
    'name_path': "/Mirantis-Liberty-NVK/Regions/RegionOne/Availability Zones/",
    'type': 'regions_folder',
    'show_in_tree': True,
    'create_object': True
}
id_field = 'id'
child_id = ''
child_type = ''
