require_relative 'db_access'

class DbFetchEnvironments < DbAccess
  
  def get(parent)
    ret = {
      "type" => "environment",
      "id" => "",
      "rows" => [
        {"id" => 1, "text" => "Koren's RedHat RDO", "descendants" => 2},
        {"id" => 2, "text" => "DT-VMS-Canonical", "descendants" => 2},
        {"id" => 3, "text" => "WebEX-Mirantis@Cisco", "descendants" => 2},
        {"id" => 4, "text" => "DEVNET-VIRL-OS-Build288", "descendants" => 2}
      ]
    }
    return jsonify(ret)
  end
  
end
