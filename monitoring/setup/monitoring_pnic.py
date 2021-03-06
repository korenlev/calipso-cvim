###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from monitoring.setup.monitoring_simple_object import MonitoringSimpleObject


class MonitoringPnic(MonitoringSimpleObject):

    def __init__(self, env):
        super().__init__(env)

    # add monitoring setup for remote host
    def create_setup(self, o):
        type = 'host_pnic'
        env_config = self.configuration.get_env_config()
        vpp_or_ovs = 'vpp' if 'VPP' in env_config['mechanism_drivers'] \
            else 'ovs'
        type_str = '{}_{}'.format(type, vpp_or_ovs)
        self.setup(type, o, values={'check_type': type_str,
                                    'local_name': o['local_name']})

