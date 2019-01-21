###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from scan.fetchers.api.api_access import ApiAccess


class ApiFetchProjects(ApiAccess):
    def __init__(self):
        super(ApiFetchProjects, self).__init__()

    def get(self, project_id):
        token = self.auth(self.admin_project)
        if not token:
            return []
        if not self.regions:
            self.log.error('No regions found')
            return []

        ret = []
        for region in self.regions:
            projects = self.get_projects_for_api_user(region, token)
            if self.keystone_client.tenants_enabled:
                tenants = self.get_tenants_for_region(region, token)
                ret.extend(t for t in tenants if t['name'] in (p['name'] for p in projects))
            else:
                ret.extend(projects)
        return ret

    def get_projects_for_api_user(self, region, token):
        if not token:
            token = self.auth(self.admin_project)
            if not token:
                return []

        endpoint = self.get_region_url_nover(region, "keystone")
        headers = {
            'X-Auth-Project-Id': self.admin_project,
            'X-Auth-Token': token['id']
        }
        # get the list of projects accessible by the admin user
        req_url = endpoint + '/v3/projects'
        response = self.get_url(req_url, headers)
        if not response or 'projects' not in response:
            return []
        # 'services' project does not contain any networks or ports
        return [p for p in response['projects'] if p.get("name") != "services"]

    def get_tenants_for_region(self, region, token):
        endpoint = self.get_region_url_nover(region, "keystone")
        req_url = endpoint + self.keystone_client.tenants_url
        headers = {
            "X-Auth-Project-Id": self.admin_project,
            "X-Auth-Token": token["id"]
        }
        response = self.get_url(req_url, headers)
        if not isinstance(response, dict):
            self.log.error('invalid response to /tenants request: not dict')
            return []
        tenants_list = response.get("tenants", [])
        if not isinstance(tenants_list, list):
            self.log.error('invalid response to /tenants request: '
                           'tenants value is n ot a list')
            return []
        return tenants_list
