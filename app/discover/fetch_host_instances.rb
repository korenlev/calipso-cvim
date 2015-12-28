require_relative 'fetch_instances'

class FetchHostInstances < FetchInstances
  
  def get(id)
    return get_instances("host", id)
  end
  
end
