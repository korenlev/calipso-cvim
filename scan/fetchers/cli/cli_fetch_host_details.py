###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional

import yaml

from base.utils.constants import HostType
from base.utils.ssh_connection import SshError
from scan.fetchers.cli.cli_fetcher import CliFetcher


class CliFetchHostDetails(CliFetcher):

    OS_DETAILS_CMD = 'cat /etc/os-release && echo "ARCHITECTURE=`arch`"'
    HOSTNAME_CMD = 'cat /etc/hostname'
    SETUP_DATA_CMD = 'cat /root/openstack-configs/setup_data.yaml'

    CEPH_OSD_DF_CMD = "cephmon ceph osd df -f json"
    CEPH_NODE_LS_CMD = "cephmon ceph node ls -f json"
    CEPH_STATUS_CMD = "cephmon ceph -s -f json"
    CEPH_PG_STATS_CMD = "cephmon ceph pg stat -f json"
    CEPH_OSD_STATS_CMD = "cephmon ceph osd stat -f json"
    CEPH_FEATURES_CMD = "cephmon ceph features -f json"
    CEPH_UTIL_CMD = 'cephmon ceph osd utilization -f json'
    CEPH_QUORUM_CMD = 'cephmon ceph quorum_status -f json'

    # Setup data field -> MongoDB field
    SETUP_DATA_TRANSLATIONS = {
        "PODNAME": "pod_name",
        "PODTYPE": "pod_type",
        "CVIM_MON": "cvim_mon",
        "STORE_BACKEND": "store_backend",
        "VOLUME_DRIVER": "volume_driver",
        "TENANT_NETWORK_TYPES": "tenant_network_types",
        "external_lb_vip_address": "external_lb_vip_address",
        "external_lb_vip_ipv6_address": "external_lb_vip_ipv6_address",
        "internal_lb_vip_address": "internal_lb_vip_address",
        "internal_lb_vip_ipv6_address": "internal_lb_vip_ipv6_address",
        "OPTIONAL_SERVICE_LIST": "optional_service_list",
        "ROLES": "roles",
        "INTEL_SRIOV_PHYS_PORTS": "sriov_phys_ports",
        "INTEL_SRIOV_VFS": "sriov_vfs"
    }

    def fetch_host_os_details(self, doc: dict) -> None:
        lines = self.run_fetch_lines(self.OS_DETAILS_CMD, ssh_to_host=doc['host'])
        os_attributes = {}
        attributes_to_fetch = {
            'NAME': 'name',
            'VERSION': 'version',
            'ID': 'ID',
            'ID_LIKE': 'ID_LIKE',
            'ARCHITECTURE': 'architecture'
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
        node_ls_response = self.run_fetch_json_response(self.CEPH_NODE_LS_CMD)
        if not node_ls_response:
            return ret

        osd_df_response = self.run_fetch_json_response(self.CEPH_OSD_DF_CMD)
        osds = osd_df_response.get("nodes", [])
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
        utilization = self.run_fetch_json_response(self.CEPH_UTIL_CMD)
        quorum = self.run_fetch_json_response(self.CEPH_QUORUM_CMD)

        for store in stores:
            ceph_details = {
                'ceph_features': features,
                'ceph_cluster_status': cluster_status,
                'ceph_pg_stats': pg_stats,
                'ceph_osd_stats': osd_stats,
                'ceph_controllers': controllers,
                'ceph_osds': store['osds'],
                'ceph_utilizations': utilization,
                'ceph_quorum': quorum
            }

            host_matched = False
            for h in ret:
                if store['name'] == h['name']:
                    # aio controllers may also be ceph storage nodes, so we'll only append new data:
                    h.update(ceph_details)
                    h['host_type'].append(HostType.STORAGE.value)
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

    def get_mgmt_node_details(self, mgmt_ip: str, parent_id: str) -> Optional[dict]:
        host_doc = {
            "id": mgmt_ip,
            "id": self.get_hostname(ip_address=mgmt_ip),
            "host": mgmt_ip,
            "name": self.get_hostname(ip_address=mgmt_ip),
            "zone": "unknown",
            "parent_type": "region",
            "parent_id": parent_id,
            "host_type": [HostType.MANAGEMENT.value],
            "ip_address": mgmt_ip,
        }
        # TODO: verify object_name
        self.fetch_host_os_details(doc=host_doc)
        self.fetch_setup_data_details(doc=host_doc)

        # TODO: discover pnics here?

        return host_doc

    def get_hostname(self, ip_address: str = "") -> str:
        """
            Fetch host name by ip address
        :param ip_address: IP of target host
        :return: host name if found, ip address otherwise (in case of any error)
        """
        try:
            lines = self.run_fetch_lines(self.HOSTNAME_CMD, ssh_to_host=ip_address)
        except SshError as e:
            self.log.error(e)
            return ip_address

        return lines[0].strip() if lines else ip_address

    def fetch_setup_data_details(self, doc: dict) -> None:
        """
        Fetch select setup data fields from CVIM setup data

        :param doc: Host document to update inplace
        :return: nothin'
        """
        try:
            setup_data_str = self.run(self.SETUP_DATA_CMD, ssh_to_host=doc['host'])
        except SshError:
            # Missing setup data file is not a fatal error
            return

        try:
            setup_data = yaml.safe_load(setup_data_str)
            if not isinstance(setup_data, dict):
                raise yaml.YAMLError()
        except yaml.YAMLError:
            self.log.error("Failed to parse valid YAML from supplied setup data file")
            return

        cvim_details = {
            key_to: setup_data[key_from]
            for key_from, key_to in self.SETUP_DATA_TRANSLATIONS.items()
            if key_from in setup_data
        }
        doc["cvim_details"] = cvim_details
