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
        pod_filter = 'metadata.uid={}'.format(parent_id)
        pods = self.api.list_pod_for_all_namespaces(field_selector=pod_filter)
        ret = []
        if not pods or len(pods.items) == 0:
            self.log.error('failed to find pod with uid={}'.format(parent_id))
            return []
        if len(pods.items) > 1:
            self.log.error('found multiple matches for pod with uid={}'
                           .format(parent_id))
            return []
        pod_obj = self.inv.get_by_id(self.get_env(), parent_id)
        if not pod_obj:
            self.log.error('inventory has no pod with uid={}'.format(parent_id))
            return []
        pod = pods.items[0]
        for container in pod.spec.containers:
            doc = {'type': 'container'}
            self.get_container_data(doc, container)
            doc['host'] = pod_obj['host']
            ret.append(doc)
        return ret

    @staticmethod
    def get_container_data(doc: dict, container: V1Container):
        if 'container-role.kubernetes.io/master' in doc['labels']:
            doc['host_type'].append('Kube-master')
        for k in [k for k in dir(container) if not k.startswith('_')]:
            try:
                val = getattr(container, k)
                KubeAccess.del_attribute_map(val)
                doc[k] = val
            except AttributeError:
                pass
