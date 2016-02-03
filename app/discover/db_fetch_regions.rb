require_relative 'db_access'

class DbFetchRegions < DbAccess
  
  def get(id)
    return get_objects_list("SELECT id, id AS text, 3 as descendants FROM keystone.region", "region")
  end
  
end
