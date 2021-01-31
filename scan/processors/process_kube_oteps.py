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

from base.utils.origins import Origin
from scan.fetchers.kube.kube_fetch_oteps_base import KubeFetchOtepsBase
from scan.processors.processor import Processor


class ProcessKubeOteps(Processor, KubeFetchOtepsBase):
    PREREQUISITES = ['ProcessCalicoVedges']
    CALICO_PORT_ID_PREFIX = 'ipip-remote-'
    CALICO_TUNNEL_PREFIX = 'tunl'
    CALICO_CLUSTER_TYPE_KEY = 'CLUSTER_TYPE'
    CALICO_FELIX_ATT = 'FELIX'
    CALICO_NAME_ATT = 'CALICO'

    def __init__(self):
        super().__init__()
        self.environment_type: Optional[str] = None

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.environment_type = self.configuration.get_env_type()

    def run(self):
        super().run()
        if self.environment_type != 'Kubernetes':
            return

        vedges = self.find_by_type("vedge")
        for vedge in vedges:
            vedge_id = vedge.get('id', '')
            host_id = vedge_id.replace('-vedge', '')
            host = self.inv.find_one({'name': host_id}, collection='inventory')
            if not host:
                self.log.error('failed to find host by ID: {}'.format(host_id))
                return []

            overlay_interface = ''
            overlay_state = ''

            overlay_data = []
            host_interfaces = host.get('interfaces', [])
            for i in host_interfaces:
                if ProcessKubeOteps.CALICO_TUNNEL_PREFIX in i['name']:
                    overlay_interface = i['id']
                    overlay_state = i['state']
                    overlay_data = i['lines']
                    break

            otep = self.inv.find_one({'parent_id': vedge_id}, collection='inventory')

            overlay_type = ''
            config = []
            vedge_configs = vedge.get('configurations')
            if vedge_configs:
                env = vedge_configs.get('Env')
                if env:
                    for env_var in env:
                        env_var_parts = env_var.split('=')
                        env_var_key = env_var_parts[0]
                        env_var_val = "=".join(env_var_parts[1:])
                        if ProcessKubeOteps.CALICO_CLUSTER_TYPE_KEY in env_var_key:
                            overlay_type = env_var_val
                        if (
                                ProcessKubeOteps.CALICO_FELIX_ATT in env_var_key
                                or ProcessKubeOteps.CALICO_NAME_ATT in env_var_key
                        ):
                            config.append(env_var)

            otep.update({
                "overlay_interface": overlay_interface,
                "overlay_state": overlay_state,
                "overlay_data": overlay_data,
                "overlay_type": overlay_type,
                "config": config,
                "vconnector": vedge.get('vconnector', ''),
                'ports': self.get_ports(
                    host=host['name'], ip=otep.get('ip_address', ''), overlay_type=overlay_type
                ),
            })
            self.inv.set(otep)

    @staticmethod
    def get_port_id(remote_host_id: str) -> str:
        return '{}{}'.format(ProcessKubeOteps.CALICO_PORT_ID_PREFIX, remote_host_id)

    @classmethod
    def get_port(cls, overlay_type: str, local_ip: str,
                 remote_ip: str, remote_host: str) -> dict:
        port_id = ProcessKubeOteps.get_port_id(remote_host)
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
