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

    def get(self, host_id) -> list:
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find node with id={}'.format(host_id))
            return []
        host_name = host['name']
        pod_filter = 'spec.nodeName={}'.format(host_name)
        pods = self.api.list_pod_for_all_namespaces(field_selector=pod_filter)
        ret = []
        for pod in pods.items:
            doc = self.get_pod_details(pod)
            self.set_folder_parent(doc, object_type='pod',
                                   master_parent_type='host',
                                   master_parent_id=host_id)
            doc['type'] = 'pod'
            doc['host'] = host_name
            ret.append(doc)

        self.update_resource_version(
            method='list_pod_for_all_namespaces',
            resource_version=pods.metadata.resource_version
        )

        return ret

    @classmethod
    def get_pod_details(cls, pod: V1Pod):
        doc = {'type': 'pod'}
        try:
            cls.get_pod_metadata(doc, pod.metadata)
        except AttributeError:
            pass
        try:
            cls.get_pod_data(doc, pod.spec)
        except AttributeError:
            pass
        try:
            cls.get_pod_status(doc, pod.status)
        except AttributeError:
            pass
        return doc

    @staticmethod
    def get_pod_metadata(doc: dict, metadata: V1ObjectMeta):
        attrs = ['uid', 'name', 'cluster_name', 'annotations', 'labels',
                 'owner_references', 'namespace']
        for attr in attrs:
            try:
                val = getattr(metadata, attr)
                if val is not None:
                    doc[attr] = val
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
