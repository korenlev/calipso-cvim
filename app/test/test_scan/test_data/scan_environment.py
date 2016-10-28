from config.local_config import ENV_CONFIG

REGIONS = "regions"
ENVIRONMENT = "environment"

folder_fetcher = (REGIONS, ENVIRONMENT)


types_of_fetches = [
    {
        "type": "regions_folder",
        "children_scanner": "ScanRegionsRoot"
    },
    {
        "type": "projects_folder",
        "children_scanner": "ScanProjectsRoot"
    }
]

obj = {
    'id': ENV_CONFIG,
    'id_path': '/Mirantis-Liberty-NVK/Mirantis-Liberty-NVK-projects',
    'name_path': '/Mirantis-Liberty-NVK/Projects'

}
id_field = 'id'
child_id = ''
child_type = ''


