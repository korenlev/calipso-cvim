###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################

from base.utils.constants import KubeVedgeType

from scan.processors.processor import Processor


class ProcessCalicoVedges(Processor):
    PREREQUISITES = []

    def update_vedge_ports(self, vedge: dict) -> None:
        # find attached vnics and add to vedge ports
        vnics_search = {
            'environment': self.get_env(),
            'type': 'vnic',
            'host': vedge['host']
        }
        vnics = self.inv.find_items(vnics_search, collection='inventory')

        routing_table = vedge.get('routing_table', [])
        ports = []
        for vnic in vnics:
            for route in routing_table:
                if vnic['name'] in route:
                    port = {
                        'id': vnic.get('local_name', ''),
                        'state': 'up',
                        'name': '{}-{}'.format(vnic['name'], vnic.get('mac_address', '')),
                        'internal': True
                    }
                    ports.append(port)

        vedge['ports'] = ports

    def update_vedge_config(self, vedge: dict) -> None:
        # find the calico container and update vedge with container config
        vedge_container_search = {
            'environment': self.get_env(),
            'type': 'container',
            'host': vedge['host'],
            'name': vedge['agent_name']
        }
        vedge_container = self.inv.find_one(vedge_container_search, collection='inventory')
        if vedge_container:
            vedge['configurations'] = vedge_container.get('config', {})

    def run(self):
        super().run()
        vedges = self.inv.find_items({
            "environment": self.env,
            "type": "vedge",
            "vedge_type": KubeVedgeType.CALICO.value
        })
        for vedge in vedges:
            self.update_vedge_ports(vedge)
            self.update_vedge_config(vedge)
            self.inv.set(vedge)
