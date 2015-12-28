require 'mysql2'
require_relative 'db_access'

class FetchAggregateHosts < DbAccess
  
  def get(id)
    query = %Q{SELECT id, host AS name FROM nova.aggregate_hosts WHERE deleted = 0 AND aggregate_id = #{id}}
    return get_objects(query, "host")
  end
  
end
