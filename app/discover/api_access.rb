require 'rest_client'
require 'json'
require 'logger'
require 'nokogiri'
require 'active_support/core_ext/hash/conversions'
require_relative 'configuration'
require_relative 'fetcher'

class ApiAccess < Fetcher
  
  @@subject_token = nil
  @@initialized  = false
  @@regions = Hash.new
  
  # identitity API v2 version with admin token
  def initialize()
    @@initialized && return
    @@config = Configuration.instance.get("OpenStack")
    host = @@config["host"]
    port = @@config["port"]
    if (host == nil or port == nil)
      raise ArgumentError, "Missing definition of host or port for OpenSTack API access"
    end
    @@base_url = "http://" + host  + ":" + port
    @@logger = Logger.new(STDOUT)
    @@logger.level = Logger::DEBUG
    @@admin_token = @@config["admin_token"]
    @@admin_endpoint = @@base_url.sub(":5000", ":35357")
    
    v2_auth_pwd(nil)
    @@initialized  = true
  end
 
  def v2_auth_pwd(project)
    req_url = @@base_url + "/v2.0/tokens"
    @@user = @@config["user"]
    @@pwd = @@config["pwd"]
    
    post_body = {
      :auth => {
        :passwordCredentials => {
          :username => @@user,
          :password => @@pwd
        }
      }
    }
    if project != nil
      post_body[:auth][:tenantName] = project
    end
    
    request_body = JSON.generate(post_body)
    @@logger.debug("request URL: " + req_url + ", request body:\n" + request_body + "\n")
    response = RestClient.post(req_url, request_body, :content_type => 'application/json')
    @@body_hash = xml_to_hash(response.body)
    @@subject_token = @@body_hash["access"]["token"]["id"]
  end
 
  def v2_auth_token()
    req_url = @@admin_endpoint + "/v2.0/tokens"
    post_body = {:auth => {:passwordCredentials => {:token => @@admin_token}}}
    request_body = JSON.generate(post_body)
    @@logger.debug("request URL: " + req_url + ", request body:\n" + request_body + "\n")
    response = RestClient.post req_url, request_body, :content_type => 'application/json',
      :"X-Auth-Token" => @@admin_token
    @@body_hash = xml_to_hash(response.body)
    @@subject_token = @@body_hash["access"]["token"]["id"]
  end
  
  def get(id)
    return nil
  end
  
  def get_url(relative_url)
    return RestClient.get(@@base_url + relative_url)
  end
  
  def get_region_url(region)
    region_details = @@regions[region]
    return region_details ? region_details["url"] : nil
  end
  
  def get_catalog(pretty)
    return jsonify(@@regions, pretty)
  end
  
  def xml_to_hash(xml_text)
    xml = Nokogiri::XML(xml_text)
    hash = Hash.from_xml(xml.to_s)
    return hash
  end
  
end