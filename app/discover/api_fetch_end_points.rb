# fetch the end points for a given project (tenant)
# return list of regions, to allow further recursive scanning

require_relative 'api_access'
require_relative 'inventory_mgr'
require_relative 'configuration'
require_relative 'util'
require 'json'

class ApiFetchEndPoints < ApiAccess
  include Util
  
  def initialize()
    @inventory = InventoryMgr.instance
  end
  
  def get(id)
    if id != "admin"
      return [] # XXX currently having problems authenticating to other tenants
    end
    v2_auth_pwd(id)
    
    environment = Configuration.instance.get_env()
    regions = []
    @@body_hash["access"]["serviceCatalog"]["service"].each {|s|
      (s["type"] != "identity") && next
      e = s["endpoint"]
      e[:environment] = environment
      e[:project] = id
      e[:type] = "endpoint"
      symbolize_keys_deep!(e)
      @inventory.set(e)
      region = nil
      region = {
        :id => e[:region],
        :environment => environment,
        :text => e[:region],
        :descendants => 3,
        :parent_id => environment,
        :parent_type => "environment"
      }
      regions.push(region)
    }
    
    return regions
  end
  
end  