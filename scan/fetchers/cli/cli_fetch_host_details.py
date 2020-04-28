###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json

from scan.fetchers.cli.cli_fetcher import CliFetcher


class CliFetchHostDetails(CliFetcher):

    def fetch_host_os_details(self, doc):
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

    def fetch_storage_hosts_details(self, ret, region, ssh_host):
        cmd = 'cephmon ceph osd df'
        osd_lines = self.run_fetch_lines(cmd, ssh_to_host=ssh_host)
        osd_lines.pop(0)
        osds = []
        for line in osd_lines:
            line = line.split()
            if line[0].isdigit():
                osd = {'id': line[0], 'class': line[1], 'weight': line[2],
                       'reweight': line[3], 'size': line[4], 'in_use': line[5],
                       'available': line[6], '%in_use': line[7],
                       'variance': line[8], 'pgs': line[9]}
                osds.append(osd)

        cmd = 'cephmon ceph node ls'
        response = json.loads(self.run(cmd, ssh_to_host=ssh_host))
        stores = []
        stores_dict = response.get('osd')
        for name in stores_dict.keys():
            store_osds = []
            store = {'name': name}
            osd_ids = stores_dict[name]
            for osd in osds:
                if int(osd['id']) in osd_ids:
                    store_osds.append(osd)
            store['osds'] = store_osds
            stores.append(store)
        controllers = []
        conts_dict = response.get('mon')
        for name in conts_dict.keys():
            monitor = {'name': name, 'mon_ids': conts_dict[name]}
            controllers.append(monitor)

        cluster_status = self.run('cephmon ceph -s', ssh_to_host=ssh_host)
        pg_stats = self.run('cephmon ceph pg stat', ssh_to_host=ssh_host)
        osd_stats = self.run('cephmon ceph osd stat', ssh_to_host=ssh_host)
        features = json.loads(self.run('cephmon ceph features', ssh_to_host=ssh_host))

        for store in stores:
            for h in ret:
                dup_names = []
                if store['name'] == h['name']:
                    # aio controllers may also be ceph storage nodes, so we'll only append new data:
                    h['ceph_features'] = features
                    h['cluster_status'] = cluster_status
                    h['pg_stats'] = pg_stats
                    h['osd_stats'] = osd_stats
                    h['controllers'] = controllers
                    h['osds'] = store['osds']
                    dup_names.append(h['name'])
            # completely new host of type Storage:
            if store['name'] not in dup_names:
                host = {'id': store['name'], 'host': store['name'], 'name': store['name'],
                        'parent_id': 'region|{}'.format(region), 'zone': 'unknown', 'parent_type': 'region',
                        'host_type': 'Storage', 'ceph_features': features, 'cluster_status': cluster_status,
                        'pg_stats': pg_stats, 'osd_stats': osd_stats, 'controllers': controllers, 'osds': store['osds']}
                self.fetch_host_os_details(host)
                ret.append(host)
        return ret
