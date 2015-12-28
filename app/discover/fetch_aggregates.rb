require 'mysql2'
require_relative 'db_access'

class FetchAggregates < DbAccess
  
  def get(id)
    return get_objects("SELECT id, name FROM nova.aggregates WHERE deleted = 0", "host aggregate")
  end
  
end
