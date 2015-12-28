require 'mysql2'
require_relative 'db_access'

class FetchEnvironments < DbAccess
  
  def get(parent)
    ret = {
      "type" => "environment",
      "id" => "",
      "parent" => "", 
      "rows" => [
        {"id" => 1, "text" => "Koren's RedHat RDO"},
        {"id" => 2, "text" => "DT-VMS-Canonical"},
        {"id" => 3, "text" => "WebEX-Mirantis@Cisco"},
        {"id" => 4, "text" => "DEVNET-VIRL-OS-Build288"}
      ]
    }
    return jsonify(ret)
  end
  
end
