DEFAULT_ARGUMENTS = {
    "CGI": False,
    "MONGO_CONFIG": "",
    "ENV": "WebEX-Mirantis@Cisco",
    "TYPE": "environment",
    "INVENTORY": "inventory",
    "SCAN_SELF": False,
    "ID": "WebEX-Mirantis@Cisco",
    "PARENT_ID": "",
    "PARENT_TYPE": "",
    "ID_FIELD": "id",
    "LOGLEVEL": "INFO",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": False,
    "CLEAR": False
}

ARGUMENTS = {
    "CGI": True,
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": "Mirantis-Liberty-Xiaocong",
    "TYPE": "project",
    "INVENTORY": "Xiaocong-UT",
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": True,
    "LINKS_ONLY": True,
    "CLIQUES_ONLY": True,
    "CLEAR": True
}

FORM = {
    "cgi": False,
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "type": "region",
    "env": "WebEX-Mirantis@Cisco",
    "id": "RegionOne",
    "parent_id": "WebEX-Mirantis@Cisco-regions",
    "parent_type": "regions_folder",
    "id_field": "id",
    "scan_self": False,
    "child_type": "region",
    "child_id": None
}

CGI_PLAN = {
    'links_only': False,
    'inventory_only': False,
    'type_to_scan': 'regions_folder',
    'object_id': 'RegionOne',
    'scan_self': False,
    'cgi': True,
    'parent_id': 'WebEX-Mirantis@Cisco-regions',
    'cliques_only': False,
    'id_field': 'id',
    'clear': True,
    'object_type': 'region',
    'env': 'WebEX-Mirantis@Cisco',
    'loglevel': 'INFO'
}

SCAN_ENV_PLAN_TO_BE_PREPARED = {
    "cgi": False,
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "environment",
    "env": "WebEX-Mirantis@Cisco",
    "object_id": "WebEX-Mirantis@Cisco",
    "parent_id": "",
    "type_to_scan": "",
    "id_field": "id",
    "scan_self": False,
    "child_type": "environment",
    "child_id": None
}

PREPARED_ENV_PLAN = {
    'obj': {
        'id': 'WebEX-Mirantis@Cisco'
    },
    'child_id': None,
    'cgi': False,
    'inventory_only': False,
    'clear': True,
    'links_only': False,
    'module_file': 'scan_environment',
    'scanner_class': 'ScanEnvironment',
    'object_type': 'Environment',
    'object_id': 'WebEX-Mirantis@Cisco',
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': False,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': 'WebEX-Mirantis@Cisco'
}

MODULE_NAME_FOR_IMPORT = 'scan_environment'
SCANNER_CLASS = "ScanEnvironment"
SCANNER_CLASS_FOR_ENV = "ScanEnvironment"
OBJ_ID_FOR_ENV = "WebEX-Mirantis@Cisco"
CHILD_TYPE_FOR_ENV = None
CHILD_ID_FOR_ENV = None

PREPARED_ENV_INVENTORY_ONLY_PLAN = {
    'obj': {
        'id': 'WebEX-Mirantis@Cisco'
    },
    'child_id': None,
    'cgi': False,
    'inventory_only': True,
    'clear': True,
    'links_only': False,
    'module_file': 'scan_environment',
    'scanner_class': 'ScanEnvironment',
    'object_type': 'Environment',
    'object_id': 'WebEX-Mirantis@Cisco',
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': False,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': 'WebEX-Mirantis@Cisco'
}

PREPARED_ENV_LINKS_ONLY_PLAN = {
    'obj': {
        'id': 'WebEX-Mirantis@Cisco'
    },
    'child_id': None,
    'cgi': False,
    'inventory_only': False,
    'clear': True,
    'links_only': True,
    'module_file': 'scan_environment',
    'scanner_class': 'ScanEnvironment',
    'object_type': 'Environment',
    'object_id': 'WebEX-Mirantis@Cisco',
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': False,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': 'WebEX-Mirantis@Cisco'
}

PREPARED_ENV_CLIQUES_ONLY_PLAN = {
    'obj': {
        'id': 'WebEX-Mirantis@Cisco'
    },
    'child_id': None,
    'cgi': False,
    'inventory_only': False,
    'clear': True,
    'links_only': False,
    'module_file': 'scan_environment',
    'scanner_class': 'ScanEnvironment',
    'object_type': 'Environment',
    'object_id': 'WebEX-Mirantis@Cisco',
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': True,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': 'WebEX-Mirantis@Cisco'
}

SCAN_REGION_PLAN_TO_BE_PREPARED = {
    "cgi": False,
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "region",
    "env": "WebEX-Mirantis@Cisco",
    "object_id": "RegionOne",
    "parent_id": "WebEX-Mirantis@Cisco-regions",
    "type_to_scan": "regions_folder",
    "id_field": "id",
    "scan_self": False,
    "child_type": "region",
    "child_id": None
}

SCANNER_CLASS_FOR_REGION = "ScanRegionsRoot"
OBJ_ID_FOR_REGION = "WebEX-Mirantis@Cisco-regions"
CHILD_TYPE_FOR_REGION = "region"
CHILD_ID_FOR_REGION = "RegionOne"

REGIONS_FOLDER = {
    "id": "WebEX-Mirantis@Cisco-regions",
    "create_object": True,
    "name": "WebEX-Mirantis@Cisco-regions",
    "text": "",
    "type": "regions_folder",
    "parent_id": "WebEX-Mirantis@Cisco",
    "parent_type": "environment"
}

SCAN_PROJECT_FOLDER_PLAN_TO_BE_PREPARED = {
    "cgi": False,
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "regions_folder",
    "env": "WebEX-Mirantis@Cisco",
    "object_id": "WebEX-Mirantis@Cisco-regions",
    "parent_id": "WebEX-Mirantis@Cisco",
    "type_to_scan": "environment",
    "id_field": "id",
    "scan_self": False,
    "child_type": "regions_folder",
    "child_id": None
}

SCANNER_CLASS_FOR_REGION_FOLDER = "ScanEnvironment"
OBJ_ID_FOR_REGION_FOLDER = "WebEX-Mirantis@Cisco"
CHILD_TYPE_FOR_REGION_FOLDER = "regions_folder"
CHILD_ID_FOR_REGION_FOLDER = "WebEX-Mirantis@Cisco-regions"

DEFAULT_COMMAND_ARGS = ["scanner.py"]

SHORT_COMMAND_ARGS = ["scanner.py", "-c", "True", "-m", "mongo_config_file", "-e", "Mirantis-Liberty-Xiaocong",
        "-t", "project", "-y", "Xiaocong-UT", "-s", "-i", "admin", "-p", "RegionOne",
        "-a", "Region", "-f", "name", "-l", "ERROR", "--inventory_only", "--links_only",
        "--cliques_only", "--clear"]

LONG_COMMAND_ARGS = ["scanner.py", "--cgi", "True", "--mongo_config", "mongo_config_file", "--env", "Mirantis-Liberty-Xiaocong",
        "--type", "project", "--inventory", "Xiaocong-UT", "--scan_self", "--id", "admin", "--parent_id", "RegionOne",
        "--parent_type", "Region", "--id_field", "name", "--loglevel", "ERROR", "--inventory_only", "--links_only",
        "--cliques_only", "--clear"]

