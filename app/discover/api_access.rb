require 'rest_client'
require 'json'
require 'logger'
require 'nokogiri'
require 'active_support/core_ext/hash/conversions'

class ApiAccess
  
  @@subject_token = nil
  @@regions = Hash.new
  
  # identitity API v2 version with admin token
  def initialize(url)
    @@base_url = url
    @@logger = Logger.new(STDOUT)
    @@logger.level = Logger::DEBUG
  end
  
  def set_v2_admin_token(token)
    @@admin_token = token
    @@admin_endpoint = @@base_url.sub(":5000", ":35357")
  end
 
  def v2_auth_pwd(user, pwd, project)
    req_url = @@base_url + "/v2.0/tokens"
    if (user != nil)
      @@user = user
    else
      user = @@user
    end
    if (pwd != nil)
      @@pwd = pwd
    else
      pwd = @@pwd
    end
    
    post_body = {
      :auth => {
        :passwordCredentials => {
          :username => user,
          :password => pwd
        }
      }
    }
    if project != nil
      post_body["tenantName"] = project
    end
    
    request_body = JSON.generate(post_body)
    @@logger.debug("request URL: " + req_url + ", request body:\n" + request_body + "\n")
    response = RestClient.post(req_url, request_body, :content_type => 'application/json')
    body = Nokogiri::XML(response.body)
    body_hash = Hash.from_xml(body.to_s)
    @@subject_token = body_hash["access"]["token"]["id"]
  end
 
  def v2_auth_token(token)
    set_v2_admin_token(token)
    req_url = @@admin_endpoint + "/v2.0/tokens"
    post_body = {:auth => {:passwordCredentials => {:token => token}}}
    request_body = JSON.generate(post_body)
    @@logger.debug("request URL: " + req_url + ", request body:\n" + request_body + "\n")
    response = RestClient.post(req_url, request_body, :content_type => 'application/json')
    body = Nokogiri::XML(response.body)
    body_hash = Hash.from_xml(body.to_s)
    @@subject_token = body_hash["access"]["token"]["id"]
  end
  
  def get(relative_url)
    return RestClient.get(@@base_url + relative_url)
  end
  
  def get_region_url(region)
    region_details = @@regions[region]
    return region_details ? region_details["url"] : nil
  end
  
  def jsonify(object, pretty)
    return pretty ? JSON.pretty_generate(object) :
      JSON.generate(object)
  end
  
end