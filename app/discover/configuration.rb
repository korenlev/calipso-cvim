require 'mongo'
require 'json'
require 'bson'

class Configuration
  
  @@client = nil
  
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
  
  def connect()
    @@client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'osdna')
  end
  
end
