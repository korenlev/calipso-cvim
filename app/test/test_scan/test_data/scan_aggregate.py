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

SCAN_AGGREGATE = {
    'cgi': False,
    'clear': False,
    'cliques_only': False,
    'env': ENV_CONFIG,
    'id': ENV_CONFIG,
    'id_field': 'id',
    'inventory': 'inventory',
    'inventory_only': False,
    'links_only': False,
    'loglevel': 'INFO',
    'mongo_config': MONGODB_CONFIG,
    'parent_id': '',
    'parent_type': '',
    'scan_self': False,
    'type': 'aggregate`'
}

types_of_fetches = [
            {
                "type": "host_ref",
                "fetcher": "DbFetchAggregateHosts"
            }
        ]

OBJECT = ENV_CONFIG

obj = {'id': OBJECT}
id_field = SCAN_AGGREGATE['id_field']
child_id = ''
child_type = ''
