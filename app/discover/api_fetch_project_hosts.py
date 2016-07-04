from api_access import ApiAccess
from db_access import DbAccess
from scanner import Scanner
import json

class ApiFetchProjectHosts(ApiAccess, DbAccess):
  def __init__(self):
    super(ApiFetchProjectHosts, self).__init__()

  def get(self, id):
    if id != "admin":
        # do not scan hosts except under project 'admin'
        return []
    token = self.v2_auth_pwd("admin")
    if not token:
        return []
    ret = []
    for region in self.regions:
      ret.extend(self.get_for_region(region, token))
    return ret

  def get_for_region(self, region, token):
    endpoint = self.get_region_url(region, "nova")
    ret = []
    if not token:
      return []
    req_url = endpoint + "/os-availability-zone/detail"
    headers = {
      "X-Auth-Project-Id": "admin",
      "X-Auth-Token": token["id"]
    }
    response = self.get_url(req_url, headers)
    if "status" in response and int(response["status"]) != 200:
      return []
    az_info = response["availabilityZoneInfo"]
    hosts = {}
    for doc in az_info:
      az_hosts = self.get_hosts_from_az(doc)
      for h in az_hosts:
        if h["name"] in hosts:
          continue
        hosts[h["name"]] = h
        ret.append(h)
    # get os_id for hosts using the os-hypervisors API call
    req_url = endpoint + "/os-hypervisors"
    response = self.get_url(req_url, headers)
    if "status" in response and int(response["status"]) != 200:
      return ret
    if "hypervisors" not in response:
      return ret
    for h in response["hypervisors"]:
        hvname = h["hypervisor_hostname"]
        if '.' in hvname and hvname not in hosts:
          hostname = hvname[:hvname.index('.')]
        else:
          hostname = hvname
        try:
          doc = hosts[hostname]
        except KeyError:
            # TBD - add error output
            continue
        doc["os_id"] = str(h["id"])
        self.fetch_compute_node_ip_address(doc, hvname)
    # get more network nodes details
    self.fetch_network_node_details(ret)
    return ret

  def get_hosts_from_az(self, az):
    ret = []
    for h in az["hosts"]:
      doc = self.get_host_details(az, h)
      ret.append(doc)
    return ret

  def get_host_details(self, az, h):
    # for hosts we use the name
    services = az["hosts"][h]
    doc = {
      "id": h,
      "host": h,
      "name": h,
      "zone": az["zoneName"],
      "parent_type": "availability_zone",
      "parent_id": az["zoneName"],
      "services": services,
      "host_type": []
    }
    if "nova-conductor" in services:
      s = services["nova-conductor"]
      if s["available"] and s["active"]:
        self.add_host_type(doc, "Controller")
    if "nova-compute" in services:
      s = services["nova-compute"]
      if s["available"] and s["active"]:
        self.add_host_type(doc, "Compute")
    return doc

  # fetch more details of network nodes from neutron.agents table
  def fetch_network_node_details(self, docs):
    hosts = {}
    for doc in docs:
      hosts[doc["host"]] = doc
    query = """
      SELECT DISTINCT host, host AS id, configurations
      FROM neutron.agents
      WHERE agent_type IN ('Metadata agent', 'DHCP agent', 'L3 agent')
    """
    results = self.get_objects_list(query, "")
    for r in results:
      host = hosts[r["host"]]
      host["config"] = json.loads(r["configurations"])
      self.add_host_type(host, "Network")

  # fetch ip_address from nova.compute_nodes table if possible
  def fetch_compute_node_ip_address(self, doc, h):
    query = """
      SELECT host_ip AS ip_address
      FROM nova.compute_nodes
      WHERE hypervisor_hostname = %s
    """
    results = self.get_objects_list_for_id(query, "", h)
    for db_row in results:
      doc.update(db_row)

  def add_host_type(self, doc, type):
    if not type in doc["host_type"]:
      doc["host_type"].append(type)
