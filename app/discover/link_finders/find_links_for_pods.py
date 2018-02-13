###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.link_finders.find_links import FindLinks


class FindLinksForPods(FindLinks):
    def __init__(self):
        super().__init__()

    def add_links(self):
        self.find_service_pod_links()
        self.find_pod_container_links()
        self.find_container_network_links()

    def find_service_pod_links(self):
        services = self.inv.find_items({
            'environment': self.get_env(),
            'type': 'vservice'
        })
        self.log.info('adding links of type: vservice-pod')
        for service in services:
            self.find_service_pods(service)

    def find_service_pods(self, service):
        if 'pods' not in service or not service['pods']:
            return
        for pod in service['pods']:
            pod_obj = self.inv.get_by_id(self.get_env(), pod['id'])
            if pod:
                # link_type: 'vservice-pod'
                self.add_items_link(service, pod_obj)
            else:
                self.log.error('unable to find pod {} in service {}'
                               .format(pod['id'], service['object_name']))

    def add_items_link(self, source, target):
        link_name = '{}-{}'.format(source['object_name'], target['type'])

    def find_pod_container_links(self):
        pods = self.inv.find_items({
            'environment': self.get_env(),
            'type': 'pod'
        })
        self.log.info('adding links of type: pod-container')
        for pod in pods:
            self.find_pod_containers(pod)

    def find_pod_containers(self, pod):
        if 'containers' not in pod or not pod['containers']:
            return
        for container in pod['containers']:
            container_obj = self.inv.find_one({
                'environment': self.get_env(),
                'type': 'container',
                'name': container['name']
            })
            if container_obj:
                # link_type: 'pod-container'
                self.add_items_link(pod, container_obj)
            else:
                self.log.error('unable to find container {} from pod {}'
                               .format(container['name'], pod['object_name']))

    def find_container_network_links(self):
        containers = self.inv.find_items({
            'environment': self.get_env(),
            'type': 'container'
        })
        self.log.info('adding links of type: container-network')
        for container in containers:
            if container.get('network', ''):
                network = self.inv.get_by_id(self.get_env(),
                                             container['network'])
                if not network:
                    self.log.error('unable to find network {} in container {}'
                                   .format(container['network'],
                                           container['name']))
                # link_type: 'container-network'
                self.add_items_link(container, network)
