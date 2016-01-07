require 'mysql2'
require 'json'

class DbAccess
  
  @@sql_client = nil
  @@prettify = false
  
  def connect(host, port, user, pwd, db)
    @@sql_client = Mysql2::Client.new(:host => host, :port => port,
      :username => user, :password => pwd, :database => db)
  end
  
  def set_prettify(pretty)
    @@prettify = pretty
  end
  
  def get_objects_list(qry, object_type)
    results = @@sql_client.query(qry)
    rows = []
    results.each {|row| rows.push(row) }
    if (object_type.is_a?(String))
      ret = {"type" => object_type, "rows" => rows}
    else
      # object_type is a hash of parameters, just add "rows" to it
      ret = object_type
      ret["rows"] = rows
    end
    
    return ret
  end
  
  def get_objects(qry, type)
    return jsonify(get_objects_list(qry, type))
  end

  def get(id)
    # return list of available fetch types
    ret = {
      :description => "List of available fetch calls for this interface",
      :types => [
        :regions => "Regions of this environment",
	:projects => "Projects (a.k.a. Tenants) of this environment",
	:availability_zones => "Availability zones",
	:aggregates => "Host aggregates",
	:aggregate_hosts => "Hosts in aggregate X (parameter: id)",
	:az_hosts => "Host in availability_zone X (parameter: id)"
      ]
    }
    return jsonify(ret)
  end
  
  def escape(str)
    return @@sql_client.escape(str)
  end
  
  def jsonify(object)
    return @prettify != false ? JSON.pretty_generate(object) :
      JSON.generate(object)
  end
 
end
