require 'bson'
require_relative 'mongo_access.rb'

class Configuration < MongoAccess
  
  def get(component)
    if (@@client == nil)
      connect()
    end
    
    matches = @@client[:configuration].find(:name => component)
    if (matches.count() == 0)
      raise IndexError, "No matches for configuration component: " + component
    end
    if (matches.count() > 1)
      raise IndexError, "Found multiple matches for configuration component: " + component
    end
    matches.each {|e| return e }
  end
  
end
