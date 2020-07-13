###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client.models \
    import V1Service, V1ObjectMeta, V1ServiceSpec, V1ServiceStatus

from base.utils.mongo_access import MongoAccess
from scan.fetchers.kube.kube_access import KubeAccess


class KubeFetchVservices(KubeAccess):

    LOAD_BALANCER_ATTR = 'load_balancer'
    STATUS_ATTRIBUTES_TO_FETCH = [LOAD_BALANCER_ATTR]

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

        results = [self.get_service_details(s) for s in services.items]
        # TODO: temporary
        if namespace['name'] == 'cattle-system':
            results.append(self.get_rancher_proxy_service_details())

        return results

    def get_rancher_proxy_service_details(self):
        doc = {
            'id': 'cattle-system-vservice',
            'type': 'vservice',
            'name': 'cattle-system-vservice',
            'service_type': 'proxy',
            'selector': {'calipso-rancher-pod-for-kube-proxy': True}
        }
        doc['pods'] = self.get_service_pods(doc)
        return doc

    def get_service_details(self, service: V1Service):
        doc = {
            **self.get_service_metadata(metadata=service.metadata),
            **self.get_service_data(spec=service.spec),
            **self.get_service_status(service_status=service.status),
            'type': 'vservice',
            'service_type': 'proxy'
        }
        doc['id'] = doc['uid']
        doc['pods'] = self.get_service_pods(doc)
        return doc

    METADATA_ATTRIBUTES_TO_FETCH = [
        'uid', 'name', 'cluster_name', 'annotations', 'labels',
        'owner_references', 'namespace'
    ]

    @classmethod
    def get_service_metadata(cls, metadata: V1ObjectMeta) -> dict:
        return cls.class_to_dict(data_object=metadata, include=cls.METADATA_ATTRIBUTES_TO_FETCH)

    @staticmethod
    def get_service_data(spec: V1ServiceSpec) -> dict:
        data = {}
        for attr in spec.__dict__:
            try:
                val = getattr(spec, attr)
                if val is None:
                    continue
                attr_name = attr[1:] if attr[1:] in spec.attribute_map else attr

                if hasattr(val, "to_dict"):
                    try:
                        val = val.to_dict()
                    except TypeError:
                        continue

                data[attr_name] = val
            except AttributeError:
                continue
        return data

    @classmethod
    def get_service_status(cls, service_status: V1ServiceStatus) -> dict:
        try:
            ingress = getattr(getattr(service_status, cls.LOAD_BALANCER_ATTR), "ingress")
        except AttributeError:
            return {}
        return {cls.LOAD_BALANCER_ATTR: ingress} if ingress else {}

    def get_service_pods(self, service: dict) -> list:
        selectors = service.get('selector')
        if not selectors:
            self.log.warning("No selectors specified for vservice {}".format(service['id']))
            return []

        labels_query = [
            {'labels.{}'.format(MongoAccess.encode_dots(selector)): value}
            for selector, value in selectors.items()
        ]

        cond = {
            'environment': self.env,
            'type': 'pod',
            '$or': labels_query
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
