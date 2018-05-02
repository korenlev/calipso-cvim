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
from utils.configuration import Configuration


class FindLinksForVedges(FindLinks):
    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.environment_type = self.configuration.get_env_type()
        self.mechanism_drivers = \
            self.configuration.environment.get('mechanism_drivers', [])
        self.is_kubernetes_vpp = \
            self.environment_type == self.ENV_TYPE_KUBERNETES \
            and 'VPP' in self.mechanism_drivers

    def add_links(self):
        self.log.info("adding link types: " +
                      "vnic-vedge, vconnector-vedge, vedge-host_pnic")
        vedges = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vedge"
        })
        for vedge in vedges:
            if self.environment_type == self.ENV_TYPE_OPENSTACK \
                    or self.is_kubernetes_vpp:
                ports = vedge.get("ports", {})
                for p in ports.values():
                    self.add_link_for_vedge(vedge, p)
            elif self.environment_type == self.ENV_TYPE_KUBERNETES:
                self.add_link_for_kubernetes_vedge(vedge)

    def add_link_for_vedge(self, vedge, port):
        # link_type: "vnic-vedge"
        vnic = None if self.environment_type == self.ENV_TYPE_KUBERNETES \
            else self.inv.get_by_id(self.get_env(),
                                    vedge['host'] + '-' + port["name"])
        if not vnic:
            self.find_matching_vconnector(vedge, port)
            self.find_matching_pnic(vedge, port)
            return
        link_name = vnic["name"] + "-" + vedge["name"]
        if "tag" in port:
            link_name += "-" + port["tag"]
        source_label = vnic["mac_address"]
        target_label = port["id"]
        self.link_items(vnic, vedge, link_name=link_name,
                        extra_attributes={"source_label": source_label,
                                          "target_label": target_label})

    def find_matching_vconnector(self, vedge, port):
        # link_type: "vconnector-vedge"
        if self.configuration.has_network_plugin('VPP'):
            vconnector_interface_name = port['name']
        else:
            if not port["name"].startswith("qv"):
                return
            base_id = port["name"][3:]
            vconnector_interface_name = "qvb" + base_id
        vconnector = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vconnector",
            "host": vedge['host'],
            'interfaces_names': vconnector_interface_name},
            get_single=True)
        if not vconnector:
            return
        link_name = "port-" + port["id"]
        if "tag" in port:
            link_name += "-" + port["tag"]
        source_label = vconnector_interface_name
        target_label = port["name"]
        mac_address = "Unknown"
        attributes = {'mac_address': mac_address, 'source_label': source_label,
                      'target_label': target_label}
        for interface in vconnector['interfaces'].values():
            if vconnector_interface_name != interface['name']:
                continue
            if 'mac_address' not in interface:
                continue
            mac_address = interface['mac_address']
            attributes['mac_address'] = mac_address
            break
        if 'network' in vconnector:
            attributes['network'] = vconnector['network']
        self.link_items(vconnector, vedge, link_name=link_name,
                        extra_attributes=attributes)

    def find_matching_pnic(self, vedge, port):
        # link_type: "vedge-host_pnic"
        pname = port["name"]
        if "pnic" in vedge:
            if pname != vedge["pnic"]:
                return
        pnic = self.inv.find_items({
            "environment": self.get_env(),
            "type": "host_pnic",
            "host": vedge["host"],
            "name": pname
        }, get_single=True)
        if not pnic:
            return
        link_name = "Port-" + port["id"]
        state = "up" if pnic["Link detected"] == "yes" else "down"
        self.link_items(vedge, pnic, link_name=link_name, state=state)

    def add_link_for_kubernetes_vedge(self, vedge):
        # link_type: 'vedge-otep'
        host_ip = vedge.get('status', {}).get('host_ip', '')
        otep = self.inv.find_one({
            'environment': self.get_env(),
            'type': 'otep',
            'ip_address': host_ip
        })
        if not otep:
            return
        link_name = '{}-{}'.format(vedge['object_name'],
                                   otep['overlay_mac_address'])
        self.link_items(vedge, otep, link_name=link_name)
