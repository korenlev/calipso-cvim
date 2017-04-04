UNIT_TESTS_ENV = "WebEX-Mirantis@Cisco"
UNIT_TESTS_INVENTORY = 'unit_tests'

DEFAULT_ARGUMENTS = {
    "MONGO_CONFIG": "",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "environment",
    "INVENTORY": "inventory",
    "SCAN_SELF": False,
    "ID": UNIT_TESTS_ENV,
    "PARENT_ID": "",
    "PARENT_TYPE": "",
    "ID_FIELD": "id",
    "LOGLEVEL": "INFO",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": False,
    "CLEAR": False
}

SHORT_FLAGS_ARGUMENTS = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR"
}

ARGUMENTS_FULL = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": False,
    "CLEAR": True,
    "CLEAR_ALL": False
}

ARGUMENTS_FULL_CLEAR_ALL = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": False,
    "CLEAR": False,
    "CLEAR_ALL": True
}

ARGUMENTS_FULL_INVENTORY_ONLY = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": True,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": False,
    "CLEAR": True,
    "CLEAR_ALL": False
}

ARGUMENTS_FULL_LINKS_ONLY = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": True,
    "CLIQUES_ONLY": False,
    "CLEAR": True,
    "CLEAR_ALL": False
}

ARGUMENTS_FULL_CLIQUES_ONLY = {
    "MONGO_CONFIG": "mongo_config_file",
    "ENV": UNIT_TESTS_ENV,
    "TYPE": "project",
    "INVENTORY": UNIT_TESTS_INVENTORY,
    "SCAN_SELF": True,
    "ID": "admin",
    "PARENT_ID": "RegionOne",
    "PARENT_TYPE": "Region",
    "ID_FIELD": "name",
    "LOGLEVEL": "ERROR",
    "INVENTORY_ONLY": False,
    "LINKS_ONLY": False,
    "CLIQUES_ONLY": True,
    "CLEAR": True,
    "CLEAR_ALL": False
}

FORM = {
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "type": "region",
    "env": UNIT_TESTS_ENV,
    "id": "RegionOne",
    "parent_id": UNIT_TESTS_ENV + "-regions",
    "parent_type": "regions_folder",
    "id_field": "id",
    "scan_self": False,
    "child_type": "region",
    "child_id": None
}


SCAN_ENV_PLAN_TO_BE_PREPARED = {
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "environment",
    "env": UNIT_TESTS_ENV,
    "id": UNIT_TESTS_ENV,
    "parent_id": "",
    "type_to_scan": "",
    "id_field": "id",
    "scan_self": False,
    "child_type": "environment",
    "child_id": None
}

PREPARED_ENV_PLAN = {
    'obj': {
        'id': UNIT_TESTS_ENV
    },
    'child_id': None,
    'environment': UNIT_TESTS_ENV,
    'inventory_only': False,
    'clear': True,
    'links_only': False,
    'scanner_class': 'ScanEnvironment',
    'object_type': 'environment',
    'id': UNIT_TESTS_ENV,
    'inventory': UNIT_TESTS_INVENTORY,
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': False,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': UNIT_TESTS_ENV
}

SCANNER_CLASS = "ScanEnvironment"
SCANNER_CLASS_FOR_ENV = "ScanEnvironment"
OBJ_ID_FOR_ENV = UNIT_TESTS_ENV
CHILD_TYPE_FOR_ENV = None
CHILD_ID_FOR_ENV = None

PREPARED_ENV_INVENTORY_ONLY_PLAN = {
    'obj': {
        'id': UNIT_TESTS_ENV
    },
    'child_id': None,
    'clear': True,
    'inventory_only': True,
    'links_only': False,
    'scanner_class': 'ScanEnvironment',
    'object_type': 'environment',
    'id': UNIT_TESTS_ENV,
    'inventory': UNIT_TESTS_INVENTORY,
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'cliques_only': False,
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': UNIT_TESTS_ENV
}

PREPARED_ENV_LINKS_ONLY_PLAN = {
    'obj': {
        'id': UNIT_TESTS_ENV
    },
    'child_id': None,
    'clear': True,
    'inventory_only': False,
    'links_only': True,
    'cliques_only': False,
    'scanner_class': 'ScanEnvironment',
    'object_type': 'environment',
    'id': UNIT_TESTS_ENV,
    'inventory': UNIT_TESTS_INVENTORY,
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': UNIT_TESTS_ENV
}

PREPARED_ENV_CLIQUES_ONLY_PLAN = {
    'obj': {
        'id': UNIT_TESTS_ENV
    },
    'child_id': None,
    'clear': True,
    'inventory_only': False,
    'links_only': False,
    'cliques_only': True,
    'scanner_class': 'ScanEnvironment',
    'object_type': 'environment',
    'id': UNIT_TESTS_ENV,
    'inventory': UNIT_TESTS_INVENTORY,
    'loglevel': 'INFO',
    'child_type': None,
    'type_to_scan': '',
    'id_field': 'id',
    'parent_id': '',
    'scan_self': False,
    'env': UNIT_TESTS_ENV
}

