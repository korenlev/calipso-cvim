###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.events.kube.kube_event_delete_base import KubeEventDeleteBase
from discover.fetchers.kube.kube_fetch_pods import KubeFetchPods


class KubePodDelete(KubeEventDeleteBase):

    def handle(self, env, values):
        super().handle(env, values)
        self.delete_pod_references(object_id=self.object_id)
        return self.delete_handler(env=env,
                                   object_id=self.object_id,
                                   object_type="pod")

    def delete_pod_references(self, object_id=None):
        pod = self.inv.get_by_id(self.env, object_id)
        if not pod:
            self.log.error('unable to find pod with ID {}'.format(object_id))
            return
        self.delete_pod_reference_from_namespace(pod)

    def delete_pod_reference_from_vservice(self, pod):
        service = KubeFetchPods().get_pod_proxy_service(self.inv, pod)
        if not service:
            self.log.error('unable to find service for pod {} (ID: {}'
                           .format(pod['object_name'], pod['id']))
            return
        pods = list(filter(lambda p: p['id'] != pod['id'],
                           service.get('pods', [])))
        self.inv.inventory_collection.update({'_id': service['_id']},
                                             {'$set': {'pods': pods}})

    def delete_pod_reference_from_namespace(self, pod):
        namespace = KubeFetchPods.get_pod_namespace(self.inv, pod)
        if not namespace:
            self.log.error('unable to find namespace {} '
                           'for pod {} (ID: {})'
                           .format(pod['namespace'], pod['object_name'],
                                   pod['id']))
            return
        pods = list(filter(lambda p: p['id'] != pod['id'],
                           namespace.get('pods', [])))
        self.inv.inventory_collection.update({'_id': namespace['_id']},
                                             {'$set': {'pods': pods}})
