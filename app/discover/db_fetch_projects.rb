require 'mysql2'
require_relative 'db_access'

class DbFetchProjects < DbAccess
  
  def get(id)
    query = "SELECT id, name, description FROM keystone.project WHERE enabled"
    return get_objects(query, "project")
  end
  
end
