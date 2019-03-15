###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.inventory_mgr import InventoryMgr
from base.utils.origins import Origin
from scan.fetchers.api.api_access import ApiAccess
from scan.fetchers.db.db_fetch_instances import DbFetchInstances


class ApiFetchHostInstances(ApiAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.endpoint = None
        self.projects = None
        self.db_fetcher = None

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.endpoint = self.base_url.replace(":5000", ":8774")
        self.db_fetcher = DbFetchInstances()

    def get_projects(self):
        if not self.projects:
            projects_list = self.inv.get(self.get_env(), "project", None)
            self.projects = [p["name"] for p in projects_list]

    def get(self, id):
        self.get_projects()
        host_id = id[:id.rindex("-")]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host or "Compute" not in host.get("host_type", ""):
            return []
        instances_found = self.get_instances_from_api(host_id)
        self.db_fetcher.get_instance_data(instances_found)
        return instances_found

    def get_instances_from_api(self, host_name):
        token = self.auth(self.admin_project)
        if not token:
            return []
        tenant_id = token["tenant"]["id"]
        req_url = self.endpoint + "/v2/" + tenant_id + "/os-hypervisors/" + host_name + "/servers"
        response = self.get_url(req_url, {"X-Auth-Token": token["id"]})
        ret = []
        if not "hypervisors" in response:
            return []
        if not "servers" in response["hypervisors"][0]:
            return []
        for doc in response["hypervisors"][0]["servers"]:
            doc["id"] = doc["uuid"]
            doc["host"] = host_name
            doc["local_name"] = doc.pop("name")
            ret.append(doc)
        self.log.info("found %s instances for host: %s", str(len(ret)), host_name)
        return ret
