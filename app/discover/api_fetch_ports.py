from api_access import ApiAccess
from inventory_mgr import InventoryMgr

class ApiFetchPorts(ApiAccess):
  def __init__(self):
    super(ApiFetchPorts, self).__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    # use project admin credentials, to be able to fetch all ports
    token = self.v2_auth_pwd("admin")
    if not token:
        return []
    ret = []
    for region in self.regions:
      ret.extend(self.get_ports_for_region(region, token))
    return ret

  def get_ports_for_region(self, region, token):
    endpoint = self.get_region_url_nover(region, "neutron")
    req_url = endpoint + "/v2.0/ports"
    headers = {
      "X-Auth-Project-Id": "admin",
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    if not "ports" in response:
      return []
    ports = response["ports"]
    for doc in ports:
      doc["parent_type"] = "network"
      doc["parent_id"] = doc["network_id"]
      # get the project name
      net = self.inv.get_by_id(self.get_env(), doc["network_id"])
      if net:
        doc["name"] = net["name"] + "-" + doc["mac_address"]
      else:
        doc["name"] = doc["id"]
      project = self.inv.get_by_id(self.get_env(), doc["tenant_id"])
      if project:
        doc["project"] = project["name"]
    return ports
