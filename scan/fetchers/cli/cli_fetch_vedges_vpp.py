###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.constants import HostType
from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.util.validators import HostTypeValidator


class CliFetchVedgesVpp(CliFetcher, HostTypeValidator):
    ACCEPTED_HOST_TYPES = [HostType.NETWORK.value, HostType.COMPUTE.value]

    def get(self, parent_id) -> list:
        host_id = parent_id.replace('-vedges', '')
        if not self.validate_host(host_id):
            return []

        vedge = {
            'host': host_id,
            'id': host_id + '-VPP',
            'name': 'VPP-' + host_id,
            'agent_type': 'VPP',
            'vedge_type': 'VPP'
        }
        ver = self.run_fetch_lines('vppctl show ver', ssh_to_host=host_id)
        if ver:
            ver = ver[0]
            vedge['binary'] = ver[:ver.index(' ', ver.index(' ') + 1)]

        interfaces = self.run_fetch_lines('vppctl show int', ssh_to_host=host_id)
        vedge['ports'] = self.fetch_ports(interfaces)
        self.set_folder_parent(vedge, 'vedge', parent_text='vEdges',
                               master_parent_type='host',
                               master_parent_id=host_id)
        return [vedge]

    @staticmethod
    def fetch_ports(interfaces):
        ports = []
        for i in interfaces:
            if not i or i.startswith(' '):
                continue
            parts = i.split()
            port = {
                'id': parts[1],
                'state': parts[2],
                'name': parts[0]
            }
            ports.append(port)
        return ports
