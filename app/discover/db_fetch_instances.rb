require 'json'
require_relative 'db_access'

class DbFetchInstances < DbAccess
  
  def get_instances(field, id)
    query = %Q{
      SELECT DISTINCT i.uuid AS id, i.display_name AS name, i.host AS host,
        network_info, i.availability_zone, p.name AS project
      FROM nova.instances i
        JOIN keystone.project p ON p.id = i.project_id
        JOIN nova.instance_info_caches ic ON i.uuid = ic.instance_uuid
      WHERE #{field} = '#{id}'
        AND host IS NOT NULL
        AND availability_zone IS NOT NULL
        AND i.deleted = 0
    }
    results = get_objects_list(query, "instance")
    ret = []
    # build instance details for each of the instances found
    results["rows"].each {|e|
      result = build_instance_details(e)
      ret.push(result)
    }
    return ret
  end
  
  def build_instance_details(result)
    network_info_str = result["network_info"]
    result.delete("network_info")
    result["descendants"] = 0
    network_info = JSON.parse(network_info_str)
    @networks = []
    @instance_id = result["id"]
    host_name = result["host"]
    @ovs_id = "ovs-" + host_name
    instance = {
      "type" => "instance",
      "id" => @instance_id,
      "group" => @instance_id,
      "label" => result["name"],
      "level" => 1,
      "attributes" => {
        "Name" => result["name"],
	"Host" => host_name,
	"Availability zone" => result["availability_zone"],
        "Project" => result["project"]
      }
    }
    @nodes = [instance]
    @links = []
    @segments = []
    network_info.each {|network|
      handle_single_network(network, result)
    }
    ovs_node = {
      "type" => "OVS",
      "id" => @ovs_id,
      "label" => "OVS: " + @ovs_id,
      "level" => 5,
      "group" => @ovs_id,
      "attributes" => [
        "ID" => @ovs_id
      ]
    }
    pnic_id = "eth0-" + host_name
    pnic_node = {
      "type" => "pNIC",
      "id" => pnic_id,
      "group" => @ovs_id,
      "label" => "pNIC: " + pnic_id,
      "level" => 7,
      "attributes" => [
        "ID" => pnic_id
      ]
    }
    @nodes.push(ovs_node)
    @nodes.push(pnic_node)
    network_names_list = network_info.map{|n| n["network"]["label"]}
    ovs_to_pnic_edge = {
      "from" => @ovs_id,
      "to" => pnic_id,
      "label" => "Networks: " + network_names_list.join(", "),
      "attributes" => [
        "Network Type: " => "VLAN Trunk",
        "Segment ID(s): " => @segments.join(", ")
      ]
    }
    @links.push(ovs_to_pnic_edge)
    result["networks"] = @networks
    result["Entities"] = @nodes
    result["Relations"] = @links
    result["type"] = "instance"
    return result
  end
  
  def handle_single_network(network, result)
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
    @networks.push(network_details)
    instance_to_br_edge = {
      "from" => @instance_id,
      "to" => bridge_id,
      "label" => net_data["label"],
      "attributes" => {
        "IP address" => ip_addr,
        "Target device" => tap_id,
        "Model type" => "VirtIO",
        "VLAN vid" => "5 (TBD)"
      }
    }
    @links.push(instance_to_br_edge)
    segment_query = %Q{
      SELECT segmentation_id
      FROM neutron.ml2_network_segments
      WHERE network_id = '#{net_data["id"]}'
    }
    segment_matches = get_objects_list(segment_query, "segment")
    segment_id = segment_matches["rows"][0] ?
      segment_matches["rows"][0]["segmentation_id"] :
      "UNKNOWN"
    @segments.push(segment_id)
    ovs_edge = {
      "from" => bridge_id,
      "to" => @ovs_id,
      "label" => net_data["label"],
      "attributes" => {
        "bridge outgoing port" => br_to_ovs_port_id,
        "OVS incoming port" => ovs_from_br_port_id,
        "DL VLAN" => segment_id
      }
    }
    @links.push(ovs_edge)
    bridge_label = net_data["bridge"]
    bridge_node = {
      "type" => "bridge",
      "id" => bridge_id,
      "group" => @instance_id,
      "label" => "bridge: " + bridge_label + " (" + bridge_id + ")",
      "level" => 2,
      "attributes" => [{"id" => bridge_id}]
    }
    @nodes.push(bridge_node)
  end

end
