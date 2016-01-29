require_relative 'api_access'
require 'json'

class ApiFetchRegions < ApiAccess
  
  def fetch_v2(args)
    #code
    services = body_hash["token"]["catalog"]["service"]
    services.each {|service|
      service["name"] == "keystone" || next
      endpoints = service["endpoint"]
      endpoints.each {|e|
        e["interface"] == "admin" || next
        @@regions[e["region"]] = e
      }
    }
  end
  
  def get_catalog(pretty)
    return jsonify(@@regions, pretty)
  end
  
end  