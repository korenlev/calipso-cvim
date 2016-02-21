from api_access import ApiAccess
import json

import httplib2 as http
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
    
class ApiFetchProjects(ApiAccess):
  def __init__(self):
    super(ApiFetchProjects, self).__init__()
  
  def get(self, id):
    admin_endpoint = ApiAccess.base_url.replace(":5000", ":7777")
    req_url = admin_endpoint + "/v2.0/tenants"
    response = ApiAccess.get_url(req_url, {"X-Auth-Token": ApiAccess.admin_token})
    response = [t for t in response["tenants"] if t["name"] != "services"]
    return response
