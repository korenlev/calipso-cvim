###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re

from discover.fetchers.cli.cli_fetcher import CliFetcher
from discover.fetchers.cli.cli_fetch_interface_hardware_details_vpp \
    import CliFetchInterfaceHardwareDetailsVpp
from utils.inventory_mgr import InventoryMgr

NAME_RE = '^[a-zA-Z]*GigabitEthernet'
MAC_FIELD_RE = '^.*\sEthernet address\s(\S+)(\s.*)?$'


class CliFetchHostPnicsVpp(CliFetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.name_re = re.compile(NAME_RE)
        self.if_details_fetcher = CliFetchInterfaceHardwareDetailsVpp()

    def set_env(self, env):
        super().set_env(env)
        self.if_details_fetcher.set_env(env)

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        host_id = parent_id[:host_id.rindex("-")]
        vedges = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vedge",
            "host": host_id
        })
        ret = []
        for vedge in vedges:
            pnic_ports = vedge['ports']
            for pnic_name in pnic_ports:
                if not self.name_re.search(pnic_name):
                    continue
                pnic = pnic_ports[pnic_name]
                pnic['host'] = host_id
                pnic['id'] = host_id + "-pnic-" + pnic_name
                pnic['type'] = 'host_pnic'
                pnic['object_name'] = pnic_name
                pnic['Link detected'] = 'yes' if pnic['state'] == 'up' else 'no'
                ret.append(pnic)
        self.if_details_fetcher.add_hardware_interfaces_details(host_id, ret)
        self.add_pnic_ip_addresses(host_id, ret)
        return ret

    def add_pnic_ip_addresses(self, host_id, pnics: list):
        cmd = 'vppctl show int addr'
        lines = self.run_fetch_lines(cmd, host_id)
        for pnic in pnics:
            self.add_pnic_ip_address(pnic, lines)

    def add_pnic_ip_address(self, pnic, lines: list):
        for pos in range(0, len(lines)-2):
            line = lines[pos]
            pnic_name = pnic['name']
            if line.startswith('{} '.format(pnic_name)):
                self.log.debug('found IP address for pnic {}'.format(pnic_name))
                pnic['ip_address'] = lines[pos+1].strip()
