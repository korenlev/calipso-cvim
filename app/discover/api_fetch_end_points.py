# fetch the end points for a given project (tenant)
# return list of regions, to allow further recursive scanning

from discover.api_access import ApiAccess


class ApiFetchEndPoints(ApiAccess):

    def get(self, project_id):
        if project_id != "admin":
            return []  # XXX currently having problems authenticating to other tenants
        self.v2_auth_pwd(project_id)

        environment = ApiAccess.config.get_env_name()
        regions = []
        services = ApiAccess.auth_response['access']['serviceCatalog']
        endpoints = []
        for s in services:
            if s["type"] != "identity":
                continue
            e = s["endpoints"][0]
            e["environment"] = environment
            e["project"] = project_id
            e["type"] = "endpoint"
            endpoints.append(e)
        return endpoints
