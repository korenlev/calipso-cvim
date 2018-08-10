###############################################################################
# Copyright (c) 2017-2018 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.fetchers.cli.cli_fetch_vconnectors import CliFetchVconnectors


class CliFetchVconnectorsVpp(CliFetchVconnectors):
    def __init__(self):
        super().__init__()
        self.vconnectors = None
        self.interfaces = {}
        self.interfaces_names = []

    def get_vconnectors(self, host):
        self.vconnectors = {}
        lines = self.run_fetch_lines("vppctl show mode", host['id'])
        is_kubernetes = self.ENV_TYPE_KUBERNETES == \
            self.configuration.environment.get('environment_type')
        self.interfaces = {}
        self.interfaces_names = []
        for l in lines:
            is_l2_bridge = l.startswith('l2 bridge')
            if not is_kubernetes and not is_l2_bridge:
                continue
            line_parts = l.strip().split(' ')
            name = line_parts[2 if is_l2_bridge else 1]
            bd_id = line_parts[4] if is_l2_bridge else ''
            self.add_vconnector(host=host, bd_id=bd_id)
            interface = self.get_interface_details(host, name)
            if interface:
                self.interfaces[name] = interface
                self.interfaces_names.append(name)
        return list(self.vconnectors.values())

    def add_vconnector(self, host: dict=None, bd_id: str=''):
        if not bd_id or bd_id in self.vconnectors:
            return
        vconnector = dict(
            host=host['id'],
            id='{}-vconnector-{}'.format(host['id'], bd_id),
            bd_id=bd_id,
            name='bridge-domain-{}'.format(bd_id),
            object_name='{}-VPP-bridge-domain-{}'.format(host['id'], bd_id),
            interfaces=self.interfaces,
            interfaces_names=self.interfaces_names
        )
        self.vconnectors[bd_id] = vconnector
        vconnector['interfaces'] = self.interfaces
        vconnector['interfaces_names'] = self.interfaces_names
        return vconnector

    def get_interface_details(self, host, name):
        # find vconnector interfaces
        cmd = "vppctl show hardware-int " + name
        interface_lines = self.run_fetch_lines(cmd, host['id'])
        # remove header line
        interface_lines.pop(0)
        interface = None
        for l in interface_lines:
            if not l.strip():
                continue  # ignore empty lines
            if not l.startswith(' '):
                details = l.split()
                interface = {
                    "name": details[0],
                    "hardware": details[3],
                    "state": details[2],
                    "id": details[1],
                }
            elif l.startswith('  Ethernet address '):
                interface['mac_address'] = l[l.rindex(' ') + 1:]
        return interface
