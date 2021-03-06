###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import copy
import functools

from base.utils.origins import Origin
from scan.processors.processor import Processor


class ProcessVedgeType(Processor):
    PREREQUISITES = []

    def __init__(self):
        super().__init__()
        self.environment_type = None

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.environment_type = self.configuration.get_env_type()

    def find_matching_vnics(self, vedge, port):
        vnics = []
        if self.environment_type != self.ENV_TYPE_KUBERNETES:
            if vedge["vedge_type"] == "SRIOV":
                for vf in port["VFs"]:
                    vf_mac = vf.get("mac_address")
                    if not vf_mac or vf_mac == "00:00:00:00:00:00":
                        continue

                    vnic = self.inv.find_one({
                        "environment": self.env,
                        "type": "vnic",
                        "host": vedge["host"],
                        "mac_address": vf_mac
                    })
                    if vnic:
                        # In fact it's a VF+port combination
                        vedge_port = copy.deepcopy(port)
                        vedge_port.pop('VFs', None)
                        vedge_port.update(vf)
                        vnic['vedge_port'] = vedge_port
                        vnic['vedge_id'] = vedge['id']
                        vnics.append(vnic)
            else:
                vnic = self.inv.get_by_id(self.env, '|'.join((vedge['host'], port["name"].replace("/", "."))))
                # try a match using port name to @dev name, as for rhel8 with OVS instance vnics attach to vedges directly
                if not vnic and vedge['vedge_type'] == 'OVS':
                    vnic = self.inv.get_by_field(environment=self.get_env(), item_type='vnic', field_name='target.@dev',
                                                 field_value=port["name"], get_single=True)
                if vnic:
                    vnic['vedge_port'] = port
                    vnic['vedge_id'] = vedge['id']
                    vnics.append(vnic)

        return vnics

    def find_matching_vconnector(self, vedge, port):
        if self.configuration.has_network_plugin('VPP'):
            vconnector_interface_name = port['name']
        else:
            if not port["name"].startswith("qv"):
                return
            base_id = port["name"][3:]
            vconnector_interface_name = "qvb{}".format(base_id)

        return self.inv.find_one({
            "environment": self.env,
            "type": "vconnector",
            "host": vedge['host'],
            'interfaces_names': vconnector_interface_name
        })

    def update_vnic_and_related_objects(self, vnic, vedge_type):
        if "vedge_type" in vnic:
            return

        vnic["vedge_type"] = vedge_type
        self.inv.set(vnic)

        instance_id = vnic.get("instance_id")
        vservice_id = vnic.get("vservice_id")
        if instance_id:
            instance = self.inv.get_by_id(self.env, instance_id)
            if instance and "vedge_type" not in instance:
                instance["vedge_type"] = vedge_type
                self.inv.set(instance)
        elif vservice_id:
            vservice = self.inv.get_by_id(self.env, vservice_id)
            if vservice and "vedge_type" not in vservice:
                vservice["vedge_type"] = vedge_type
                self.inv.set(vservice)

    def find_vnic_for_vconnector_interface(self, vconnector, interface_name):
        ovs_or_flannel = (
            self.configuration.has_network_plugin('OVS')
            or self.configuration.has_network_plugin('Flannel')
        )
        if ovs_or_flannel:
            # interface ID for OVS
            search_func = functools.partial(self.inv.get_by_field,
                                            self.env, 'vnic',
                                            field_value=interface_name, get_single=True)
            vnic = search_func(field_name='name')
            if not vnic:
                vnic = search_func(field_name='target.@dev')
        else:
            # interface ID for VPP - match interface MAC address to vNIC MAC
            interface = next(i for i in vconnector['interfaces'] if interface_name == i['name'])
            if not interface or 'mac_address' not in interface:
                return None
            vconnector_if_mac = interface['mac_address']
            vnic = self.inv.find_one({
                'environment': self.env,
                'type': 'vnic',
                'host': vconnector['host'],
                'mac_address': vconnector_if_mac
            })
        return vnic

    def update_matching_objects(self, vedge, port):
        vedge_type = vedge["vedge_type"]
        vnics = self.find_matching_vnics(vedge, port)
        if vnics:
            for vnic in vnics:
                self.update_vnic_and_related_objects(vnic, vedge_type)
        else:
            vconnector = self.find_matching_vconnector(vedge, port)
            if vconnector and "vedge_type" not in vconnector:
                vconnector.update({
                    "vedge_type": vedge_type,
                    "vedge_id": vedge["id"],
                    "vedge_port": port
                })
                self.inv.set(vconnector)
                for interface in vconnector["interfaces_names"]:
                    vnic = self.find_vnic_for_vconnector_interface(vconnector, interface)
                    # TODO: assumption: vnic M<->1 vconnector?
                    if vnic:
                        vnic["vconnector_id"] = vconnector["id"]
                        self.update_vnic_and_related_objects(vnic, vedge_type)

    def run(self):
        super().run()
        vedges = self.find_by_type("vedge")
        for vedge in vedges:
            for port in vedge.get("ports", []):
                self.update_matching_objects(vedge, port)

        vnics = self.find_by_type("vnic")
        for vnic in vnics:
            if not vnic.get('vedge_type'):
                vnic['vedge_type'] = 'Unknown'
                self.inv.set(vnic)
