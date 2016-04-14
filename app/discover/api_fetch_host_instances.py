from api_access import ApiAccess
from inventory_mgr import InventoryMgr
from scanner import Scanner
import json

import httplib2 as http
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
    
class ApiFetchHostInstances(ApiAccess):
  def __init__(self):
    super(ApiFetchHostInstances, self).__init__()
    self.inv = InventoryMgr()
    self.endpoint = ApiAccess.base_url.replace(":5000", ":8774")
  
  def get(self, id):
    host_name = id.replace("-instances", "")
    host = self.inv.getSingle(self.get_env(), "host", host_name)
    if host["host_type"] == "Network Node":
      return []
    os_id = host["os_id"]
    instances_found = []
    for project in host["projects"]:
      instances_found.extend(self.get_instances_for_project(os_id, project))
    return instances_found

  def get_instances_for_project(self, os_id, project):
    token = self.v2_auth_pwd(project)
    tenant_id = token["tenant"]["id"]
    req_url = self.endpoint + "/v2/" + tenant_id + \
      "/os-hypervisors/" + os_id + "/servers"
    response = self.get_url(req_url, {"X-Auth-Token": token["id"]})
    ret = []
    if not "hypervisors" in response:
      return []
    if not "servers" in response["hypervisors"][0]:
      return []
    for doc in response["hypervisors"][0]["servers"]:
        doc["id"] = doc["uuid"]
        doc["local_name"] = doc.pop("name")
        ret.append(doc)
    return ret
