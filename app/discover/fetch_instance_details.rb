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
    base_id = result["id"]
    base = {"id" => base_id, "label" => result["name"]}
    nodes = [base]
    links = []
    network_info.each {|network|
      net_data = network["network"]
      tap_id = network["devname"]
      bridge_id = tap_id.sub("tap", "qbr")
      br_to_ovs_port_id = tap_id.sub("tap", "qvb")
      ovs_from_br_port_id = tap_id.sub("tap", "qvo")
      ip_addr= net_data["subnets"][0]["ips"][0]["address"]
      network_details = {
        "id" => network["id"],
        "name" => net_data["label"],
        "address" => ip_addr
      }
      networks.push(network_details)
      base_to_br_edge = {
        "from" => base_id,
        "to" => bridge_id,
        "label" => net_data["label"],
        "attributes" => {
          "IP address" => ip_addr,
          "bridge outgoing port" => br_to_ovs_port_id,
          "OVS incoming port" => ovs_from_br_port_id
        }
      }
      links.push(base_to_br_edge)
      ovs_id = network["id"]
      ovs_edge = {"from" => bridge_id, "to" => ovs_id, "label" => net_data["label"]}
      links.push(ovs_edge)
      bridge_label = net_data["bridge"]
      bridge_node = {"id" => bridge_id, "label" => "bridge: " + bridge_label,
        "attributes" => [{"id" => bridge_id}]}
      nodes.push(bridge_node)
      ovs_node = {"id" => bridge_id, "label" => "bridge " + bridge_label + bridge_id}
      nodes.push(ovs_node)
    }
    result["networks"] = networks
    result["Entities"] = nodes
    result["Relations"] = links
    return jsonify(result)
  end

end


