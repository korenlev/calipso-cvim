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

from discover.fetchers.kube.kube_access import KubeAccess


class KubeFetchNodes(KubeAccess):

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
        doc['host_type'] = ['Kube-node']

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
