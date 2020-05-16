###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from scan.fetchers.cli.cli_fetcher import CliFetcher
import toml


class CliFetchHostMonitoringAgent(CliFetcher):
    # todo: class will get agent_type in the future
    AGENT_TYPE = 'telegraf'
    AGENT_CMD = 'cat /etc/telegraf.conf'

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]
        parsed_config = {}
        if self.AGENT_TYPE == 'telegraf':
            agent_string = self.run(cmd=self.AGENT_CMD, ssh_to_host=host_id)
            parsed_config = toml.loads(agent_string)
        agents = []
        try:
            agents.append({
                'type': 'monitoring_agent',
                'agent_type': self.AGENT_TYPE,
                'parent_id': parent_id,
                'parent_type': 'monitoring_agents_folder',
                'id': '{}-{}'.format(host_id, self.AGENT_TYPE),
                'name': '{}-{}'.format(host_id, self.AGENT_TYPE),
                'host': host_id,
                'configuration': parsed_config
                })
        except IndexError:
            print('agents not found on host {}'.format(host_id))

        return agents

