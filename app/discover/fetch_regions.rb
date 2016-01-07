<<<<<<< HEAD
require_relative 'api_access'
require 'json'

class FetchRegions < ApiAccess
  
  def get_catalog(pretty)
    return jsonify(@@regions, pretty)
  end
  
end  
=======
require 'mysql2'
require_relative 'db_access'

class FetchRegions < DbAccess
  
  def get(id)
    return get_objects("SELECT id, id AS text, 3 as descendants FROM keystone.region", "region")
  end
  
end
>>>>>>> origin/fetch_from_db
