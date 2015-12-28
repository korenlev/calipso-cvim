require 'mysql2'
require_relative 'db_access'

class FetchRegions < DbAccess
  
  def get(id)
    return get_objects("SELECT id FROM keystone.region", "region")
  end
  
end
