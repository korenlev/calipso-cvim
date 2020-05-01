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
from base.utils.inventory_mgr import InventoryMgr
from scan.fetchers.cli.cli_fetcher import CliFetcher


class CliFetchHostDisks(CliFetcher):

    DISKS_CMD = 'lsblk -d -n -o KNAME,STATE,SIZE,SERIAL,VENDOR,HCTL,REV,WWN,MODEL'

    ACCEPTED_HOST_TYPES = [HostType.STORAGE.value]

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def set_env(self, env):
        super().set_env(env)

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error("CliFetchHostDisks: host not found: " + host_id)
            return []
        if "host_type" not in host:
            self.log.error("host does not have host_type: {}".format(host_id))
            return []
        host_types = host["host_type"]
        if not [t for t in self.ACCEPTED_HOST_TYPES if t in host_types]:
            return []

        disk_lines = self.run_fetch_lines(self.DISKS_CMD, host_id)
        disks = []
        for line in disk_lines:
            line_parts = line.split()
            disks.append({
                'type': 'disk',
                'parent_id': parent_id,
                'parent_type': 'disks_folder',
                'id': '{}|dev|{}'.format(host_id, line_parts[0]),
                'name': line.split()[0],
                'host': host_id,
                'device': '/dev/{}'.format(line_parts[0]),
                'state': line_parts[1],
                'size': line_parts[2],
                'serial': line_parts[3],
                'vendor': line_parts[4],
                'scsi_address': line_parts[5],
                'revision': line_parts[6],
                'wwn_address': line_parts[7],
                'model': " ".join(line_parts[8:]) if len(line_parts) > 9 else line_parts[8]
            })
        return disks
