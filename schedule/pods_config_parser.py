#!/usr/bin/env python

from yaml import safe_load

from calipso_client import CalipsoClient

try:
    from yaml import CDumper as Dumper
    from yaml.emitter import Emitter
except ImportError:
    from yaml import Dumper
    from yaml.emitter import Emitter


DEFAULTS = {
    'discovery_interval': '24h',
    'replication_interval': '24h',
    'volume_size': '100Gi'
}


# Exclude class tags from dump
Emitter.process_tag = lambda x, *args, **kwargs: None


def auto_repr(cls):
    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )
    cls.__repr__ = __repr__
    return cls


@auto_repr
class PodData:
    def __init__(self, stack, region, metro, name, vip, inv_api_pwd, inv_mongo_pwd, inv_username,
                 discovery_interval, replication_interval):
        self.stack = stack
        self.region = region
        self.metro = metro
        self.name = name
        self.username = inv_username
        self.api_pwd = inv_api_pwd
        self.mongo_pwd = inv_mongo_pwd
        self.discovery_interval = discovery_interval
        self.replication_interval = replication_interval

        vip_parts = vip.split(":")
        if len(vip_parts) == 1:
            self.host = vip
            self.ip_version = 4
        elif len(vip_parts) == 2:
            self.host = vip_parts[0]
            self.ip_version = 4
        else:
            self.host = ":".join(vip_parts[:-1])
            self.ip_version = 6

        self.next_discovery = None
        self.next_replication = None
        self.env_name = None
        self.health = {}
        self.api_client = CalipsoClient(api_host=self.host, api_port=8747, api_password=self.api_pwd)  # TODO: api port?

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )


def get_pods_config(setup_data_file):
    with open(setup_data_file) as setup_data_yaml:
        setup_data = safe_load(setup_data_yaml)

    cvim_mon_stacks = setup_data.get('cvim-mon-stacks', [])
    if not cvim_mon_stacks:
        return []

    pods = []
    for stack in cvim_mon_stacks:

        for region in stack.get('regions', []):
            for metro in region.get('metros', []):
                for pod in metro.get('pods', []):
                    if "inventory_api_password" not in pod or "inventory_mongo_password" not in pod:
                        continue
                    pods.append(PodData(stack=stack['name'],
                                        discovery_interval=stack.get('inventory_discovery_interval',
                                                                     DEFAULTS['discovery_interval']),
                                        replication_interval=stack.get('inventory_replication_interval',
                                                                       DEFAULTS['replication_interval']),
                                        region=region['name'],
                                        metro=metro['name'],
                                        name=pod['name'],
                                        vip=pod['ip'],
                                        inv_username=pod.get('inventory_username', 'calipso'),
                                        inv_api_pwd=pod['inventory_api_password'],
                                        inv_mongo_pwd=pod['inventory_mongo_password']))

    return pods
