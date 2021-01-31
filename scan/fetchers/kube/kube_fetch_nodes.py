###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re
from typing import List

from kubernetes.client.models import V1Node, V1ObjectMeta, V1NodeSpec, \
    V1NodeStatus

from base.utils.constants import HostType
from base.utils.exceptions import SshError, ScanError
from base.utils.origins import Origin
from scan.fetchers.cli.cli_fetch_host_details import CliFetchHostDetails
from scan.fetchers.cli.cli_fetch_interface_details \
    import CliFetchInterfaceDetails
from scan.fetchers.kube.kube_access import KubeAccess


class KubeFetchNodes(KubeAccess, CliFetchHostDetails):

    METADATA_ATTRIBUTES = ['uid', 'name', 'cluster_name', 'annotations', 'labels']
    SPEC_ATTRIBUTES = ['pod_cidr', 'provider_id', 'taints', 'unschedulable']

    IP_SHOW_CMD = 'ip address show'
    ID_REGEX = re.compile('^[0-9]+:\s([^@:]+)')

    def __init__(self, config=None):
        super().__init__(config)
        self.details_fetcher = None

    def setup(self, env, origin: Origin = None):
        self.details_fetcher = CliFetchInterfaceDetails()
        super().setup(env, origin)

    def set_env(self, env):
        super().set_env(env)
        self.details_fetcher.set_env(env)

    def get(self, object_id):
        nodes = self.api.list_node()
        ret = []
        for node in nodes.items:
            try:
                ret.append(self.get_node_details(node))
            except SshError as e:
                ret.append(e)

        self.update_resource_version(
            method='list_node',
            resource_version=nodes.metadata.resource_version
        )

        return ret

    def get_node_details(self, node: V1Node):
        doc = {'type': 'host'}
        doc.update(self.get_node_metadata(metadata=node.metadata))
        doc.update(self.get_node_data_from_spec(spec=node.spec))
        doc.update(self.get_node_data_from_status(status=node.status))

        doc.update({
            'id': doc['name'],
            'host': doc['name'],
            'host_type': [HostType.NETWORK.value, HostType.COMPUTE.value],
            'ip_address': next((addr.address for addr in doc['addresses'] if addr.type == 'InternalIP'), None),
            'node_info': self.class_to_dict(data_object=doc['node_info']),
            'interfaces': self.get_host_interfaces(host_id=doc['name'])
        })
        if 'node-role.kubernetes.io/master' in doc['labels']:
            doc['host_type'].append(HostType.KUBEMASTER.value)

        self.update_host_os_details(doc)
        return doc

    @classmethod
    def get_node_metadata(cls, metadata: V1ObjectMeta) -> dict:
        return cls.class_to_dict(data_object=metadata, include=cls.METADATA_ATTRIBUTES)

    @classmethod
    def get_node_data_from_spec(cls, spec: V1NodeSpec) -> dict:
        return cls.class_to_dict(data_object=spec, include=cls.SPEC_ATTRIBUTES)

    @classmethod
    def get_node_data_from_status(cls, status: V1NodeStatus) -> dict:
        return cls.class_to_dict(data_object=status, exclude=['daemon_endpoints'])

    def get_interface_data(self, interface_name, interface_lines, host_id) -> dict:
        ethtool_cmd = 'ethtool {}'.format(interface_name)
        ethtool_lines = self.run_fetch_lines(ethtool_cmd, ssh_to_host=host_id, find_route_to_host=False)
        return self.details_fetcher.get_interface_details(host_id=host_id,
                                                          interface_name=interface_name,
                                                          ip_lines=interface_lines,
                                                          ethtool_lines=ethtool_lines)

    def get_host_interfaces(self, host_id: str) -> List[dict]:
        lines = self.run_fetch_lines(self.IP_SHOW_CMD, ssh_to_host=host_id, find_route_to_host=False)
        if not lines:
            raise ScanError('No output returned by command: {}'.format(self.IP_SHOW_CMD))

        interface_lines = []
        interface_name = None
        interfaces = []
        for line in lines:
            # look for interfaces sections in the output of 'ip address show'
            matches = self.ID_REGEX.match(line)
            if not matches:
                # add more lines to an already discovered interface
                interface_lines.append(line)
                continue
            if interface_lines and interface_name != 'lo':
                # handle previous section
                interface = self.get_interface_data(interface_name, interface_lines, host_id)
                interfaces.append(interface)

            interface_lines = []
            interface_name = matches.group(1)
            interface_lines.append(line)

        if interface_lines:
            # add last interface
            interface = self.get_interface_data(interface_name, interface_lines, host_id)
            interfaces.append(interface)

        return interfaces
