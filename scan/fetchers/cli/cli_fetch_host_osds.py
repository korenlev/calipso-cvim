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


class CliFetchHostOsds(CliFetcher, HostTypeValidator):

    OSDS_METADATA_CMD = 'cephmon ceph osd metadata -f json {}'

    ACCEPTED_HOST_TYPES = [HostType.STORAGE.value]

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host or not self.validate_host(host_id):
            return []

        host_osds = host.get('ceph_osds', [])
        ceph_osds = [{
            'metadata': self.run_fetch_json_response(self.OSDS_METADATA_CMD.format(o.get('name', ''))),
            'type': 'osd',
            'parent_id': parent_id,
            'parent_type': 'osds_folder',
            'id': '{}|{}'.format(host_id, o.get('name', '')),
            'name': o.get('name', ''),
            'host': host_id,
        } for o in host_osds]
        return ceph_osds
