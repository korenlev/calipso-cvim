from discover.api_access import ApiAccess


class ApiFetchRegions(ApiAccess):
    def __init__(self):
        super(ApiFetchRegions, self).__init__()
        self.endpoint = ApiAccess.base_url

    def get(self, id):
        token = self.v2_auth_pwd(self.admin_project)
        token = self.v2_auth_pwd("admin")
        if not token:
            return []
        # the returned authentication response contains the list of end points
        # and regions
        service_catalog = ApiAccess.auth_response['access']['serviceCatalog']
        env = self.get_env()
        ret = []
        NULL_REGION = "No-Region"
        for service in service_catalog:
            for e in service["endpoints"]:
                if "region" in e:
                    region_name = e.pop("region")
                    region_name = region_name if region_name else NULL_REGION
                else:
                    region_name = NULL_REGION
                if region_name in self.regions.keys():
                    region = self.regions[region_name]
                else:
                    region = {
                        "id": region_name,
                        "name": region_name,
                        "endpoints": {}
                    }
                    ApiAccess.regions[region_name] = region
                region["parent_type"] = "regions_folder"
                region["parent_id"] = env + "-regions"
                e["service_type"] = service["type"]
                region["endpoints"][service["name"]] = e
        ret.extend(list(ApiAccess.regions.values()))
        return ret
