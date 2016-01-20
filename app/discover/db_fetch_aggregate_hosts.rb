require_relative 'db_access'

class DbFetchAggregateHosts < DbAccess
  
  def get(id)
    query = %Q{
      SELECT h.host AS id, h.host AS name, COUNT(*) AS descendants
      FROM nova.aggregate_hosts h
        LEFT JOIN nova.instances i ON h.host = i.hostname
      WHERE h.deleted = 0 AND aggregate_id = '#{id}'
      GROUP BY h.id, h.host
    }
    return get_objects_list(query, "host")
  end
  
end
