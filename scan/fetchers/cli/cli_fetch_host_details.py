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


class CliFetchHostDetails(CliFetcher):

    CEPH_OSD_DF_CMD = "cephmon ceph osd df -f json"
    CEPH_NODE_LS_CMD = "cephmon ceph node ls -f json"
    CEPH_STATUS_CMD = "cephmon ceph -s -f json"
    CEPH_PG_STATS_CMD = "cephmon ceph pg stat -f json"
    CEPH_OSD_STATS_CMD = "cephmon ceph osd stat -f json"
    CEPH_FEATURES_CMD = "cephmon ceph features -f json"

    def fetch_host_os_details(self, doc: dict) -> None:
        cmd = 'cat /etc/os-release && echo "ARCHITECURE=`arch`"'
        lines = self.run_fetch_lines(cmd, ssh_to_host=doc['host'])
        os_attributes = {}
        attributes_to_fetch = {
            'NAME': 'name',
            'VERSION': 'version',
            'ID': 'ID',
            'ID_LIKE': 'ID_LIKE',
            'ARCHITECURE': 'architecure'
        }
        for attr in attributes_to_fetch:
            matches = [l for l in lines if l.startswith(attr + '=')]
            if matches:
                line = matches[0]
                attr_name = attributes_to_fetch[attr]
                os_attributes[attr_name] = line[line.index('=')+1:].strip('"')
        if os_attributes:
            doc['OS'] = os_attributes

    def fetch_storage_hosts_details(self, ret: list, region: str) -> list:
        osd_df_response = self.run_fetch_json_response(self.CEPH_OSD_DF_CMD)
        osds = osd_df_response.get("nodes", [])

        node_ls_response = self.run_fetch_json_response(self.CEPH_NODE_LS_CMD)
        stores = [
            {
                'name': name,
                'osds': [osd for osd in osds if int(osd['id']) in osd_ids],
            } for name, osd_ids in node_ls_response.get('osd', {}).items()
        ]

        # TODO: Remove/reduce redundancy of this data
        controllers = [
            {
                'name': name,
                'mon_ids': mon_ids
            } for name, mon_ids in node_ls_response.get('mon', {}).items()
        ]

        # TODO: Remove/reduce redundancy of this data
        cluster_status = self.run_fetch_json_response(self.CEPH_STATUS_CMD)
        pg_stats = self.run_fetch_json_response(self.CEPH_PG_STATS_CMD)
        osd_stats = self.run_fetch_json_response(self.CEPH_OSD_STATS_CMD)
        features = self.run_fetch_json_response(self.CEPH_FEATURES_CMD)

        for store in stores:
            ceph_details = {
                'ceph_features': features,
                'cluster_status': cluster_status,
                'pg_stats': pg_stats,
                'osd_stats': osd_stats,
                'ceph_controllers': controllers,
                'osds': store['osds']
            }

            host_matched = False
            for h in ret:
                if store['name'] == h['name']:
                    # aio controllers may also be ceph storage nodes, so we'll only append new data:
                    h.update(ceph_details)
                    host_matched = True

            # completely new host of type Storage:
            if not host_matched:
                host = {
                    'id': store['name'],
                    'host': store['name'],
                    'name': store['name'],
                    'parent_id': 'region|{}'.format(region),
                    'parent_type': 'region',
                    'zone': 'unknown',
                    'host_type': [HostType.STORAGE.value]}
                host.update(ceph_details)
                self.fetch_host_os_details(host)
                ret.append(host)
        return ret
