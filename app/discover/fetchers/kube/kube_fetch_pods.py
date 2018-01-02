###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models import V1Pod, V1ObjectMeta, V1PodSpec, V1PodStatus

from discover.fetchers.kube.kube_access import KubeAccess
from utils.inventory_mgr import InventoryMgr


class KubeFetchPods(KubeAccess):

    def __init__(self, config=None):
        super().__init__(config)
        self.inv = InventoryMgr()

    def get(self, parent_id) -> list:
        node_id = parent_id.replace('-pods', '')
        node = self.inv.get_by_id(self.get_env(), node_id)
        if not node:
            self.log.error('failed to find node with id={}'.format(node_id))
            return []
        pod_filter = 'spec.nodeName={}'.format(node['name'])
        pods = self.api.list_pod_for_all_namespaces(field_selector=pod_filter)
        ret = []
        for pod in pods.items:
            doc = self.get_pod_details(pod)
            host_id = node['name']
            doc.update({
                'type': 'pod',
                'host': host_id,
                'master_parent_type': 'host',
                'master_parent_id': host_id,
                'parent_type': 'pods_folder',
                'parent_id': '{}-pods'.format(host_id)})
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
        try:
            self.get_pod_status(doc, pod.status)
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
        for attr in KubeFetchPods.ATTRBUTES_TO_FETCH:
            try:
                val = getattr(spec, attr)
                KubeAccess.del_attribute_map(val)
                doc[attr] = val
            except AttributeError:
                pass

    @staticmethod
    def get_pod_status(doc: dict, pod_status: V1PodStatus):
        status_data = {}
        for k in dir(pod_status):
            if k.startswith('_'):
                continue
            if k not in [
                    'conditions',
                    'container_statuses',
                    'host_ip',
                    'init_container_statuses',
                    'message', 'phase',
                    'pod_ip', 'qos_class', 'reason', 'start_time']:
                continue
            try:
                val = getattr(pod_status, k)
                if val is None:
                    continue
                status_data[k] = val
            except AttributeError:
                pass
        if status_data:
            doc['status'] = status_data
