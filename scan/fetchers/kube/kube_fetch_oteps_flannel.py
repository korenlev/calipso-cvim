###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import json

from base.fetcher import Fetcher
from base.utils.constants import EnvironmentFeatures
from base.utils.inventory_mgr import InventoryMgr


class KubeFetchOtepsFlannel(Fetcher):

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    FLANNEL_PREFIX = 'flannel.alpha.coreos.com/'
    PUBLIC_IP_KEY = FLANNEL_PREFIX + 'public-ip'
    BACKEND_TYPE = FLANNEL_PREFIX + 'backend-type'
    BACKEND_DATA = FLANNEL_PREFIX + 'backend-data'
    OTEP_MAC_ATTR = 'VtepMAC'
    OTEP_UDP_PORT = 8285

    def get(self, vedge_id) -> list:
        host_id = vedge_id.replace('-vedge', '')
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find host by ID: {}'.format(host_id))
            return []
        annotations = host.get('annotations', {})
        ip_address = annotations.get(self.PUBLIC_IP_KEY, '')
        overlay_type = annotations.get(self.BACKEND_TYPE, '')
        backend_data = annotations.get(self.BACKEND_DATA, {})
        if isinstance(backend_data, str):
            backend_data = json.loads(backend_data)
        otep_mac = backend_data.get(self.OTEP_MAC_ATTR, '')
        doc = {
            'id': '{}-otep'.format(host_id),
            'name': '{}-otep'.format(host['name']),
            'host': host['name'],
            'parent_type': 'vedge',
            'parent_id': vedge_id,
            'ip_address': ip_address,
            'overlay_type': overlay_type,
            'overlay_mac_address': otep_mac,
            'ports': self.get_ports(host['name'], ip_address, overlay_type),
            'udp_port': self.OTEP_UDP_PORT
        }
        return [doc]

    def get_ports(self, host: str, ip: str, overlay_type: str) -> dict:
        ports = dict()
        existing_oteps = self.inv.get_by_field(self.env, 'otep')
        for other_otep in existing_oteps:
            port = self.get_port(overlay_type, ip, other_otep['ip_address'],
                                 other_otep['host'])
            ports[port['name']] = port
            self.add_port_to_other_otep(other_otep, ip, host)
        return ports

    def add_port_to_other_otep(self, other_otep: dict, local_ip: str,
                               local_host: str):
        other_ports = other_otep.get('ports', {})
        port_in_other = self.get_port(other_otep['overlay_type'],
                                      other_otep['ip_address'],
                                      local_ip, local_host)
        other_ports[port_in_other['name']] = port_in_other
        other_otep['ports'] = other_ports
        self.inv.set(other_otep)
        # repeat call to create_setup() as initial call
        # did not include this port
        if self.inv.is_feature_supported(self.env,
                                         EnvironmentFeatures.MONITORING):
            self.inv.monitoring_setup_manager.create_setup(other_otep)

    PORT_ID_PREFIX = 'vxlan-remote-'

    @staticmethod
    def get_port_id(remote_host_id: str) -> str:
        return '{}{}'.format(KubeFetchOtepsFlannel.PORT_ID_PREFIX, remote_host_id)

    @staticmethod
    def get_port(overlay_type: str, local_ip: str,
                 remote_ip: str, remote_host: str) -> dict:
        port_id = KubeFetchOtepsFlannel.get_port_id(remote_host)
        return {
            'name': port_id,
            'type': overlay_type,
            'remote_host': remote_host,
            'interface': port_id,
            'options': {
                'local_ip': local_ip,
                'remote_ip': remote_ip
            }
        }
