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
from typing import List

from base.utils.constants import KubeVedgeType
from scan.fetchers.cli.cli_fetcher import CliFetcher

# Fetch K8S vEdge details from output of 'ip route show' ('ip r show')


class CliFetchKubeVedgeDetails(CliFetcher):
    IP_ROUTE_CMD = "ip route show"

    def update_vedge_details(self, vedge: dict, host_id: str) -> None:
        # only for calico vedges yet
        if vedge.get('vedge_type', '') != KubeVedgeType.CALICO.value:
            return

        routing_table = self.run_fetch_lines(cmd=self.IP_ROUTE_CMD, ssh_to_host=host_id)
        ip_address = vedge.get('ip_address', '')
        # currently ip_address is in the /bit_mask format, later it might not
        if '/' in ip_address:
            ip_address = ip_address.split('/')[0]
        # outbound_route is the line in the routing tables sourced from that vedge ip_address
        # we need the routing_table and the device from which vedge sends out the traffic

        device = self.find_device(routing_table=routing_table, ip_address=ip_address)
        vedge.update({
            'routing_table': routing_table,
            'vconnector': '{}-{}'.format(host_id, device)
        })

    @staticmethod
    def find_device(routing_table: List[str], ip_address: str) -> str:
        src_regex = re.compile(".*dev\s+(\w+)\s+.*src\s+{}".format(re.escape(ip_address)))
        for line in routing_table:
            device_match = src_regex.match(line)
            if device_match:
                return device_match.group(1).strip()
        return ""
