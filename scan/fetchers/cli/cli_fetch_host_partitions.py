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


class CliFetchHostPartitions(CliFetcher, HostTypeValidator):

    PARTS_CMD = 'lsblk -n -o KNAME,PKNAME,SIZE,PARTLABEL,MOUNTPOINT | grep -E "data|block"'

    ACCEPTED_HOST_TYPES = [HostType.STORAGE.value]

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        if not self.validate_host(host_id):
            return []

        part_lines = self.run_fetch_lines(self.PARTS_CMD, ssh_to_host=host_id)
        parts = []
        for line in part_lines:
            try:
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
            except IndexError:
                continue
        return parts
