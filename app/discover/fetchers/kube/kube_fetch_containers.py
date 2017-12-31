###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models import V1Container

from discover.fetchers.kube.kube_access import KubeAccess
from utils.inventory_mgr import InventoryMgr


class KubeFetchContainers(KubeAccess):

    def __init__(self, config=None):
        super().__init__(config)
        self.inv = InventoryMgr()

    def get(self, parent_id) -> list:
        pod_id = parent_id.replace('-containers', '')
        pod_obj = self.inv.get_by_id(self.get_env(), pod_id)
        if not pod_obj:
            self.log.error('inventory has no pod with uid={}'.format(pod_id))
            return []
        host = pod_obj['host']
        pod_filter = 'spec.nodeName={}'.format(host)
        pods = self.api.list_pod_for_all_namespaces(field_selector=pod_filter)
        ret = []
        if not pods or len(pods.items) == 0:
            self.log.error('failed to find pod with nodeName={}'.format(host))
            return []
        pod = next(pod for pod in pods.items if pod.metadata.uid == pod_id)
        if not pod:
            self.log.error('failed to find pod with uid={}'.format(pod_id))
            return []
        for container in pod.spec.containers:
            doc = {'type': 'container'}
            self.get_container_data(doc, container)
            doc['host'] = pod_obj['host']
            doc['id'] = '{}-{}'.format(pod_id, doc['name'])
            ret.append(doc)
        return ret

    @staticmethod
    def get_container_data(doc: dict, container: V1Container):
        for k in [k for k in dir(container) if not k.startswith('_')]:
            try:
                # TBD a lot of attributes from V1Container fail the saving to DB
                if k in ['to_dict', 'to_str', 'attribute_map', 'swagger_types',
                         'resources',
                         'liveness_probe',
                         'readiness_probe',
                         'security_context']:
                    continue
                val = getattr(container, k)
                if isinstance(val, classmethod):
                    continue
                if isinstance(val, staticmethod):
                    continue
                if val is not None:
                    doc[k] = val
            except AttributeError:
                pass
