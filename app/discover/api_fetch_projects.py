from discover.api_access import ApiAccess


class ApiFetchProjects(ApiAccess):
    def __init__(self):
        super(ApiFetchProjects, self).__init__()

    def get(self, project_id):
        token = self.v2_auth_pwd(self.admin_project)
        if not token:
            return []
        ret = []
        for region in self.regions:
            ret.extend(self.get_for_region(region, token))
        projects_for_user = self.get_projects_for_api_user(region, token)
        return [p for p in ret if p['name'] in projects_for_user] \
            if projects_for_user else ret

    def get_projects_for_api_user(self, region, token):
        if not token:
            token = self.v2_auth_pwd(self.admin_project)
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
            return None
        response = [p['name'] for p in response['projects']]
        return response

    def get_for_region(self, region, token):
        endpoint = self.get_region_url_nover(region, "keystone")
        req_url = endpoint + "/v2.0/tenants"
        headers = {
            "X-Auth-Project-Id": self.admin_project,
            "X-Auth-Token": token["id"]
        }
        response = self.get_url(req_url, headers)
        response = [t for t in response["tenants"] if t["name"] != "services"]
        return response
