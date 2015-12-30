require 'mysql2'
require 'json'
require_relative 'db_access'

class FetchInstanceDetails < DbAccess

  def get(id)
    query = %Q{
      SELECT DISTINCT i.uuid AS id, i.display_name AS name, i.host AS host,
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
    instance_id = result["id"]
    host_name = result["host"]
    ovs_id = "ovs-" + host_name
    instance = {
      "id" => instance_id,
      "group" => instance_id,
      "label" => result["name"],
      "attributes" => {
        "Project" => "XXX"
      }
    }
    nodes = [instance]
    links = []
    network_names_list = "";
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
      network_names_list += (network_names_list == "" ? "" : ",") +
        net_data["label"]
      networks.push(network_details)
      instance_to_br_edge = {
        "from" => instance_id,
        "to" => bridge_id,
        "label" => net_data["label"],
        "attributes" => {
          "IP address" => ip_addr,
          "Target device" => tap_id,
	  "Model type" => "VirtIO"
        }
      }
      links.push(instance_to_br_edge)
      ovs_edge = {
        "from" => bridge_id,
	"to" => ovs_id,
	"label" => net_data["label"],
        "attributes" => {
          "bridge outgoing port" => br_to_ovs_port_id,
          "OVS incoming port" => ovs_from_br_port_id
        }
      }
      links.push(ovs_edge)
      bridge_label = net_data["bridge"]
      bridge_node = {
        "id" => bridge_id,
	"group" => instance_id,
	"label" => "bridge: " + bridge_label + " (" + bridge_id + ")",
        "attributes" => [{"id" => bridge_id}]
      }
      nodes.push(bridge_node)
    }
    ovs_node = {
      "id" => ovs_id,
      "label" => "OVS: " + ovs_id,
      "group" => ovs_id
    }
    pnic_id = "eth0-" + host_name
    pnic_node = {
      "id" => pnic_id,
      "group" => ovs_id,
      "label" => "pNIC"
    }
    nodes.push(ovs_node)
    nodes.push(pnic_node)
    ovs_to_pnic_edge = {
      "from": ovs_id,
      "to": pnic_id,
      "label": "Networks: " + network_names_list
    }
    links.push(ovs_to_pnic_edge)
    result["networks"] = networks
    result["Entities"] = nodes
    result["Relations"] = links
    return jsonify(result)
  end

end
