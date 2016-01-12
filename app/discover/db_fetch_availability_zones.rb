require_relative 'db_access'

class DbFetchAvailabilityZones < DbAccess
  
  def get(id)
    query = %Q{
      SELECT DISTINCT availability_zone, COUNT(DISTINCT host) AS descendants
      FROM nova.instances
      WHERE availability_zone IS NOT NULL
      GROUP BY availability_zone
    }
    return get_objects(query, "availability zone")
  end
  
end
