from api_access import ApiAccess
from db_access import DbAccess
from db_fetch_instances import DbFetchInstances
from inventory_mgr import InventoryMgr
from scanner import Scanner
from singleton import Singleton

import json

import httplib2 as http
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
    
class ApiFetchHostInstances(ApiAccess, DbAccess, metaclass=Singleton):

  def __init__(self):
    super(ApiFetchHostInstances, self).__init__()
    self.inv = InventoryMgr()
    self.endpoint = ApiAccess.base_url.replace(":5000", ":8774")
    self.projects = None
    self.db_fetcher = DbFetchInstances()

  def get_projects(self):
    if not self.projects:
        projects_list = self.inv.get(self.get_env(), "project", None)
        self.projects = [p["name"] for p in projects_list]
  
  def get(self, id):
    self.get_projects()
    host_name = id.replace("-instances", "")
    host = self.inv.getSingle(self.get_env(), "host", host_name)
    if host["host_type"] != "Compute node":
      return []
    instances_found = []
    for project in self.projects:
      instances_found.extend(self.get_instances_for_project(host_name, project))
    return instances_found

  def get_instances_for_project(self, host_name, project):
    token = self.v2_auth_pwd(project)
    if not token:
        return []
    tenant_id = token["tenant"]["id"]
    req_url = self.endpoint + "/v2/" + tenant_id + \
      "/os-hypervisors/" + host_name + "/servers"
    response = self.get_url(req_url, {"X-Auth-Token": token["id"]})
    ret = []
    if not "hypervisors" in response:
      return []
    if not "servers" in response["hypervisors"][0]:
      return []
    for doc in response["hypervisors"][0]["servers"]:
        doc["id"] = doc["uuid"]
        doc["host"] = host_name
        doc["in_project-" + project] = "1"
        doc["local_name"] = doc.pop("name")
        db_matches = self.db_fetcher.get_instance(doc["uuid"])
        if len(db_matches):
          doc.update(db_matches[0])
        ret.append(doc)
    return ret

