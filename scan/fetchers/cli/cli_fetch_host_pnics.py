###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re

from base.utils.inventory_mgr import InventoryMgr
from scan.fetchers.cli.cli_fetch_interface_details \
    import CliFetchInterfaceDetails
from scan.fetchers.cli.cli_fetcher import CliFetcher


class CliFetchHostPnics(CliFetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.ethtool_attr = re.compile('^\s+([^:]+):\s(.*)$')
        self.regexps = [
            {'name': 'mac_address', 're': '^.*\slink/ether\s(\S+)\s',
             'description': 'MAC address'},
            {'name': 'IP Address', 're': '^\s*inet ([0-9.]+)/',
             'description': 'IP Address v4'},
            {'name': 'IPv6 Address', 're': '^\s*inet6 (\S+) .* global ',
             'description': 'IPv6 Address'}
        ]
        self.details_fetcher = CliFetchInterfaceDetails()

    def set_env(self, env):
        super().set_env(env)
        self.details_fetcher.set_env(env)

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error("CliFetchHostPnics: host not found: " + host_id)
            return []
        if "host_type" not in host:
            self.log.error("host does not have host_type: " + host_id +
                           ", host: " + str(host))
            return []
        host_types = host["host_type"]
        accepted_host_types = ['Network', 'Compute']
        if not [t for t in accepted_host_types if t in host_types]:
            return []

        cmd = 'ls -l /sys/class/net | grep ^l'
        interface_lines = self.run_fetch_lines(cmd, host_id)
        interfaces = []
        for line in interface_lines:
            if "/virtual/" in line and "ovs-system" not in line:
                continue

            interface_name = line[line.rindex('/')+1:]
            interface_name = interface_name.strip()
            # run 'ip address show' with specific interface name,
            # since running it with no name yields a list without inactive pNICs
            interface = self.find_interface_details(host_id, interface_name)
            if interface:
                interfaces.append(interface)
        return interfaces

    def find_interface_details(self, host_id, interface_name):
        cmd = "ip address show {}".format(interface_name)
        lines = self.run_fetch_lines(cmd, host_id)
        return self.details_fetcher.get_interface_details(host_id,
                                                          interface_name,
                                                          lines)
