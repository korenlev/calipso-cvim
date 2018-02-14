###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client import V1Pod, V1Service

from discover.events.event_base import EventBase
from discover.fetchers.kube.kube_fetch_pods import KubeFetchPods
from discover.fetchers.kube.kube_fetch_vservices import KubeFetchVservices


class KubeEventBase(EventBase):

    def __init__(self):
        super().__init__()
        self.object = None
        self.object_id = None
        self.metadata = None

    def handle(self, env, values):
        self.setup(env=env)
        self.object = values['object']
        self.metadata = self.object.metadata
        self.object_id = self.metadata.uid

        self.log.debug("Event: {type}. "
                       "Namespace: {namespace}. "
                       "Object name: {obj_name}, uid: {uid}"
                       .format(type="{} {}".format(values['object'].kind,
                                                   values['type']),
                               namespace=self.metadata.namespace,
                               obj_name=self.metadata.name,
                               uid=self.object_id))

    def save_pod_doc(self, pod: V1Pod = None):
        if not pod:
            pod = self.object

        host_id = pod.spec.node_name
        host_name = pod.spec.node_name

        pods_fetcher = KubeFetchPods()
        pods_fetcher.set_env(self.env)

        doc = pods_fetcher.get_pod_details(pod)
        self.set_folder_parent(doc, object_type='pod',
                               master_parent_type='host',
                               master_parent_id=host_id)
        pods_fetcher.add_pod_to_proxy_service(doc)

        doc['type'] = 'pod'
        doc['environment'] = self.env
        doc['host'] = host_name
        parent = self.inv.get_by_id(environment=self.env,
                                    item_id=doc['parent_id'])

        self.inv.save_inventory_object(o=doc,
                                       parent=parent,
                                       environment=self.env)

    def save_vservice_doc(self, service: V1Service = None):
        if not service:
            service = self.object

        doc = {}
        self.set_folder_parent(doc, object_type='vservice',
                               master_parent_type='environment',
                               master_parent_id=self.env)
        doc.update(KubeFetchVservices.get_service_details(service))
        doc['type'] = 'vservice'  # TODO: fix this in fetcher

        self.inv.save_inventory_object(o=doc,
                                       parent={'environment': self.env,
                                               'id': self.env},
                                       environment=self.env)