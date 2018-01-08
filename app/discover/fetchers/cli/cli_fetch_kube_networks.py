###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json
from json import JSONDecodeError

from discover.fetchers.cli.cli_access import CliAccess
from utils.inventory_mgr import InventoryMgr


class CliFetchKubeNetworks(CliAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, host_id: str) -> list:
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('Failed to find host with ID: {}', host_id)
            return []
        lines = self.run_fetch_lines('docker network ls', host_id)
        ret = []
        headers = [
            'NETWORK ID',
            'NAME',
            'DRIVER',
            'SCOPE'
        ]
        networks = self.parse_cmd_result_with_whitespace(lines, headers, True)
        for network in networks:
            ret.append(self.get_network(host, network))
        return ret

    def get_network(self, host, network_data) -> dict:
        network = {
            'host': host['host'],
            'id': network_data['NETWORK ID'],
            'name': '{}-{}'.format(host['host'], network_data['NAME']),
            'driver': network_data['DRIVER'],
            'scope': network_data['SCOPE']
        }
        self.set_folder_parent(network, 'network',
                               master_parent_type='host',
                               master_parent_id=host['id'])
        self.get_network_data(network)
        return network

    def get_network_data(self, network):
        cmd = 'docker network inspect {}'.format(network['id'])
        output = self.run(cmd, network['host'])
        try:
            network_data = json.loads(output)
        except JSONDecodeError as e:
            self.log.error('error reading network data for {}: {}'
                           .format(network['id'], str(e)))
            return
        network_data = network_data[0]
        network_data.pop('Id')
        network_data.pop('Name')
        network.update(network_data)
