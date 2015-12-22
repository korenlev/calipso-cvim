require 'rest_client'
require 'json'
require 'logger'
require 'nokogiri'
require 'active_support/core_ext/hash/conversions'

class ApiAccess
  
  @@subject_token = nil
  @@regions = Hash.new
  
  # identitity API v2 version with admin token
  def initialize(url, admin_token)
    @@base_url = url
    @@logger = Logger.new(STDOUT)
    @@logger.level = Logger::INFO
    
    @@subject_token ||= admin_token
  end
  
  def set_v2_admin_token(token)
    @@admin_token = token
  end
  
  # identitity API v3 version with user+password
  def initialize(url, user, password)
    @@base_url = url
    @@logger = Logger.new(STDOUT)
    @@logger.level = Logger::INFO
    
    if (@@subject_token == nil)
      auth(user, password)
    end
  end
  
  def auth(user, password)
    req_url = @@base_url + "/v3/auth/tokens"
    post_body = {
      :auth => {
        :identity => {
          :methods => ["password"],
          :password => {
              :user => {
                  :name => "admin",
                  :password => "admin",
                  :domain => {:name => "Default"}
              }
          }
        }
      }
    }
    request_body = JSON.generate(post_body)
    @@logger.debug("request URL: " + req_url + ", request body:\n" + request_body + "\n")
    response = RestClient.post(req_url, request_body, :content_type => 'application/json')
    @@subject_token = response.headers[:x_subject_token]
    body = Nokogiri::XML(response.body)
    body_hash = Hash.from_xml(body.to_s)
    @@logger.debug "\nauth: got response: " +
      "code=" + response.code.to_s + ", " +
      "subject_token: " + @@subject_token + ", " +
      "headers" + response.headers.to_s +
      ",\n body: \n" + body_hash.to_s + "\n"
    services = body_hash["token"]["catalog"]["service"]
    services.each {|service|
      service["name"] == "keystone" || next
      endpoints = service["endpoint"]
      endpoints.each {|e|
        e["interface"] == "admin" || next
        @@regions[e["region"]] = e
      }
    }
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