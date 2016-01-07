<<<<<<< HEAD
require_relative 'api_access'
require 'json'

class FetchProjects < ApiAccess
  
  def get_projects(region, pretty)
    req_url = @@base_url + "/v3/projects"
    @@logger.debug("getting projects: " + req_url)
    response_string = RestClient.get(req_url, :"X-Auth-Token" => @@subject_token)
    response_xml = Nokogiri::XML(response_string)
    response = Hash.from_xml(response_xml.to_s)
    response = response["projects"]["project"]
    response.delete_if {|e| e["name"] == "services"}
    return jsonify(response, pretty)
  end
  
end  
=======
require 'mysql2'
require_relative 'db_access'

class FetchProjects < DbAccess
  
  def get(id)
    query = "SELECT id, name, description FROM keystone.project WHERE enabled"
    return get_objects(query, "project")
  end
  
end
>>>>>>> origin/fetch_from_db
