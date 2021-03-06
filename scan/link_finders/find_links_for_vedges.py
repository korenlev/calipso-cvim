###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional

from base.utils.configuration import Configuration
from base.utils.constants import KubeVedgeType
from base.utils.origins import Origin
from scan.link_finders.find_links import FindLinks


class FindLinksForVedges(FindLinks):
    def __init__(self):
        super().__init__()
        self.environment_type: Optional[str] = None
        self.mechanism_drivers: Optional[list] = None
        self.is_kubernetes_vpp: bool = False
        self.is_kubernetes_calico: bool = False
        self.is_kubernetes_flannel: bool = False

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.configuration = Configuration()
        self.environment_type = self.configuration.get_env_type()
        self.mechanism_drivers = self.configuration.environment.get('mechanism_drivers', [])
        self.is_kubernetes_vpp = (
            self.environment_type == self.ENV_TYPE_KUBERNETES
            and KubeVedgeType.VPP.value in self.mechanism_drivers
        )
        self.is_kubernetes_calico = (
            self.environment_type == self.ENV_TYPE_KUBERNETES
            and KubeVedgeType.CALICO.value in self.mechanism_drivers
        )
        self.is_kubernetes_flannel = (
            self.environment_type == self.ENV_TYPE_KUBERNETES
            and KubeVedgeType.FLANNEL.value in self.mechanism_drivers
        )

    def add_links(self):
        self.log.info("adding link types: vnic-vedge, vconnector-vedge, vedge-host_pnic")
        vedges = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vedge"
        })
        for vedge in vedges:
            if (
                    self.environment_type == self.ENV_TYPE_OPENSTACK
                    or self.is_kubernetes_vpp
                    or self.is_kubernetes_calico
            ):
                ports = vedge.get("ports", [])
                for p in ports:
                    self.add_links_for_vedge_port(vedge, p)

            if self.environment_type == self.ENV_TYPE_KUBERNETES:
                self.add_link_for_kubernetes_vedge(vedge)

    def add_links_for_vedge_port(self, vedge, port):
        vnic = self.find_matching_vnic(vedge, port)
        if vnic:
            link_name = vnic["name"] + "-" + vedge["name"]
            if "tag" in port:
                link_name += "-" + port["tag"]
            source_label = vnic["mac_address"]
            target_label = ''
            if vedge["vedge_type"] == "SRIOV":
                for vf in port["VFs"]:
                    if vf["mac_address"] == vnic["mac_address"]:
                        target_label = "port_{}-vlan_{}-vf_{}".format(port["id"], vf["vlan"], vf["vf"])
            else:
                target_label = port["id"]
            self.link_items(vnic, vedge, link_name=link_name,
                            extra_attributes={"source_label": source_label,
                                              "target_label": target_label,
                                              "vedge_type": vedge["type"]})
        elif vedge["vedge_type"] == "SRIOV":  # No vnic - no pnic
            return

        self.add_link_for_vconnector(vedge, port)
        self.add_link_for_pnic(vedge, port)

    def find_matching_vnic(self, vedge, port):
        # link_type: "vnic-vedge"
        vnic = None
        if vedge["vedge_type"] == "SRIOV":
            for vf in port["VFs"]:
                vf_mac = vf.get("mac_address")
                if not vf_mac or vf_mac == "00:00:00:00:00:00":
                    continue
                vnic = self.inv.find_one({
                    "environment": self.get_env(),
                    "type": "vnic",
                    "host": vedge["host"],
                    "mac_address": vf_mac
                })
                if vnic:
                    break
        else:
            vnic = self.inv.get_by_id(self.get_env(), '|'.join((vedge['host'], port["name"].replace("/", "."))))
            # try a match using port name to @dev name, as for rhel8 with OVS instance vnics attach to vedges directly
            if not vnic and vedge['vedge_type'] == 'OVS':
                vnic = self.inv.get_by_field(environment=self.get_env(), item_type='vnic',  field_name='target.@dev',
                                             field_value=port["name"], get_single=True)
        return vnic

    def add_link_for_vconnector(self, vedge, port):
        # link_type: "vconnector-vedge"
        if self.configuration.has_network_plugin('VPP'):
            vconnector_interface_name = port['name']
        else:
            if not port["name"].startswith("qv"):
                return
            base_id = port["name"][3:]
            vconnector_interface_name = "qvb{}".format(base_id)

        vconnector = self.inv.find_one({
            "environment": self.get_env(),
            "type": "vconnector",
            "host": vedge['host'],
            'interfaces_names': vconnector_interface_name
        })
        if not vconnector:
            return

        link_name = "-".join(("port", port["id"]))
        if "tag" in port:
            link_name = "-".join((link_name, port["tag"]))
        source_label = vconnector_interface_name
        target_label = port["name"]
        mac_address = "Unknown"
        attributes = {
            'mac_address': mac_address,
            'source_label': source_label,
            'target_label': target_label,
            'vedge_type': vedge['vedge_type']
        }

        for interface in vconnector['interfaces']:
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

    def add_link_for_pnic(self, vedge, port):
        # link_type: "vedge-host_pnic"
        pname = port["name"]
        if "pnic" in vedge and pname != vedge["pnic"]:
            return

        pnic_query = {
            "environment": self.get_env(),
            "type": "host_pnic",
            "host": vedge["host"]
        }
        if vedge["vedge_type"] == "SRIOV":
            pnic_query["local_name"] = pname
        else:
            pnic_query["name"] = pname

        pnic = self.inv.find_one(pnic_query)
        if not pnic:
            return

        attributes = {}
        if 'network' in pnic:
            attributes['network'] = pnic['network']

        link_name = "Port-" + port["id"]
        state = "up" if pnic["Link detected"] == "yes" else "down"
        self.link_items(vedge, pnic, link_name=link_name, state=state,
                        extra_attributes=attributes)

    def add_link_for_kubernetes_vedge(self, vedge):
        otep = {}
        link_name = ''
        # link_type: 'vedge-otep' for flannel case
        if self.is_kubernetes_flannel:
            host_ip = vedge.get('pod_status', {}).get('host_ip', '')
            otep = self.inv.find_one({
                'environment': self.get_env(),
                'type': 'otep',
                'ip_address': host_ip
            })
            link_name = '{}-{}'.format(vedge['object_name'], otep.get('overlay_mac_address', 'Unknown'))
        # link_type: 'vedge-otep' for calico case
        elif self.is_kubernetes_calico:
            ip_address = vedge.get('ip_address')
            otep = self.inv.find_one({
                'environment': self.get_env(),
                'type': 'otep',
                'ip_address': ip_address
            })
            link_name = '{}-{}'.format(vedge['object_name'], otep.get('tunnel_address', 'Unknown'))

        if not otep:
            return
        self.link_items(vedge, otep, link_name=link_name)
