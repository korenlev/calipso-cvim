require 'mysql2'
require_relative 'fetch_instances'

class FetchProjectInstances < FetchInstances
  
  def get(id)
    return get_instances("project_id", id)
  end
  
end
