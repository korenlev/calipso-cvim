###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.fetchers.cli.cli_fetcher import CliFetcher
from discover.fetchers.cli.cli_fetch_interface_hardware_details_vpp \
    import CliFetchInterfaceHardwareDetailsVpp
from utils.inventory_mgr import InventoryMgr


class KubeFetchVnicsVpp(CliFetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.if_details_fetcher = CliFetchInterfaceHardwareDetailsVpp()

    def set_env(self, env):
        super().set_env(env)
        self.if_details_fetcher.set_env(env)

    def get(self, host_id: str) -> list:
        cmd = 'vppctl show ip arp'
        lines = self.run_fetch_lines(cmd, ssh_to_host=host_id)
        ret = []
        for l in lines:
            line = l.strip()
            if line.startswith('Time'):
                continue
            if line.startswith('Proxy arps enabled for:'):
                break
            interface = self.process_interface(host_id, line)
            if interface:
                ret.append(self.process_interface(host_id, line))
        self.if_details_fetcher.add_hardware_interfaces_details(host_id, ret)
        return ret

    def process_interface(self, host_id, interface_details) -> dict:
        # parse interface details line like this:
        #  Time           IP4       Flags      Ethernet              Interface
        #  1.6414  192.168.30.1    SN    1a:2b:3c:4d:5e:01 loop0
        #  1.6494  192.168.30.2    SN    1a:2b:3c:4d:5e:02 loop0
        #  1.3167    10.1.2.2      SN    00:00:00:00:00:02 tap1
        details = interface_details.split()
        if len(details) < 5:
            self.log.error('incorrect interface line for host {}: {}'
                           .format(host_id, interface_details))
            return dict()
        interface = dict(name=details[4], mac_address=details[3],
                         ip_address=details[1], host=host_id)
        if not interface['name'].startswith('tap'):
            return dict()
        interface['id'] = '{}-{}'.format(host_id, interface['name'])
        return interface
