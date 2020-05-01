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


class CliFetchHostOsds(CliFetcher):

    OSDS_METADATA_CMD = 'cephmon ceph osd metadata -f json {}'

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
            self.log.error("CliFetchHostOsds: host not found: " + host_id)
            return []
        if "host_type" not in host:
            self.log.error("host does not have host_type: {}".format(host_id))
            return []
        host_types = host["host_type"]
        if not [t for t in self.ACCEPTED_HOST_TYPES if t in host_types]:
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
