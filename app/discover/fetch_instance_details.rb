require 'mysql2'
require 'json'
require_relative 'db_access'

class FetchInstanceDetails < DbAccess

  def get(id)
    query = %Q{
      SELECT DISTINCT i.uuid AS id, i.host AS name, i.hostname AS host,
        network_info, i.availability_zone, p.name AS project
      FROM nova.instances i
        JOIN keystone.project p ON p.id = i.project_id
        JOIN nova.instance_info_caches ic ON i.uuid = ic.instance_uuid
      WHERE uuid = '#{id}'
      }
    results = get_objects_list(query, "instance")
    results = results["rows"]
    result = results[0]
    network_info_str = result["network_info"]
    result.delete("network_info")
    result["descendants"] = 0
    network_info = JSON.parse(network_info_str)
    networks = []
    network_info.each {|network|
      net_data = network["network"]
      network_details = {
        "id" => network["id"],
        "name" => net_data["label"],
        "address" => net_data["subnets"][0]["ips"][0]["address"]
      }
      networks.push(network_details)
    }
    result["networks"] = networks
    return jsonify(result)
  end

end


