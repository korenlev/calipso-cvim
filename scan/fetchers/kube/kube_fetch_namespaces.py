###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from kubernetes.client import V1Namespace

from scan.fetchers.kube.kube_access import KubeAccess


class KubeFetchNamespaces(KubeAccess):
    ATTRIBUTES_TO_FETCH = ['name', 'creation_timestamp', 'self_link', 'uid']

    def get(self, object_id):
        namespaces = self.api.list_namespace()

        self.update_resource_version(
            method='list_namespace',
            resource_version=namespaces.metadata.resource_version
        )

        return [self.get_namespace(i) for i in namespaces.items]

    @classmethod
    def get_namespace(cls, namespace: V1Namespace) -> dict:
        namespace_details = cls.class_to_dict(data_object=namespace.metadata, include=cls.ATTRIBUTES_TO_FETCH)
        namespace_details['id'] = namespace_details['uid']
        namespace_details['status'] = namespace.status.phase
        return namespace_details
