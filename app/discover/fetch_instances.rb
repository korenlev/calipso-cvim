require 'mysql2'
require_relative 'db_access'

class FetchInstances < DbAccess
  
  def get(id)
    return get_objects("SELECT uuid AS id, hostname AS name FROM nova.instances WHERE host = '#{id}'")
  end
  
end
