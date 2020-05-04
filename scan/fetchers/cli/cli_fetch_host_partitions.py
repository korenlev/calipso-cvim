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


class CliFetchHostPartitions(CliFetcher):

    PARTS_CMD = 'lsblk -n -o KNAME,PKNAME,SIZE,PARTLABEL,MOUNTPOINT | grep -E "data|block"'
    PART_DEP_CMD = "ceph-disk list /dev/{}"

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
            self.log.error("CliFetchHostPartitions: host not found: " + host_id)
            return []
        if "host_type" not in host:
            self.log.error("host does not have host_type: {}".format(host_id))
            return []
        host_types = host["host_type"]
        if not [t for t in self.ACCEPTED_HOST_TYPES if t in host_types]:
            return []

        part_lines = self.run_fetch_lines(self.PARTS_CMD, host_id)
        parts = []
        for line in part_lines:
            line_parts = line.split()
            parts.append({
                'type': 'partition',
                'parent_id': parent_id,
                'parent_type': 'partitions_folder',
                'id': '{}|dev|{}'.format(host_id, line_parts[0]),
                'name': '{}-{}'.format(line_parts[0], line_parts[4]),
                'host': host_id,
                'device': '/dev/{}'.format(line_parts[0]),
                'master_disk': line_parts[1],
                'size': line_parts[2],
                'label': '{}-{}'.format(line_parts[3], line_parts[4]),
                'mount_point': line_parts[5] if len(line_parts) == 6 else '',
                'osd_partition_type': line_parts[4]
            })
        return parts
