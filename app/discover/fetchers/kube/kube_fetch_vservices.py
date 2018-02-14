###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models \
    import V1Service, V1ObjectMeta, V1ServiceSpec, V1ServiceStatus

from discover.fetchers.kube.kube_access import KubeAccess
from utils.inventory_mgr import InventoryMgr


class KubeFetchVservices(KubeAccess):

    def __init__(self, config=None):
        super().__init__(config)
        self.inv = InventoryMgr()

    def get(self, object_id) -> list:
        services = self.api.list_service_for_all_namespaces()

        self.update_resource_version(
            method='list_service_for_all_namespaces',
            resource_version=services.metadata.resource_version
        )

        return [self.get_service_details(s) for s in services.items]

    @classmethod
    def get_service_details(cls, service: V1Service):
        doc = {'type': 'vservice'}
        try:
            cls.get_service_metadata(doc, service.metadata)
        except AttributeError:
            pass
        try:
            cls.get_service_data(doc, service.spec)
        except AttributeError:
            pass
        try:
            cls.get_service_status(doc, service.status)
        except AttributeError:
            pass
        doc['id'] = doc['uid']
        doc['local_service_id'] = doc['name']
        doc['service_type'] = 'proxy'
        KubeAccess.del_attribute_map(doc)
        return doc

    METADATA_ATTRIBUTES_TO_FETCH = [
        'uid', 'name', 'cluster_name', 'annotations', 'labels',
        'owner_references', 'namespace'
    ]

    @staticmethod
    def get_service_metadata(doc: dict, metadata: V1ObjectMeta):
        for attr in KubeFetchVservices.METADATA_ATTRIBUTES_TO_FETCH:
            try:
                val = getattr(metadata, attr)
                if val is not None:
                    doc[attr] = val
            except AttributeError:
                pass
        doc['id'] = doc['uid']

    @staticmethod
    def get_service_data(doc: dict, spec: V1ServiceSpec):
        for attr, val in spec.__dict__.items():
            try:
                val = getattr(spec, attr)
                if val is None:
                    continue
                attr_name = attr[1:] if attr[1:] in spec.attribute_map else attr
                KubeAccess.del_attribute_map(val)
                doc[attr_name] = val
            except AttributeError:
                pass

    STATUS_ATTRIBUTES_TO_FETCH = ['load_balancer']

    LOAD_BALANCER_ATTR = 'load_balancer'

    @staticmethod
    def get_service_status(doc: dict, service_status: V1ServiceStatus):
        load_balancer = getattr(service_status,
                                KubeFetchVservices.LOAD_BALANCER_ATTR)
        if not load_balancer.get('ingress'):
            return
        doc['status'] = {KubeFetchVservices.LOAD_BALANCER_ATTR: load_balancer}
