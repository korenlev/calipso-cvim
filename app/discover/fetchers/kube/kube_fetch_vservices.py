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


class KubeFetchVservices(KubeAccess):

    def get(self, object_id) -> list:
        parent = self.inv.get_by_id(self.env, object_id)
        if not parent:
            self.log.error('unable to find parent of vService by id: {}'
                           .format(object_id))
            return []
        namespace_id = parent['parent_id']
        namespace = self.inv.get_by_id(self.env, namespace_id)
        if not namespace:
            self.log.error('unable to find namespace of vServices folder '
                           'by id: {}'.format(namespace_id))
            return []
        services = self.api.list_namespaced_service(namespace['name'])

        self.update_resource_version(
            method='list_namespaced_service',
            resource_version=services.metadata.resource_version
        )

        return [self.get_service_details(s) for s in services.items]

    def get_service_details(self, service: V1Service):
        doc = {}
        try:
            self.get_service_metadata(doc, service.metadata)
        except AttributeError:
            pass
        try:
            self.get_service_data(doc, service.spec)
        except AttributeError:
            pass
        try:
            self.get_service_status(doc, service.status)
        except AttributeError:
            pass
        doc['id'] = doc['uid']
        doc['type'] = 'vservice'
        doc['local_service_id'] = doc['name']
        doc['service_type'] = 'proxy'
        KubeAccess.del_attribute_map(doc)
        doc['pods'] = self.get_service_pods(doc)
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

    @classmethod
    def get_app_field(cls, service: dict) -> str:
        selector = service.get('selector', {})
        app_fields = ['k8s-app', 'app']
        for field in app_fields:
            app_name = selector.get(field, '')
            if app_name:
                return field
        return ''

    def get_service_pods(self, service: dict) -> list:
        app_field = self.get_app_field(service)
        if not app_field:
            return []
        app_name = service.get('selector', {}).get(app_field, '')
        cond = {
            'environment': self.env,
            'type': 'pod',
            'labels.{}'.format(app_field): app_name
        }
        pods = []
        for pod in self.inv.find_items(cond):
            pods.append(dict(name=pod['name'], id=pod['id']))
            if 'vservices' not in pod:
                pod['vservices'] = []
            pod['vservices'].append(dict(id=service['id'],
                                         name=service['name']))
            self.inv.set(pod)
        return pods
