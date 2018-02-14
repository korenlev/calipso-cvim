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
                self.add_service_pod_link(service, pod_obj)
            else:
                self.log.error('unable to find pod {} in service {}'
                               .format(pod['id'], service['object_name']))

    def add_service_pod_link(self, service, pod):
        host = pod['host']
        source = service['_id']
        source_id = service['id']
        target = pod['_id']
        target_id = pod['id']
        link_type = 'vservice-pod'
        link_name = '{}-pod'.format(service['object_name'])
        state = 'up'  # TBD
        link_weight = 0  # TBD
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host)

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
                'host': pod['host'],
                'name': container['name']
            })
            if container_obj:
                self.add_pod_container_link(pod, container_obj)
            else:
                self.log.error('unable to find container {} from pod {}'
                               .format(container['name'], pod['object_name']))

    def add_pod_container_link(self, pod, container):
        host = pod['host']
        source = pod['_id']
        source_id = pod['id']
        target = container['_id']
        target_id = container['id']
        link_type = 'pod-container'
        link_name = '{}-container'.format(pod['object_name'])
        state = 'up'  # TBD
        link_weight = 0  # TBD
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host)

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
                self.add_container_network_link(container, network)

    def add_container_network_link(self, container, network):
        host = container['host']
        source = container['_id']
        source_id = container['id']
        target = network['_id']
        target_id = network['id']
        link_type = 'container-network'
        link_name = '{}-network'.format(container['name'])
        state = 'up'  # TBD
        link_weight = 0  # TBD
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host)
