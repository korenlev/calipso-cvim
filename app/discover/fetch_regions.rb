require 'mysql2'
require_relative 'db_access'

class FetchRegions < DbAccess
  
  def get()
    return get_objects("SELECT id FROM keystone.region")
  end
  
end
