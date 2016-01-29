require 'mongo'

Mongo::Logger.logger.level = ::Logger::FATAL

class MongoAccess
  
  @@client = nil
  
  def connect()
    (@@client != nil) && return
    @@client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'osdna')
  end
  
end
