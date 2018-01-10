###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models import V1Node, V1ObjectMeta, V1NodeSpec

from discover.fetchers.cli.cli_access import CliAccess
from discover.fetchers.kube.kube_access import KubeAccess


class KubeFetchNodes(KubeAccess, CliAccess):

    def __init__(self, config=None):
        super().__init__(config)

    def get(self, object_id):
        nodes = self.api.list_node()
        ret = []
        for node in nodes.items:
            ret.append(self.get_node_details(node))
        return ret

    def get_node_details(self, node: V1Node):
        doc = {'type': 'host'}
        try:
            self.get_node_metadata(doc, node.metadata)
            doc['host'] = doc.get('name', '')
        except AttributeError:
            pass
        try:
            self.get_node_data(doc, node.spec)
        except AttributeError:
            pass
        self.get_host_interfaces(doc)
        return doc

    @staticmethod
    def get_node_metadata(doc: dict, metadata: V1ObjectMeta):
        attrs = ['uid', 'name', 'cluster_name', 'annotations', 'labels']
        for attr in attrs:
            try:
                doc[attr] = getattr(metadata, attr)
            except AttributeError:
                pass
        doc['id'] = doc['name']
        doc['host_type'] = ['Network', 'Compute']

    @staticmethod
    def get_node_data(doc: dict, spec: V1NodeSpec):
        if 'node-role.kubernetes.io/master' in doc['labels']:
            doc['host_type'].append('Kube-master')
        attrs = ['pod_cidr', 'provider_id', 'taints', 'unschedulable']
        for attr in attrs:
            try:
                doc[attr] = getattr(spec, attr)
            except AttributeError:
                pass

    def get_host_interfaces(self, host):
        cmd = 'ip link show'
        lines = self.run_fetch_lines(cmd, host['host'])
        interface_lines = []
        interfaces = {}
        for line in lines:
            interface_lines.append(line)
            if len(interface_lines) == 2:
                interface = self.get_host_interface(interface_lines)
                interfaces[interface['id']] = interface
                interface_lines = []
        host['interfaces'] = interfaces

    def get_host_interface(self, interface_lines):
        interface = {'lines': interface_lines}
        regexps = [
            {'name': 'index', 're': '^([0-9]+):\s'},
            {'name': 'id', 're': '^[0-9]+:\s([^@:]+)'},
            {'name': 'state', 're': '^.*,(UP),', 'default': 'DOWN'},
            {'name': 'mac_address', 're': '.*\slink/ether\s(\S+)\s'},
            {'name': 'mtu', 're': '.*\smtu\s(\S+)\s'},
        ]
        self.get_object_data(interface, interface_lines, regexps)
        return interface
