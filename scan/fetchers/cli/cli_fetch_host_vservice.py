###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
import re

from base.utils.constants import NETWORK_AGENT_TYPES, MISC_AGENT_TYPE
from base.utils.inventory_mgr import InventoryMgr
from base.utils.string_utils import plural
from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.db.db_access import DbAccess


class CliFetchHostVservice(CliFetcher, DbAccess):
    def __init__(self):
        super(CliFetchHostVservice, self).__init__()
        # match only DHCP agent and router (L3 agent)
        self.type_re = re.compile("^q(dhcp|router)-")
        self.inv = InventoryMgr()

    def get_vservice(self, host_id, name_space):
        result = {"local_service_id": name_space}
        self.set_details(host_id, result)
        return result

    def set_details(self, host_id, r):
        # keep the index without prefix
        id_full = r["local_service_id"].strip()
        prefix = id_full[:id_full.index('-')]
        id_clean = id_full[len(prefix)+1:]
        r["service_type"] = prefix[1:]
        name = self.get_router_name(r, id_clean) if r["service_type"] == "router" else self.get_network_name(id_clean)
        r["name"] = "{}-{}".format(prefix, name)
        r["host"] = host_id
        r["id"] = "{}-{}".format(host_id, id_full)
        if r.get('admin_state_up') in (0, 1):
            r['admin_state_up'] = bool(r['admin_state_up'])
        self.set_agent_type(r)

    def get_network_name(self, network_id):
        query = """
                SELECT name
                FROM {}.networks
                WHERE id = %s
                """.format(self.neutron_db)
        results = self.get_objects_list_for_id(query, "router", network_id)
        if not list(results):
            return network_id
        for db_row in results:
            return db_row["name"]

    def get_router_name(self, r, router_id):
        query = """
                SELECT *
                FROM {}.routers
                WHERE id = %s
                """.format(self.neutron_db)
        results = self.get_objects_list_for_id(query, "router",
                                               router_id.strip())
        for db_row in results:
            r.update(db_row)
        return r["name"]

    # dynamically create sub-folder for vService by type
    @staticmethod
    def set_agent_type(o):
        o["master_parent_id"] = "{}-vservices".format(o["host"])
        o["master_parent_type"] = "vservices_folder"
        agent_type = o["service_type"]
        agent = NETWORK_AGENT_TYPES.get(agent_type, MISC_AGENT_TYPE)
        o.update({
            "parent_id": "{}-{}s".format(o["master_parent_id"], agent_type),
            "parent_type": "vservice_{}_folder".format(plural(agent_type)),
            "parent_text": agent.folder_text
        })
