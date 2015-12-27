require 'mysql2'
require_relative 'db_access'

class FetchAggregateHosts < DbAccess
  
  def get(id)
    return get_objects(@@sql_client.escape(%Q{SELECT id, host AS name FROM nova.aggregate_hosts WHERE deleted = 0 AND aggregate_id = #{id}}))
  end
  
end
