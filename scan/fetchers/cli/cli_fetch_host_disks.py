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


class CliFetchHostDisks(CliFetcher, HostTypeValidator):

    DISKS_CMD = 'lsblk -d -n -o KNAME,STATE,SIZE,SERIAL,VENDOR,HCTL,REV,WWN,MODEL'

    ACCEPTED_HOST_TYPES = [HostType.STORAGE.value, HostType.MANAGEMENT.value]

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        if not self.validate_host(host_id):
            return []

        disk_lines = self.run_fetch_lines(cmd=self.DISKS_CMD, ssh_to_host=host_id)
        disks = []
        for line in disk_lines:
            try:
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
            except IndexError:
                continue
        return disks
