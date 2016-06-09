from api_access import ApiAccess
from inventory_mgr import InventoryMgr

class ApiFetchNetworks(ApiAccess):
  def __init__(self):
    super(ApiFetchNetworks, self).__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    # use project admin credentials, to be able to fetch all networks
    token = self.v2_auth_pwd("admin")
    if not token:
        return []
    ret = []
    for region in self.regions:
      ret.extend(self.get_for_region(region, token))
    return ret

  def get_for_region(self, region, token):
    endpoint = self.get_region_url_nover(region, "neutron")
    req_url = endpoint + "/v2.0/networks"
    headers = {
      "X-Auth-Project-Id": "admin",
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    if not "networks" in response:
      return []
    networks = response["networks"]
    req_url = endpoint + "/v2.0/subnets"
    response = self.get_url(req_url, headers)
    subnets_hash = {}
    if "subnets" in response:
      # create a hash subnets, to allow easy locating of subnets
      subnets = response["subnets"]
      for s in subnets:
        subnets_hash[s["id"]] = s
    for doc in networks:
      doc["master_parent_type"] = "project"
      doc["master_parent_id"] = doc["tenant_id"]
      doc["parent_type"] = "networks_folder"
      doc["parent_id"] = doc["tenant_id"] + "-networks"
      doc["parent_text"] = "Networks"
      # get the project name
      project = self.inv.get_by_id(self.get_env(), doc["tenant_id"])
      if project:
        doc["project"] = project["name"]
      subnets_details = {}
      gateway_ips = []
      for s in doc["subnets"]:
        try:
          subnet = subnets_hash[s]
          gateway_ips.append(subnet["gateway_ip"])
          subnets_details[subnet["name"]] = subnet
        except KeyError:
          pass
      if subnets_details:
        doc["subnets"] = subnets_details
        doc["gateway_ips"] = gateway_ips
    return networks
