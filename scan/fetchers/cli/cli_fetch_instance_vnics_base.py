###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import abc
import re

import xmltodict

from base.utils.constants import HostType
from base.utils.origins import Origin

from scan.fetchers.cli.cli_fetch_vservice_vnics import CliFetchVserviceVnics
from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.util.validators import HostTypeValidator


class CliFetchInstanceVnicsBase(CliFetcher, HostTypeValidator):
    ACCEPTED_HOST_TYPES = [HostType.COMPUTE.value]
    PATH_UUID_REGEX = re.compile(".*([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-4[A-Fa-f0-9]{3}-[89aAbB][A-Fa-f0-9]{3}-[A-Fa-f0-9]{12})")

    def __init__(self):
        super().__init__()
        self.ports = None

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.ports = {}

    def get(self, parent_id):
        instance_uuid = parent_id[:parent_id.rindex('-')]
        instance = self.inv.get_by_id(self.get_env(), instance_uuid)
        if not instance:
            return []

        if not self.get_and_validate_host(instance["host"]):
            return []

        if instance["host"] not in self.ports:
            self.ports[instance["host"]] = self.inv.find({"environment": self.get_env(),
                                                          "type": "port",
                                                          "binding:host_id": instance["host"]})

        lines = self.run_fetch_lines("virsh list --all", ssh_to_host=instance["host"])
        del lines[:2]  # remove header
        virsh_names = [l.split()[1] for l in lines if l > ""]  # need to use names instead of ids
        results = []
        # Note: there are 2 ids here of instances with local names, which are
        # not connected to the data we have thus far for the instance
        # therefore, we will decide whether the instance is the correct one
        # based on comparison of the uuid in the dumpxml output
        for name in virsh_names:
            results.extend(self.get_vnics_data(name, instance))
        return results

    def update_instance_with_domain_data(self, instance, domain):
        disks = domain["devices"].get("disk")
        if disks:
            instance["disks"] = [disks] if isinstance(disks, dict) else disks
        vcpu = domain.get("vcpu")
        if vcpu:
            instance["vcpu"] = vcpu
        self.inv.set(instance)

    def get_vnics_data(self, name, instance):
        xml_string = self.run("virsh dumpxml {}".format(name), ssh_to_host=instance["host"])
        if not xml_string.strip():
            return []

        response = xmltodict.parse(xml_string)
        domain = response["domain"]
        if instance["uuid"] != domain["uuid"]:
            # this is the wrong instance - skip it
            return []

        # Update instance with matching domain data
        self.update_instance_with_domain_data(instance, domain)

        try:
            vnics = domain["devices"]["interface"]
        except KeyError:
            return []

        if isinstance(vnics, dict):
            vnics = [vnics]
        for v in vnics:
            self.set_vnic_properties(v, instance)

        return vnics

    @abc.abstractmethod
    def set_vnic_names(self, v, instance):
        return

    def set_vnic_properties(self, v, instance):
        v.update({
            "vnic_type": "instance_vnic",
            "host": instance["host"],
            "instance_id": instance["id"],
            "instance_db_id": instance["_id"],
            "mac_address": v["mac"]["@address"],
            "mtu": v.get("mtu", {}).get("@size")
        })
        self.set_vnic_names(v, instance)

        instance["mac_address"] = v["mac_address"]
        uuid_match = re.match(self.PATH_UUID_REGEX, v.get("source", {}).get("@path", ""))
        if uuid_match:
            v["uuid"] = uuid_match.group(1)

        port = next((p for p in self.ports.get(instance["host"], []) if p.get("mac_address") == v["mac_address"]), None)
        if port:
            v["port"] = port["id"]

        network = next((n for n in instance.get("network_info", []) if n["address"] == v["mac_address"]), None)
        if network:
            v["addresses"] = []
            for subnet in network.get("network", {}).get("subnets", []):
                if subnet["version"] == 4:
                    cidr = subnet["cidr"]
                    netmask = CliFetchVserviceVnics.convert_netmask(cidr.split("/")[-1])
                elif subnet["version"] == 6:
                    cidr = subnet["cidr"]
                    netmask = cidr
                else:
                    cidr = "undetermined"
                    netmask = "undetermined"
                v["addresses"].append({
                    "cidr": cidr,
                    "version": subnet["version"],
                    "netmask": netmask,
                    "IP Address": subnet["ips"][0]["address"],
                    "dhcp_server": subnet["meta"].get("dhcp_server"),
                    "gateway": subnet["gateway"]["address"],
                    "routes": subnet["routes"],
                    "dns": subnet["dns"]
                })

        self.inv.set(instance)
