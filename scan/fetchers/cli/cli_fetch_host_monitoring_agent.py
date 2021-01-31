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

from base.utils.constants import MonitoringAgentType
from scan.fetchers.cli.cli_fetcher import CliFetcher
import toml


class CliFetchHostMonitoringAgent(CliFetcher):
    TELEGRAF_CMD = 'cat /etc/telegraf.conf 2>/dev/null || echo'

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex("-")]

        agents = []
        # TODO: more agent types
        telegraf_agent = self.get_telegraf_agent(host_id)
        if telegraf_agent:
            agents.append(telegraf_agent)

        return agents

    def get_telegraf_agent(self, host_id: str) -> Optional[dict]:
        agent_string = self.run(cmd=self.TELEGRAF_CMD, ssh_to_host=host_id)
        if not agent_string:
            return None

        try:
            parsed_config = toml.loads(agent_string)
        except toml.TomlDecodeError:
            self.log.error("Failed to parse valid toml from telegraf config file")
            return None

        doc = self.build_agent_document(host_id=host_id, agent_type=MonitoringAgentType.TELEGRAF.value)
        doc['configuration'] = parsed_config
        return doc

    @staticmethod
    def build_agent_document(host_id: str, agent_type: str) -> dict:
        return {
            'type': 'monitoring_agent',
            'agent_type': agent_type,
            'host': host_id,
            'id': '{}-{}'.format(host_id, agent_type),
            'name': '{}-{}'.format(host_id, agent_type),
        }
