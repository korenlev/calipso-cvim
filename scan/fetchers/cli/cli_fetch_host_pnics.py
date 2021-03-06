###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re

from base.utils.constants import HostType
from scan.fetchers.cli.cli_fetch_interface_details import CliFetchInterfaceDetails
from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.util.validators import HostTypeValidator


class CliFetchHostPnics(CliFetcher, HostTypeValidator):

    SUPPORTED_PORTS_REGEX = re.compile("Supported ports:\s*\[(?P<ports>.*)\]")
    SUPPORTED_LINK_MODES_REGEX = re.compile("Supported link modes:\s*(?P<link_modes>.*)")
    ACCEPTED_HOST_TYPES = [HostType.CONTROLLER.value, HostType.NETWORK.value, HostType.COMPUTE.value]

    def __init__(self):
        super().__init__()
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

    def get_by_host_id(self, host_id):
        ls_cmd = 'ls -l /sys/class/net | grep ^l'
        interface_lines = self.run_fetch_lines(cmd=ls_cmd, ssh_to_host=host_id)
        interfaces = []
        for line in interface_lines:
            if "/virtual/" in line and "ovs-system" not in line:
                continue

            interface_name = line[line.rindex('/') + 1:]
            interface_name = interface_name.strip()

            ethtool_cmd = 'ethtool {}'.format(interface_name)
            ethtool_lines = self.run_fetch_lines(cmd=ethtool_cmd, ssh_to_host=host_id)

            ports_match, link_modes_match = None, None
            is_physical = True
            for ethtool_line in ethtool_lines:
                if ports_match and link_modes_match:
                    ports = ports_match.groupdict().get('ports', '').strip()
                    link_modes = link_modes_match.groupdict().get('link_modes', '').strip()
                    if not ports and not link_modes:
                        is_physical = False
                        break

                if not ports_match:
                    ports_match = self.SUPPORTED_PORTS_REGEX.match(ethtool_line)
                    if ports_match:
                        continue

                if not link_modes_match:
                    link_modes_match = self.SUPPORTED_LINK_MODES_REGEX.match(ethtool_line)
                    if link_modes_match:
                        continue

            if not is_physical:
                continue

            # run 'ip address show' with specific interface name,
            # since running it with no name yields a list without inactive pNICs
            ip_cmd = "ip address show {}".format(interface_name)
            ip_lines = self.run_fetch_lines(cmd=ip_cmd, ssh_to_host=host_id)
            interface = self.details_fetcher.get_interface_details(host_id, interface_name, ip_lines, ethtool_lines)
            if interface:
                interfaces.append(interface)
        return interfaces

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        if not self.get_and_validate_host(host_id):
            return []

        return self.get_by_host_id(host_id)
