from api_access import ApiAccess
from inventory_mgr import InventoryMgr
import json

class ApiFetchNetworks(ApiAccess):
  def __init__(self):
    super(ApiFetchNetworks, self).__init__()
    self.endpoint = ApiAccess.base_url.replace(":5000", ":9696")
    self.inv = InventoryMgr()

  def get(self, id):
    # use project admin credentials, to be able to fetch all networks
    token = self.v2_auth_pwd("admin")
    if not token:
        return []
    req_url = self.endpoint + "/v2.0/networks"
    headers = {
      "X-Auth-Project-Id": token["tenant"]["id"],
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    if not "networks" in response:
      return []
    networks = response["networks"]
    req_url = self.endpoint + "/v2.0/subnets"
    response = self.get_url(req_url, headers)
    subnets_hash = {}
    if "subnets" in response:
      # create a hash subnets, to allow easy locating of subnets
      subnets = response["subnets"]
      for s in subnets:
        subnets_hash[s["id"]] = s
    for doc in networks:
      doc["parent_type"] = "project"
      doc["parent_id"] = doc["tenant_id"]
      # get the project name
      project = self.inv.get_by_id(self.get_env(), doc["tenant_id"])
      if project:
        doc["project"] = project["name"]
      subnets_details = {}
      for s in doc["subnets"]:
        try:
          subnet = subnets_hash[s]
          subnets_details[subnet["name"]] = subnet
        except KeyError:
          pass
      if subnets_details:
        doc["subnets"] = subnets_details
    return networks
