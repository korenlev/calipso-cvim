from config.local_config import ENV_CONFIG, MONGODB_CONFIG

ACTUAL_ARGS = {
    'cgi': False,
    'clear': False,
    'cliques_only': False,
    'env': 'Mirantis-Liberty-NVK',
    'id': 'Mirantis-Liberty-NVK',
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': False,
    'links_only': False,
    'loglevel': 'INFO',
    'mongo_config': '',
    'parent_id': '',
    'parent_type': '',
    'scan_self': False,
    'type': 'environment'
}

PAYLOAD_ARGS = {
    'cgi': False,
    'clear': True,
    'cliques_only': True,
    'env': ENV_CONFIG,
    'id': ENV_CONFIG,
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': True,
    'links_only': True,
    'loglevel': 'INFO',
    'mongo_config': MONGODB_CONFIG,
    'parent_id': ENV_CONFIG,
    'parent_type': 'environment',
    'scan_self': False,
    'type': 'environment'
}
ARGS_INVENTORY = {
    'cgi': False,
    'clear': False,
    'cliques_only': False,
    'id': ENV_CONFIG,
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': True,
    'links_only': False,
    'loglevel': 'INFO',
    'mongo_config': '',
    'parent_id': '',
    'parent_type': '',
    'scan_self': False,
    'type': 'environment'
}

ARGS_LINKS = {
    'cgi': False,
    'clear': False,
    'cliques_only': False,
    'id': ENV_CONFIG,
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': False,
    'links_only': True,
    'loglevel': 'INFO',
    'mongo_config': '',
    'parent_id': '',
    'parent_type': '',
    'scan_self': False,
    'type': 'environment'
}

ARGS_CLIQUES = {
    'cgi': False,
    'clear': False,
    'cliques_only': True,
    'id': ENV_CONFIG,
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': False,
    'links_only': False,
    'loglevel': 'INFO',
    'mongo_config': '',
    'parent_id': '',
    'parent_type': '',
    'scan_self': False,
    'type': 'environment'
}
