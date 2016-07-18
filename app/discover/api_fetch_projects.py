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
    projects_for_user = self.get_projects_for_api_user(region, token)
    return [p for p in ret if p['name'] in projects_for_user] \
      if projects_for_user else ret

  def get_projects_for_api_user(self, region, token):
    token = self.v2_auth_pwd("admin")
    endpoint = self.get_region_url_nover(region, "keystone")
    headers = {
      'X-Auth-Project-Id': 'admin',
      'X-Auth-Token': token['id']
    }
    # first get the list of users to get the user ID
    req_url = endpoint + '/v3/users'
    response = self.get_url(req_url, headers)
    if not response or 'users' not in response:
      return None
    user_name = ApiAccess.api_config['user']
    matches = [u for u in response['users'] if u['name'] == user_name]
    if not matches:
      return None
    user_id = matches[0]['id']
    req_url = endpoint + '/v3/users/' + user_id + "/projects"
    response = self.get_url(req_url, headers)
    if not response or 'projects' not in response:
      return None
    response = [p['name'] for p in response['projects']]
    return response

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
