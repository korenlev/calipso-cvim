require 'mysql2'
require_relative 'db_access'

class FetchAvailabilityZones < DbAccess
  
  def get(id)
    query = %Q{
      SELECT DISTINCT availability_zone
      FROM nova.instances
      WHERE availability_zone IS NOT NULL
    }
    return get_objects(query, "availability zone")
  end
  
end
