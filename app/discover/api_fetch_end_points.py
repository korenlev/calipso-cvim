# fetch the end points for a given project (tenant)
# return list of regions, to allow further recursive scanning

from discover.api_access import ApiAccess
from utils.util import Util

class ApiFetchEndPoints(ApiAccess, Util):
  
  def __init__(self):
    super(ApiFetchEndPoints, self).__init__()
    
  
  def get(self, id):
    if id != "admin":
      return [] # XXX currently having problems authenticating to other tenants
    self.v2_auth_pwd(id)
    
    environment = ApiAccess.config.get_env()
    regions = []
    services = ApiAccess.body_hash['access']['serviceCatalog']
    endpoints = []
    for s in services:
      if s["type"] != "identity":
        next
      e = s["endpoints"][0]
      e["environment"] = environment
      e["project"] = id
      e["type"] = "endpoint"
      endpoints.append(e)
    return endpoints
