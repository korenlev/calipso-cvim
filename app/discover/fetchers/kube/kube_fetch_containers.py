###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
from json import JSONDecodeError
from kubernetes.client.models import V1Container

from discover.fetchers.cli.cli_access import CliAccess
from discover.fetchers.kube.kube_access import KubeAccess
from utils.inventory_mgr import InventoryMgr


class KubeFetchContainers(KubeAccess, CliAccess):

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
            ret.append(self.get_container(container, pod, pod_obj))
        return ret

    def get_container(self, container, pod, pod_obj):
        doc = {'type': 'container', 'namespace': pod.metadata.namespace}
        self.get_container_data(doc, container)
        self.fetch_container_status_data(doc, pod, pod_obj)
        self.get_container_config(doc, pod_obj)
        doc['host'] = pod_obj['host']
        doc['id'] = '{}-{}'.format(pod_obj['id'], doc['name'])
        return doc

    def fetch_container_status_data(self, doc, pod, pod_obj):
        container_statuses = pod_obj['status']['container_statuses']
        container_status = next(s for s in container_statuses
                                if s['name'] == doc['name'])
        if not container_status:
            self.log.error('failed to find container_status record '
                           'for container {} in pod {}'
                           .format(doc['name'], pod['name']))
            return
        container_id = container_status['container_id']
        if container_id is None:
            doc['container_type'] = container_status['name']
            doc['container_id'] = container_status['image']
        else:
            id_parts = container_id.split('://')
            doc['container_type'] = id_parts[0]
            doc['container_id'] = id_parts[1]
        doc['container_status'] = container_status

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

    def get_container_config(self, doc, pod_obj):
        cmd = 'docker inspect {}'.format(doc['container_id'])
        output = self.run(cmd, pod_obj['host'])
        try:
            data = json.loads(output)
        except JSONDecodeError as e:
            self.log.error('error reading output of cmd: {}, {}'
                           .format(cmd, str(e)))
            return
        data = data[0]
        if 'Config' in data:
            doc['config'] = data['Config']
            self.get_container_sandbox(doc, pod_obj)

    SANDBOX_ID_ATTR = 'io.kubernetes.sandbox.id'

    def get_container_sandbox(self, doc, pod_obj):
        sandbox_id = doc['config'].get('Labels').get(self.SANDBOX_ID_ATTR)
        cmd = 'docker inspect {}'.format(sandbox_id)
        output = self.run(cmd, pod_obj['host'])
        try:
            data = json.loads(output)
        except JSONDecodeError as e:
            self.log.error('error reading output of cmd: {}, {}'
                           .format(cmd, str(e)))
            return
        doc['sandbox'] = data[0]
