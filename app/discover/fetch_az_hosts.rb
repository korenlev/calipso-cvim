require 'mysql2'
require_relative 'db_access'

class FetchAZHosts < DbAccess
  
  def get(id)
    query = %Q{
      SELECT DISTINCT host
      FROM nova.instances
      WHERE availability_zone = '#{id}' AND host IS NOT NULL
    }
    return get_objects(query, "host")
  end
  
end
