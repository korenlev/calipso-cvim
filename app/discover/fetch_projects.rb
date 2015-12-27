require 'mysql2'
require_relative 'db_access'

class FetchProjects < DbAccess
  
  def get(id)
    return get_objects("SELECT id, name, description FROM keystone.project WHERE enabled")
  end
  
end
