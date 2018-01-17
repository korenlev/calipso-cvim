
ENVIRONMENT = {
    'name': 'test-env',
    'environment_type': 'OpenStack',
    'distribution': 'Mirantis',
    'distribution_version': '9.0',
    'mechanism_drivers': ['OVS'],
    'type_drivers': 'vxlan'
}

CLIQUE_TYPES = [
    {
        'name': 'environment match',
        'clique_type': {
            'environment': 'test-env',
            'link_types': []},
        'score': 6
    },
    {
        'name': 'distribution and version match',
        'clique_type': {
            'environment_type': 'OpenStack',
            'distribution': 'Mirantis',
            'distribution_version': '9.0',
            'mechanism_drivers': 'VPP',
            'type_drivers': 'vlan',
            'link_types': []
        },
        'score': 5
    },
    {
        'name': 'mechanism drivers match',
        'clique_type': {
            'environment_type': 'OpenStack',
            'distribution': 'Apex',
            'distribution_version': 'Euphrates',
            'mechanism_drivers': 'OVS',
            'type_drivers': 'vlan',
            'link_types': []
        },
        'score': 3
    },
    {
        'name': 'type drivers match',
        'clique_type': {
            'environment_type': 'OpenStack',
            'distribution': 'Apex',
            'distribution_version': 'Euphrates',
            'mechanism_drivers': 'VPP',
            'type_drivers': 'vxlan',
            'link_types': []
        },
        'score': 2
    },
    {
        'name': 'ANY fallback',
        'clique_type': {
            'environment': 'ANY',
            'link_types': []
        },
        'score': 1
    },
    {
        'name': 'No environment name match',
        'clique_type': {
            'environment': 'test-env-2',
            'link_types': []
        },
        'score': 0
    },
    {
        'name': 'No configuration match',
        'clique_type': {
            'environment_type': 'OpenStack',
            'distribution': 'Apex',
            'distribution_version': 'Euphrates',
            'mechanism_drivers': 'VPP',
            'type_drivers': 'vlan',
            'link_types': []
        },
        'score': 0
    },
    {
        'name': 'No environment type match',
        'clique_type': {
            'environment_type': 'Kubernetes',
            'distribution': 'Kubernetes',
            'distribution_version': '1.9',
            'mechanism_drivers': 'Flannel',
            'type_drivers': 'vxlan',
            'link_types': []
        },
        'score': 0
    },
]
