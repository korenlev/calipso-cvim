from api_access import ApiAccess

class ApiFetchAvailabilityZones(ApiAccess):
  def __init__(self):
    super(ApiFetchAvailabilityZones, self).__init__()

  def get(self, id):
    project = id
    token = self.v2_auth_pwd(project)
    if not token:
        return []
    ret = []
    for region in self.regions:
      ret.extend(self.get_for_region(project, region, token))
    return ret

  def get_for_region(self, project, region, token):
    # we use os-availability-zone/detail rather than os-availability-zone,
    # because the later does not inclde the "internal" zone in the results
    endpoint = self.get_region_url_nover(region, "nova")
    req_url = endpoint + "/v2/" + token["tenant"]["id"] + \
      "/os-availability-zone/detail"
    headers = {
      "X-Auth-Project-Id": project,
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
