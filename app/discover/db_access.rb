require 'mysql2'
require 'json'

class DbAccess
  
  @@client = nil
  @@prettify = false
  
  def connect(host, port, user, pwd, db)
    @@client = Mysql2::Client.new(:host => host, :port => port,
      :username => user, :password => pwd, :database => db)
  end
  
  def set_prettify(pretty)
    @@prettify = pretty
  end
  
  def get_objects(qry)
    results = @@client.query(qry)
    rows = []
    results.each {|row| rows.push(row) }
    ret = {:rows => rows}
    return jsonify(ret)
  end

  def get()
    # return list of available fetch types
    ret = {
      :description => "List of available fetch calls for this interface",
      :types => [
        :regions => "Regions of this environment",
	:projects => "Projects (a.k.a. Tenants) of this environment"
      ]
    }
    return jsonify(ret)
  end
  
  def jsonify(object)
    return @prettify ? JSON.pretty_generate(object) : JSON.generate(object)
  end
 
end
