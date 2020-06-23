###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################

from base.fetcher import Fetcher
from base.utils.constants import KubeVedgeType


class KubeFetchOtepsCalico(Fetcher):
    CALICO_PREFIX = 'projectcalico.org/'
    PUBLIC_IP_KEY = '{}IPv4Address'.format(CALICO_PREFIX)
    TUNNEL_IP_KEY = '{}IPv4IPIPTunnelAddr'.format(CALICO_PREFIX)
    PORT_ID_PREFIX = 'ipip-remote-'
    OVERLAY_MAC_ADDRESS = "ee:ee:ee:ee:ee:ee"
    OVERLAY_TYPE = "bgp"

    def get(self, vedge_id) -> list:
        host_id = vedge_id.replace('-vedge', '')
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find host by ID: {}'.format(host_id))
            return []
        ip_address = ''
        tunnel_address = ''
        if host.get('annotations', ''):
            annotations = host['annotations']
            ip_address = annotations.get(self.PUBLIC_IP_KEY, '')
            tunnel_address = annotations.get(self.TUNNEL_IP_KEY, '')
        doc = {
            'id': '{}-otep'.format(host_id),
            'name': '{}-otep'.format(host['name']),
            'host': host['name'],
            'ip_address': ip_address,
            'tunnel_address': tunnel_address,
            'vedge_type': KubeVedgeType.CALICO.value,
            "overlay_mac_address": self.OVERLAY_MAC_ADDRESS,
            "overlay_type": self.OVERLAY_TYPE
        }
        return [doc]
