require_relative 'api_access'
require 'json'

class FetchRegions < ApiAccess
  
  def get_catalog(pretty)
    return jsonify(@@regions, pretty)
  end
  
end  