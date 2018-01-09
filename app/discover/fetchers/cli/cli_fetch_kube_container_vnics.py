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
        host = self.inv.get_by_id(self.get_env(), container['host'])
        if not host:
            return []
        index = self.get_interface_index(container)
        if index is None:
            return []
        interfaces = [i for i in host['interfaces'].values()
                      if i['index'] == str(index)]
        if not container:
            self.log.error('Failed to find interface index {} '
                           'for container with ID: {}', index, container_id)
            return []
        ret = []
        for interface in interfaces:
            ret.append(self.process_interface(container, interface))
        return ret

    @staticmethod
    def get_interface_index(container) -> int:
        try:
            ret = int(container.get('iflink'))
        except (TypeError, ValueError):
            ret = None
        return ret

    def process_interface(self, container, interface_details) -> dict:
        interface = {
            'vnic_type': 'container_vnic',
            'host': container['host']
        }
        if 'network' in container:
            interface['network'] = container['network']
        interface.update(interface_details)
        self.set_folder_parent(interface, 'vnic',
                               master_parent_type='container',
                               master_parent_id=container['id'],
                               parent_id='{}-vnics'.format(container['id']),
                               parent_type='vnics_folder',
                               parent_text='vNICs')
        return interface
