require_relative 'api_access'
require 'json'

class ApiFetchRegions < ApiAccess
  
  def get(id)
    services = @@body_hash["token"]["catalog"]["service"]
    services.each {|service|
      service["name"] == "keystone" || next
      endpoints = service["endpoint"]
      endpoints.each {|e|
        e["interface"] == "admin" || next
        @@regions[e["region"]] = e
      }
    }
    return @@regions
  end
  
end  