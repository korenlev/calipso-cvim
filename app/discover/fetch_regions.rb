require 'mysql2'
require_relative 'db_access'

class FetchRegions < DbAccess
  
  def get_regions()
    return get_objects("SELECT id FROM keystone.region")
  end
  
end
