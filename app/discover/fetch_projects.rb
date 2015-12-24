require 'mysql2'
require_relative 'db_access'

class FetchProjects < DbAccess
  
  def get_projects()
    return get_objects("SELECT id, name FROM keystone.project WHERE enabled")
  end
  
end
