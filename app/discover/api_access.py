from configuration import Configuration
from fetcher import Fetcher

import httplib2 as http
import json
import time
import calendar
import re

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
  
  host = ""
  base_url = ""
  admin_token = ""
  tokens = {}
  admin_endpoint = ""
  auth_response = None
  
  
  # identitity API v2 version with admin token
  def __init__(self):
    super(ApiAccess, self).__init__()
    if ApiAccess.initialized:
      return
    ApiAccess.config = Configuration()
    ApiAccess.api_config = ApiAccess.config.get("OpenStack")
    host = ApiAccess.api_config["host"]
    ApiAccess.host = host
    port = ApiAccess.api_config["port"]
    if (host == None or port == None):
      raise ValueError("Missing definition of host or port for OpenStack API access")
    ApiAccess.base_url = "http://" + host  + ":" + port
    ApiAccess.admin_token = ApiAccess.api_config["admin_token"]
    ApiAccess.admin_endpoint = "http://" + host  + ":" + "35357"
    
    self.v2_auth_pwd("admin")
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
    ApiAccess.auth_response = json.loads(content_string)
    try:
        token_details = ApiAccess.auth_response["access"]["token"]
    except KeyError:
        # assume authentication failed
        return None
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
  
  
  def get(self, id):
    return nil
  
  
  def get_rel_url(self, relative_url, headers):
    req_url = ApiAccess.base_url + relative_url
    return self.get_url(req_url, headers)
  
  
  def get_url(self, req_url, headers):
    method = 'GET'
    h = http.Http()
    response, content = h.request(req_url, method, "", headers)
    if int(response["status"]) != 200:
      # some error happened
      if "reason" in response:
        msg = ", reason: " + response["reason"]
      else:
        msg = ", response: " + str(response)
      print("Error: req_url:" + req_url + msg)
      return response
    content_string = content.decode('utf-8')
    ret = json.loads(content_string)
    return ret
  
  
  def get_region_url(self, region_name, service):
    if region_name not in self.regions:
      return None
    region = self.regions[region_name]
    if not service in region["endpoints"]:
      return None
    s = region["endpoints"][service]
    orig_url = s["adminURL"]
    # replace host name with the host found in config
    url = re.sub(r"^([^/]+)//[^:]+", r"\1//" + ApiAccess.host, orig_url)
    return url
  
  # like get_region_url(), but remove everything starting from the "/v2"
  def get_region_url_nover(self, region, service):
    full_url = self.get_region_url(region, service)
    url = re.sub(r":([0-9]+)/v[2-9].*", r":\1", full_url)
    return url
  
  def get_catalog(self, pretty):
    return jsonify(regions, pretty)
  
