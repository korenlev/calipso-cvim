require_relative 'api_access'
require 'json'

class FetchProjects < ApiAccess
  
  def get_projects(region, pretty)
    @@admin_endpoint = @@base_url #.sub(":5000", ":35357")
    req_url = @@admin_endpoint + "/v2.0/tenants"
    @@logger.debug("getting projects: " + req_url)
    response_string = RestClient.get req_url,
      :"X-Auth-Token" => @@admin_token
    response_xml = Nokogiri::XML(response_string)
    response = Hash.from_xml(response_xml.to_s)
    response = response["tenants"]["tenant"]
    response.delete_if {|e| e["name"] == "services"}
    
    return jsonify(response, pretty)
  end
  
end  