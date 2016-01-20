require_relative 'db_access'

class DbFetchAZHosts < DbAccess
  
  def get(id)
    query = %Q{
      SELECT DISTINCT host, host AS id
      FROM nova.instances
      WHERE availability_zone = '#{id}'
        AND host IS NOT NULL
        AND availability_zone IS NOT NULL
        AND deleted = 0
    }
    return get_objects_list(query, "host")
  end
  
end
