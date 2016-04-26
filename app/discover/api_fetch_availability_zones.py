from api_access import ApiAccess
import json

class ApiFetchAvailabilityZones(ApiAccess):
  def __init__(self):
    super(ApiFetchAvailabilityZones, self).__init__()
    self.endpoint = ApiAccess.base_url.replace(":5000", ":8774")

  def get(self, id):
    project = id
    token = self.v2_auth_pwd(project)
    if not token:
        return []
    # we use os-availability-zone/detail rather than os-availability-zone,
    # because the later does not inclde the "internal" zone in the results
    req_url = self.endpoint + "/v2/" + token["tenant"]["id"] + \
      "/os-availability-zone/detail"
    headers = {
      "X-Auth-Project-Id": id,
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    if "status" in response and int(response["status"]) != 200:
      return []
    ret = []
    if not "availabilityZoneInfo" in response:
      return []
    azs = response["availabilityZoneInfo"]
    if not azs:
      return []
    for doc in azs:
      doc["id"] = doc["zoneName"]
      doc["name"] = doc.pop("zoneName")
      doc["parent_type"] = "region"
      doc["parent_id"] = "RegionOne"
      doc["available"] = doc["zoneState"]["available"]
      doc.pop("zoneState")
      ret.append(doc)
    return ret
