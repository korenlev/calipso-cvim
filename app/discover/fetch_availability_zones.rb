require 'mysql2'
require_relative 'db_access'

class FetchAvailabilityZones < DbAccess
  
  def get(id)
    return get_objects("SELECT DISTINCT availability_zone FROM nova.instances WHERE availability_zone IS NOT NULL")
  end
  
end
