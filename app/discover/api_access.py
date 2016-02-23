from configuration import Configuration
from fetcher import Fetcher

import httplib2 as http
import json
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

class ApiAccess(Fetcher):
  
  subject_token = None
  initialized  = False
  regions = {}
  config = None
  api_config = None
  
  base_url = ""
  admin_token = ""
  admin_endpoint = ""
  body_hash = None
  
  
  # identitity API v2 version with admin token
  def __init__(self):
    super(ApiAccess, self).__init__()
    if ApiAccess.initialized:
      return
    ApiAccess.config = Configuration()
    ApiAccess.api_config = ApiAccess.config.get("OpenStack")
    host = ApiAccess.api_config["host"]
    port = ApiAccess.api_config["port"]
    if (host == None or port == None):
      raise ValueError("Missing definition of host or port for OpenSTack API access")
    ApiAccess.base_url = "http://" + host  + ":" + port
    ApiAccess.admin_token = ApiAccess.api_config["admin_token"]
    ApiAccess.admin_endpoint = ApiAccess.base_url.replace(":5000", ":35357")
    
    self.v2_auth_pwd(None)
    initialized  = True
    
 
  def v2_auth(self, headers, post_body):
    req_url = ApiAccess.base_url + "/v2.0/tokens"
    request_body = json.dumps(post_body)
    method = 'POST'
    h = http.Http()
    response, content = h.request(req_url, method, request_body, headers)
    content_string = content.decode('utf-8')
    ApiAccess.body_hash = json.loads(content_string)
    subject_token = ApiAccess.body_hash["access"]["token"]["id"]
    
 
  def v2_auth_pwd(self, project):
    user = ApiAccess.api_config["user"]
    pwd = ApiAccess.api_config["pwd"]
    post_body = {
      "auth": {
        "passwordCredentials": {
          "username": user,
          "password": pwd
        }
      }
    }
    if project != None:
      post_body["auth"]["tenantName"] = project
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=UTF-8'
    }
    self.v2_auth(headers, post_body)
 
 
  def v2_auth_token(self):
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=UTF-8',
      'X-Auth-Token': admin_token
    }
    post_body = {"auth": {"passwordCredentials": {"token": admin_token}}}
    self.v2_auth(headers, post_body)
  
  
  def get(id):
    return nil
  
  
  def get_rel_url(self, relative_url, headers):
    req_url = ApiAccess.base_url + relative_url
    return self.get_url(req_url, headers)
  
  
  def get_url(self, req_url, headers):
    method = 'GET'
    h = http.Http()
    response, content = h.request(req_url, method, "", headers)
    content_string = content.decode('utf-8')
    ret = json.loads(content_string)
    return ret
  
  
  def get_region_url(self, region):
    region_details = regions[region]
    return region_details["url"] if region_details else None
  
  
  def get_catalog(self, pretty):
    return jsonify(regions, pretty)
  
