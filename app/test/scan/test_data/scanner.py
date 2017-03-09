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
            "key": "/Users/ngrandhi/.ssh/id_rsa",
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
    "name": "Mirantis-Liberty-Nvn",
    "mechanism_drivers": [
        "OVS"
    ],
    "operational": "yes",
    "type": "environment"
}

TYPES_TO_FETCHES_FOR_PNIC = {
    "type": "pnic",
    "fetcher": "CliFetchHostPnicsVpp",
    "environment_condition": {"mechanism_drivers": "VPP"},
    "children_scanner": "ScanOteps"
}

TYPES_TO_FETCHES_FOR_PNIC_WITHOUT_ENV_CON = {
    "type": "pnic",
    "fetcher": "CliFetchHostPnicsVpp",
    "children_scanner": "ScanOteps"
}

TYPES_TO_FETCHES_FOR_SCAN_AGGREGATE = [{
    "type": "host_ref",
    "fetcher": "DbFetchAggregateHosts"
}]




# id = 'RegionOne-aggregates'
# obj = self.inv.get_by_id(self.env, id)
obj = {'id': 'Mirantis-Liberty-Nvn'}
id_field = 'id'
child_id = '',
child_type = ''


child_data = [
    {
        'id_path': '/Mirantis-Liberty-Nvn/Mirantis-Liberty-Nvn-regions',
        'object_name': 'Regions',
        'parent_id': 'Mirantis-Liberty-Nvn',
        'environment': 'Mirantis-Liberty-Nvn',
        'id': 'Mirantis-Liberty-Nvn-regions',
        'show_in_tree': True,
        'text': 'Regions',
        'type': 'regions_folder',
        'name': 'Regions',
        'create_object': True,
        'name_path': '/Mirantis-Liberty-Nvn/Regions',
        'parent_type': 'environment'
    }
]


