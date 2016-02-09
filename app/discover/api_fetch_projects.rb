require_relative 'api_access'
require 'json'

class ApiFetchProjects < ApiAccess
  
  def get(id)
    @@admin_endpoint = @@base_url.sub(":5000", ":7777")
    req_url = @@admin_endpoint + "/v2.0/tenants"
    @@logger.debug("getting projects: " + req_url)
    response_string = RestClient.get req_url,
      :"X-Auth-Token" => @@admin_token
    response = JSON.parse(response_string)
    response = response["tenants"]
    response.delete_if {|e| e["name"] == "services"}
    
    return response
  end
  
end  