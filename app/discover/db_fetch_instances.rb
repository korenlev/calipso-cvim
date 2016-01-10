require_relative 'db_access'

class DbFetchInstances < DbAccess
  
  def get_instances(field, id)
    query = %Q{
      SELECT uuid AS id, display_name AS name, 1 AS descendants
      FROM nova.instances
      WHERE #{field} = '#{id}' AND deleted = 0
    }
    return get_objects(query, "instance")
  end

  def get(id)
    return jsonify("error" => "FetchInstances: use get_instances() instead of get()")
  end
  private :get
  
end
