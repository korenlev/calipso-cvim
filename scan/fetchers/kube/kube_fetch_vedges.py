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
from scan.fetchers.cli.cli_fetch_kube_vedge_details import CliFetchKubeVedgeDetails


class KubeFetchVedges(Fetcher):
    CALICO_PREFIX = 'projectcalico.org/'
    PUBLIC_IP_KEY = '{}IPv4Address'.format(CALICO_PREFIX)
    TUNNEL_IP_KEY = '{}IPv4IPIPTunnelAddr'.format(CALICO_PREFIX)
    CALICO_DEFAULT_AS = 64512  # TODO: discover it

    def __init__(self):
        super().__init__()
        self.details_fetcher = CliFetchKubeVedgeDetails()

    def set_env(self, env):
        super().set_env(env)
        self.details_fetcher.set_env(env)

    def get(self, host_id) -> list:
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find host: {}'.format(host_id))
            return []

        search_condition = {
            'environment': self.get_env(),
            'type': 'pod',
            'host': host['name'],
            # the following allows matching by several labels
            '$or': [{"labels.k8s-app": "flannel"}, {"labels.app": "flannel"}, {"labels.k8s-app": "calico-node"}]
        }

        ip_address = ''
        tunnel_address = ''
        annotations = host.get('annotations')
        if annotations:
            ip_address = annotations.get(self.PUBLIC_IP_KEY, '')
            tunnel_address = annotations.get(self.TUNNEL_IP_KEY, '')

        vedges = self.inv.find_items(search_condition)
        ret = []
        for v in vedges:
            v.update({
                'id': '{}-vedge'.format(host_id),
                'host': host_id,
                'ip_address': ip_address,
                'tunnel_address': tunnel_address
            })

            vedge_type = 'Unknown'
            agent_name = 'Unknown'
            labels = v.get('labels')
            if labels:
                k8s_app = labels.get('k8s-app', '')
                if k8s_app == 'calico-node':
                    vedge_type = KubeVedgeType.CALICO.value
                    agent_name = 'calico-node'
                    v['bgp_as'] = self.CALICO_DEFAULT_AS
                elif k8s_app == 'flannel':
                    vedge_type = KubeVedgeType.FLANNEL.value
                    agent_name = 'kube-flannel'

            v['vedge_type'] = vedge_type
            v['agent_name'] = agent_name
            self.details_fetcher.update_vedge_details(v, host_id)

            self.set_folder_parent(v,
                                   object_type='vedge',
                                   master_parent_type='host',
                                   master_parent_id=host_id,
                                   parent_objects_name='vedges',
                                   parent_text='vEdges')
            ret.append(v)
        return ret
