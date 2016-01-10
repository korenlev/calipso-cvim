require 'mysql2'
require_relative 'db_access'

class DbFetchAggregates < DbAccess
  
  def get(id)
    return get_objects(%Q{
        SELECT a.id, a.name, COUNT(*) AS descendants
        FROM nova.aggregates a
          LEFT JOIN nova.aggregate_hosts ah ON ah.aggregate_id = a.id AND ah.deleted = 0
        WHERE a.deleted = 0
        GROUP BY a.id  
      },
      "host aggregate")
  end
  
end
