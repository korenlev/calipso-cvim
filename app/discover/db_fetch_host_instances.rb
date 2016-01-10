require_relative 'db_fetch_instances'

class DbFetchHostInstances < DbFetchInstances
  
  def get(id)
    return get_instances("host", id)
  end
  
end
