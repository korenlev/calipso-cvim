require 'mysql2'
require_relative 'db_fetch_instances'

class DbFetchProjectInstances < DbFetchInstances
  
  def get(id)
    return get_instances("project_id", id)
  end
  
end
