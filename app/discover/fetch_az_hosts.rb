require 'mysql2'
require_relative 'db_access'

class FetchAZHosts < DbAccess
  
  def get(id)
    return get_objects("SELECT DISTINCT host FROM nova.instances WHERE availability_zone = '#{id}' AND host IS NOT NULL")
  end
  
end
