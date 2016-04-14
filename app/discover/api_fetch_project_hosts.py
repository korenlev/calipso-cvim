from api_access import ApiAccess
from db_access import DbAccess
from inventory_mgr import InventoryMgr
from scanner import Scanner
import json

import httplib2 as http
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

class ApiFetchProjectHosts(ApiAccess, DbAccess):
  def __init__(self):
    super(ApiFetchProjectHosts, self).__init__()
    self.inv = InventoryMgr()

  def get(self, id):
    admin_endpoint = ApiAccess.base_url.replace(":5000", ":8774")
    matches = self.inv.get_by_field(self.get_env(), "project", "name", id)
    if not len(matches):
      return []
    project = matches[0]
    req_url = admin_endpoint + "/v2/" + project["id"]  + "/os-hypervisors"
    token = self.v2_auth_pwd(project["name"])
    response = self.get_url(req_url, {"X-Auth-Token": token["id"]})
    ret = []
    for doc in response["hypervisors"]:
        # for hosts we use the name as id
        doc["os_id"] = str(doc["id"])
        doc["host_type"] = "Compute Node"
        id = doc["hypervisor_hostname"]
        doc["id"] = id[:id.index('.')]
        doc["host"] = doc["id"]
        # keep a list of projects using the host by adding "in_project-X"
        # attribute for each project X that the host is associated with
        doc["in_project-" + project["name"]] = "1"
        # fetch ip_address from nova.compute_nodes table if possible
        query = """
          SELECT host_ip AS ip_address
          FROM nova.compute_nodes
          WHERE hypervisor_hostname = %s
        """
        results = self.get_objects_list_for_id(query, "", id)
        for db_row in results:
            doc.update(db_row)
        ret.append(doc)
    return ret

