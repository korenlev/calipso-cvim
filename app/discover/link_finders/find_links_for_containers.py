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


class FindLinksForContainers(FindLinks):
    def __init__(self):
        super().__init__()

    def add_links(self):
        containers = self.inv.find_items({
            'environment': self.get_env(),
            'type': 'container'
        })
        self.log.info('adding links of type: container-vnic')
        for container in containers:
            self.find_matching_vnic(container)
            self.find_matching_vedge(container)

    def find_matching_vnic(self, container):
        if 'vnic_index' not in container or not container['vnic_index']:
            return
        vnic = self.inv.find_one({
            'environment': self.get_env(),
            'type': 'vnic',
            'host': container['host'],
            'index': container['vnic_index']
        })
        if vnic:
            self.add_container_vnic_link(container, vnic)

    def add_container_vnic_link(self, container, vnic):
        host = vnic['host']
        source = container['_id']
        source_id = container['id']
        target = vnic['_id']
        target_id = vnic['id']
        link_type = 'container-vnic'
        link_name = vnic['mac_address']
        state = 'up'  # TBD
        link_weight = 0  # TBD
        attributes = dict(container_vnic=vnic['object_name'])
        if 'network' in container:
            vnic['network'] = container['network']
            self.inv.set(vnic)
            attributes['network'] = container['network']
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host,
                         extra_attributes=attributes)

    def find_matching_vedge(self, container):
        if container['name'] != 'kube-proxy':
            return
        vedge = self.inv.find_one({
            'environment': self.get_env(),
            'type': 'vedge',
            'host': container['host']
        })
        if not vedge:
            return
        pass

    def add_container_vedge_link(self, container, vedge):
        host = container['host']
        source = container['_id']
        source_id = container['id']
        target = vedge['_id']
        target_id = vedge['id']
        link_type = 'container-vedge'
        link_name = vedge['mac_address']
        state = 'up'  # TBD
        link_weight = 0  # TBD
        attributes = dict()
        if 'network' in container:
            attributes['network'] = container['network']
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host,
                         extra_attributes=attributes)
