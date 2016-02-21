import json
from db_access import DbAccess

class DbFetchInstances(DbAccess):
  
  def get_instances(self, field, id):
    query = """
      SELECT DISTINCT i.uuid AS id, i.display_name AS name, i.host AS host,
        network_info, i.availability_zone, p.name AS project
      FROM nova.instances i
        JOIN keystone.project p ON p.id = i.project_id
        JOIN nova.instance_info_caches ic ON i.uuid = ic.instance_uuid
      WHERE %(field) = %s
        AND host IS NOT NULL
        AND availability_zone IS NOT NULL
        AND i.deleted = 0
    """ % (field)
    results = get_objects_list_for_id(query, "instance", id)
    ret = []
    # build instance details for each of the instances found
    for e in results:
      result = build_instance_details(e)
      ret.append(result)
    return ret
  
  def build_instance_details(self, result):
    network_info_str = result["network_info"]
    result.delete("network_info")
    result["descendants"] = 0
    network_info = json.loads(network_info_str)
    self.networks = []
    self.instance_id = result["id"]
    host_name = result["host"]
    self.ovs_id = "ovs-" + host_name
    instance = {
      "type": "instance",
      "id": self.instance_id,
      "group": self.instance_id,
      "label": result["name"],
      "level": 1,
      "attributes": {
        "Name": result["name"],
        "Host": host_name,
        "Availability zone": result["availability_zone"],
        "Project": result["project"]
      }
    }
    self.nodes = [instance]
    self.links = []
    self.segments = []
    for network in network_info:
      handle_single_network(network, result)
    ovs_node = {
      "type": "OVS",
      "id": self.ovs_id,
      "label": "OVS: " + self.ovs_id,
      "level": 5,
      "group": self.ovs_id,
      "attributes": {
        "ID": self.ovs_id
      }
    }
    pnic_id = "eth0-" + host_name
    pnic_node = {
      "type": "pNIC",
      "id": pnic_id,
      "group": self.ovs_id,
      "label": "pNIC: " + pnic_id,
      "level": 7,
      "attributes": {
        "ID": pnic_id
      }
    }
    self.nodes.append(ovs_node)
    self.nodes.append(pnic_node)
    network_names_list = [n["network"]["label"] for n in network_info]
    ovs_to_pnic_edge = {
      "from": self.ovs_id,
      "to": pnic_id,
      "label": "Networks: " + network_names_list.join(", "),
      "attributes": {
        "Network Type: ": "VLAN Trunk",
        "Segment ID(s): ": self.segments.join(", ")
      }
    }
    self.links.append(ovs_to_pnic_edge)
    result["networks"] = self.networks
    result["Entities"] = self.nodes
    result["Relations"] = self.links
    result["type"] = "instance"
    return result
  
  def handle_single_network(self, network, result):
    net_data = network["network"]
    tap_id = network["devname"]
    bridge_id = tap_id.sub("tap", "qbr")
    br_to_ovs_port_id = tap_id.sub("tap", "qvb")
    ovs_from_br_port_id = tap_id.sub("tap", "qvo")
    ip_addr= net_data["subnets"][0]["ips"][0]["address"]
    network_details = {
      "id": network["id"],
      "name": net_data["label"],
      "address": ip_addr
    }
    self.networks.append(network_details)
    instance_to_br_edge = {
      "from": self.instance_id,
      "to": bridge_id,
      "label": net_data["label"],
      "attributes": {
        "IP address": ip_addr,
        "Target device": tap_id,
        "Model type": "VirtIO",
        "VLAN vid": "5 (TBD)"
      }
    }
    self.links.append(instance_to_br_edge)
    segment_query = """
      SELECT segmentation_id
      FROM neutron.ml2_network_segments
      WHERE network_id = %s
    """
    segment_matches = get_objects_list_for_id(segment_query, "segment", net_data["id"])
    segment_id = segment_matches["rows"][0]
    segment_id = segment_id["segmentation_id"] if segment_id else "UNKNOWN"
    self.segments.append(segment_id)
    ovs_edge = {
      "from": bridge_id,
      "to": self.ovs_id,
      "label": net_data["label"],
      "attributes": {
        "bridge outgoing port": br_to_ovs_port_id,
        "OVS incoming port": ovs_from_br_port_id,
        "DL VLAN": segment_id
      }
    }
    self.links.append(ovs_edge)
    bridge_label = net_data["bridge"]
    bridge_node = {
      "type": "bridge",
      "id": bridge_id,
      "group": self.instance_id,
      "label": "bridge: " + bridge_label + " (" + bridge_id + ")",
      "level": 2,
      "attributes": [{"id": bridge_id}]
    }
    self.nodes.append(bridge_node)
