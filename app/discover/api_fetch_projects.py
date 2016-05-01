from api_access import ApiAccess

class ApiFetchProjects(ApiAccess):
  def __init__(self):
    super(ApiFetchProjects, self).__init__()
  
  def get(self, id):
    token = self.v2_auth_pwd("admin")
    if not token:
        return []
    ret = []
    for region in self.regions:
      ret.extend(self.get_for_region(region, token))
    return ret

  def get_for_region(self, region, token):
    endpoint = self.get_region_url_nover(region, "keystone")
    req_url = endpoint + "/v2.0/tenants"
    headers = {
      "X-Auth-Project-Id": "admin",
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    response = [t for t in response["tenants"] if t["name"] != "services"]
    return response
