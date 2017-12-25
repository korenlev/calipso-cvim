###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models import V1Pod, V1ObjectMeta, V1PodSpec

from discover.fetchers.kube.kube_access import KubeAccess
from utils.inventory_mgr import InventoryMgr


class KubeFetchPods(KubeAccess):

    def __init__(self, config=None):
        super().__init__(config)
        self.inv = InventoryMgr()

    def get(self, parent_id) -> list:
        node = self.inv.get_by_id(self.get_env(), parent_id)
        if not node:
            self.log.error('failed to find node with id={}'.format(parent_id))
            return []
        pod_filter = 'spec.nodeName={}'.format(node['name'])
        pods = self.api.list_pod_for_all_namespaces(field_selector=pod_filter)
        ret = []
        for pod in pods.items:
            doc = self.get_pod_details(pod)
            doc['host'] = node['name']
            ret.append(doc)
        return ret

    def get_pod_details(self, pod: V1Pod):
        doc = {'type': 'pod'}
        try:
            self.get_pod_metadata(doc, pod.metadata)
        except AttributeError:
            pass
        try:
            self.get_pod_data(doc, pod.spec)
        except AttributeError:
            pass
        return doc

    @staticmethod
    def get_pod_metadata(doc: dict, metadata: V1ObjectMeta):
        attrs = ['uid', 'name', 'cluster_name', 'annotations', 'labels']
        for attr in attrs:
            try:
                doc[attr] = getattr(metadata, attr)
            except AttributeError:
                pass
        doc['id'] = doc['uid']

    ATTRBUTES_TO_FETCH = [
        'containers',
        'node_name',
        'scheduler_name',
        'dns_policy',
        'termination_grace_period_seconds',
        'tolerations',
        'volumes'
    ]

    @staticmethod
    def get_pod_data(doc: dict, spec: V1PodSpec):
        if 'pod-role.kubernetes.io/master' in doc['labels']:
            doc['host_type'].append('Kube-master')
        for attr in KubeFetchPods.ATTRBUTES_TO_FETCH:
            try:
                val = getattr(spec, attr)
                KubeAccess.del_attribute_map(val)
                doc[attr] = val
            except AttributeError:
                pass
