# fetch the end points for a given project (tenant)
# return list of regions, to allow further recursive scanning

from api_access import ApiAccess
from fetcher import Fetcher
from util import Util

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
    for s in services:
      if s["type"] != "identity":
        next
      e = s["endpoints"][0]
      e["environment"] = environment
      e["project"] = id
      e["type"] = "endpoint"
      Fetcher.inventory.set(e)
      region = {
        "id": e["region"],
        "environment": environment,
        "text": e["region"],
        "descendants": 3,
        "parent_id": environment,
        "parent_type": "environment"
      }
      regions.append(region)
    
    return regions
