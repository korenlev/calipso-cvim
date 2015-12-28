require 'mysql2'
require_relative 'db_access'

class FetchRegionObjectTypes < DbAccess
  
  def get(parent)
    ret = {
      "type" => "region object type",
      "id" => "",
      "parent" => parent, 
      "rows" => [
        {"id" => "projects root", "text" => "projects"},
        {"id" => "aggregates root", "text" => "aggregates"},
        {"id" => "availability zones root", "text" => "availability zones"}
      ]
    }
    return jsonify(ret)
  end
  
end
