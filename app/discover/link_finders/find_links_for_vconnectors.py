###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.configuration import Configuration
from discover.link_finders.find_links import FindLinks


class FindLinksForVconnectors(FindLinks):
    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.environment_type = self.configuration.get_env_type()

    def add_links(self):
        if self.environment_type == self.ENV_TYPE_OPENSTACK:
            self.log.info('adding links of type: vnic-vconnector, '
                          'vconnector-host_pnic')
        if self.environment_type == self.ENV_TYPE_KUBERNETES:
            self.log.info('adding links of type: vconnector-vedge')
        vconnectors = self.inv.find_items({
            'environment': self.get_env(),
            'type': 'vconnector'
        })
        for vconnector in vconnectors:
            for interface in vconnector["interfaces_names"]:
                self.add_vnic_vconnector_link(vconnector, interface)
                if self.environment_type == self.ENV_TYPE_OPENSTACK:
                    self.add_vconnector_pnic_link(vconnector, interface)
            if self.environment_type == self.ENV_TYPE_KUBERNETES:
                self.add_vconnector_vedge_link(vconnector)

    def add_vnic_vconnector_link(self, vconnector, interface_name):
        mechanism_drivers = self.configuration.environment['mechanism_drivers']
        ovs_or_flannel = mechanism_drivers and ('OVS' in mechanism_drivers or
                                                'Flannel' in mechanism_drivers)
        if ovs_or_flannel:
            # interface ID for OVS
            vnic_id = "{}-{}".format(vconnector["host"], interface_name)
            vnic = self.inv.get_by_id(self.get_env(), vnic_id)
        else:
            # interface ID for VPP - match interface MAC address to vNIC MAC
            interface = vconnector['interfaces'][interface_name]
            if not interface or 'mac_address' not in interface:
                return
            vnic_mac = interface['mac_address']
            vnic = self.inv.get_by_field(self.get_env(), 'vnic',
                                         'mac_address', vnic_mac,
                                         get_single=True)
        if not vnic:
            return
        if 'network' in vnic:
            vconnector['network'] = vnic['network']
            self.inv.set(vconnector)
        host = vnic["host"]
        source = vnic["_id"]
        source_id = vnic["id"]
        target = vconnector["_id"]
        target_id = vconnector["id"]
        link_type = "vnic-vconnector"
        link_name = vnic["mac_address"]
        state = "up"  # TBD
        link_weight = 0  # TBD
        attributes = {}
        if 'network' in vnic:
            attributes = {'network': vnic['network']}
            vconnector['network'] = vnic['network']
            self.inv.set(vconnector)
        self.create_link(self.get_env(),
                         source, source_id, target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host,
                         extra_attributes=attributes)

    def add_vconnector_pnic_link(self, vconnector, interface):
        ifname = interface['name'] if isinstance(interface, dict) else interface
        if "." in ifname:
            ifname = ifname[:ifname.index(".")]
        host = vconnector["host"]
        pnic = self.inv.find_items({
            "environment": self.get_env(),
            "type": "host_pnic",
            "host": vconnector["host"],
            "name": ifname
        }, get_single=True)
        if not pnic:
            return
        source = vconnector["_id"]
        source_id = vconnector["id"]
        target = pnic["_id"]
        target_id = pnic["id"]
        link_type = "vconnector-host_pnic"
        link_name = pnic["name"]
        state = "up"  # TBD
        link_weight = 0  # TBD
        self.create_link(self.get_env(),
                         source, source_id,
                         target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host)

    def add_vconnector_vedge_link(self, vconnector):
        host = vconnector['host']
        prefix = '{}-cni'.format(host)
        if not vconnector['id'].startswith(prefix):
            return
        vedge = self.inv.find_one({
            'environment': self.get_env(),
            'type': 'vedge',
            'host': host
        })
        if not vedge:
            return
        source = vconnector['_id']
        source_id = vconnector['id']
        target = vedge['_id']
        target_id = vedge['id']
        link_type = 'vconnector-vedge'
        link_name = vedge['name']
        state = 'up'  # TBD
        link_weight = 0  # TBD
        self.create_link(self.get_env(),
                         source, source_id,
                         target, target_id,
                         link_type, link_name, state, link_weight,
                         host=host)