SCAN_REGION_FOLDER_PLAN_TO_BE_PREPARED = {
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "regions_folder",
    "env": UNIT_TESTS_ENV,
    "id": UNIT_TESTS_ENV + "-regions",
    "parent_id": UNIT_TESTS_ENV,
    "parent_type": "environment",
    "type_to_scan": "regions_folder",
    "id_field": "id",
    "scan_self": False
}

SCAN_REGION_PLAN_TO_BE_PREPARED = {
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "region",
    "env": UNIT_TESTS_ENV,
    "id": "RegionOne",
    "parent_id": UNIT_TESTS_ENV + "-regions",
    "parent_type": "regions_folder",
    "type_to_scan": "region",
    "id_field": "id",
    "scan_self": False,
    "child_type": "region",
    "child_id": "RegionOne"
}

SCANNER_CLASS_FOR_REGION = "ScanRegionsRoot"
OBJ_ID_FOR_REGION = UNIT_TESTS_ENV + "-regions"
CHILD_TYPE_FOR_REGION = "region"
CHILD_ID_FOR_REGION = "RegionOne"

REGIONS_FOLDER = {
    "id": OBJ_ID_FOR_REGION,
    "create_object": True,
    "name": OBJ_ID_FOR_REGION,
    "text": "",
    "type": "regions_folder",
    "parent_id": UNIT_TESTS_ENV,
    "parent_type": "environment"
}

SCAN_PROJECT_FOLDER_PLAN_TO_BE_PREPARED = {
    "loglevel": "INFO",
    "inventory_only": False,
    "links_only": False,
    "cliques_only": False,
    "clear": True,
    "object_type": "projects_folder",
    "env": UNIT_TESTS_ENV,
    "object_id": UNIT_TESTS_ENV + "-projects",
    "parent_id": UNIT_TESTS_ENV,
    "type_to_scan": "project",
    "id_field": "id",
    "scan_self": False,
    "child_type": "regions_folder",
    "child_id": None
}

SCANNER_CLASS_FOR_REGION_FOLDER = "ScanEnvironment"
OBJ_ID_FOR_REGION_FOLDER = UNIT_TESTS_ENV
CHILD_TYPE_FOR_REGION_FOLDER = "regions_folder"
CHILD_ID_FOR_REGION_FOLDER = UNIT_TESTS_ENV + "-regions"

DEFAULT_COMMAND_ARGS = ["scanner.py"]

SHORT_COMMAND_ARGS = ["scanner.py", "-m", "mongo_config_file",
                      "-e", UNIT_TESTS_ENV, "-t", "project",
                      "-y", UNIT_TESTS_INVENTORY, "-s", "-i", "admin",
                      "-p", "RegionOne", "-a", "Region", "-f", "name",
                      "-l", "ERROR"]

LONG_COMMAND_ARGS = [
    "scanner.py", "--mongo_config", "mongo_config_file",
    "--env", UNIT_TESTS_ENV, "--type", "project",
    "--inventory", UNIT_TESTS_INVENTORY, "--scan_self", "--id", "admin",
    "--parent_id", "RegionOne", "--parent_type", "Region",
    "--id_field", "name", "--loglevel", "ERROR",
    "--clear"]

LONG_COMMAND_ARGS_CLEAR_ALL = [
    "scanner.py", "--mongo_config", "mongo_config_file",
    "--env", UNIT_TESTS_ENV, "--type", "project",
    "--inventory", UNIT_TESTS_INVENTORY, "--scan_self", "--id", "admin",
    "--parent_id", "RegionOne", "--parent_type", "Region",
    "--id_field", "name", "--loglevel", "ERROR",
    "--clear_all"]

LONG_COMMAND_ARGS_INVENTORY_ONLY = [
    "scanner.py", "--mongo_config", "mongo_config_file",
    "--env", UNIT_TESTS_ENV, "--type", "project",
    "--inventory", UNIT_TESTS_INVENTORY, "--scan_self", "--id", "admin",
    "--parent_id", "RegionOne", "--parent_type", "Region",
    "--id_field", "name", "--loglevel", "ERROR", "--inventory_only",
    "--clear"]

LONG_COMMAND_ARGS_LINKS_ONLY = [
    "scanner.py", "--mongo_config", "mongo_config_file",
    "--env", UNIT_TESTS_ENV, "--type", "project",
    "--inventory", UNIT_TESTS_INVENTORY, "--scan_self", "--id", "admin",
    "--parent_id", "RegionOne", "--parent_type", "Region",
    "--id_field", "name", "--loglevel", "ERROR", "--links_only",
    "--clear"]

LONG_COMMAND_ARGS_CLIQUES_ONLY = [
    "scanner.py", "--mongo_config", "mongo_config_file",
    "--env", UNIT_TESTS_ENV, "--type", "project",
    "--inventory", UNIT_TESTS_INVENTORY, "--scan_self", "--id", "admin",
    "--parent_id", "RegionOne", "--parent_type", "Region",
    "--id_field", "name", "--loglevel", "ERROR", "--cliques_only",
    "--clear"]

