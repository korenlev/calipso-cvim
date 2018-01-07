###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.fetchers.cli.cli_access import CliAccess
from utils.inventory_mgr import InventoryMgr


class CliFetchKubeContainerVnics(CliAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, container_id: str) -> list:
        container = self.inv.get_by_id(self.get_env(), container_id)
        if not container:
            self.log.error('Failed to find container with ID: {}', container_id)
            return []
        host = container['host']
        if not host:
            return []
        lines = self.run_fetch_lines("ip link show | grep -A1 veth", host)
        interface_lines = []
        ret = []
        for l in lines:
            interface_lines.append(l)
            if len(interface_lines) == 2:
                ret.append(self.process_interface(container, interface_lines))
                interface_lines = []
        return ret

    def process_interface(self, container, interface_lines) -> dict:
        interface = {
            'vnic_type': 'container_vnic',
            'host': container['host'],
            'lines': interface_lines
        }
        self.set_folder_parent(interface, 'vnic',
                               master_parent_type='container',
                               master_parent_id=container['id'],
                               parent_id='{}-vnics'.format(container['id']),
                               parent_type='vnics_folder',
                               parent_text='vNICs')
        regexps = [
            {'name': 'id', 're': '^[0-9]+:\s([^:]+):\s'},
            {'name': 'state', 're': ',(UP),', 'default': 'DOWN'},
            {'name': 'mac_address', 're': '.*\slink/ether\s(\S+)\s'},
            {'name': 'mtu', 're': '.*\smtu\s(\S+)\s'},
        ]
        self.get_object_data(interface, interface_lines, regexps)
        return interface
