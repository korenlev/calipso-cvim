from configuration import Configuration
from fetcher import Fetcher

import httplib2 as http
import json
import time
import calendar

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
  tokens = {}
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
    
  def parse_time(self, time_str):
    try:
        time_struct = time.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        try:
          time_struct = time.strptime(time_str,
            "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
          return None
    return time_struct

  # try to use existing token, if it did not expire
  def get_existing_token(self, id):
    try:
        token_details = ApiAccess.tokens[id]
    except KeyError:
      return None
    token_expiry = token_details["expires"]
    token_expiry_time_struct = self.parse_time(token_expiry)
    if not token_expiry_time_struct:
      return None
    token_expiry_time = token_details["token_expiry_time"]
    now = time.time()
    if now > token_expiry_time:
      # token has expired
      ApiAccess.tokens.pop(id)
      return None
    return token_details

  def v2_auth(self, id, headers, post_body):
    subject_token = self.get_existing_token(id)
    if subject_token:
      return subject_token
    req_url = ApiAccess.base_url + "/v2.0/tokens"
    request_body = json.dumps(post_body)
    method = 'POST'
    h = http.Http()
    response, content = h.request(req_url, method, request_body, headers)
    content_string = content.decode('utf-8')
    ApiAccess.body_hash = json.loads(content_string)
    token_details = ApiAccess.body_hash["access"]["token"]
    token_expiry = token_details["expires"]
    token_expiry_time_struct = self.parse_time(token_expiry)
    if not token_expiry_time_struct:
      return None
    token_expiry_time = calendar.timegm(token_expiry_time_struct)
    token_details["token_expiry_time"] = token_expiry_time
    ApiAccess.tokens[id] = token_details
    return token_details
 
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
    id = ""
    if project != None:
      post_body["auth"]["tenantName"] = project
      id = project
    else:
      id = ""
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=UTF-8'
    }
    return self.v2_auth(id, headers, post_body)
 
 
  def v2_auth_token(self):
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json; charset=UTF-8',
      'X-Auth-Token': admin_token
    }
    post_body = {"auth": {"passwordCredentials": {"token": admin_token}}}
    return self.v2_auth("admin_token", headers, post_body)
  
  
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
  
