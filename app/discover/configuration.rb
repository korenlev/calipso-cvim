require_relative 'mongo_access.rb'
require 'singleton'

class Configuration < MongoAccess
  include Singleton
  
  @config = nil
  
  def use_env(env_name)
    envs = @@client[:environments].find(:name => env_name)
    if envs.count() != 1
      raise ArgumentError, "set_env: could not find matching environment"
    end
    envs.each {|e| @config = e[:configuration]}
  end
  
  def check_config()
    !@config && raise(ArgumentError, "Configuration: environment not set")
  end
  
  def get(component)
    check_config()
    matches = @config.select { |c| c[:name] == component}
    if (matches.count() == 0)
      raise IndexError, "No matches for configuration component: " + component
    end
    if (matches.count() > 1)
      raise IndexError, "Found multiple matches for configuration component: " + component
    end
    matches.each {|e| return e }
  end
  
end
