import json
from db_access import DbAccess

class DbFetchInstances(DbAccess):
  
  def get_instance_data(self, instances):
    instances_hash = {}
    for doc in instances:
      instances_hash[doc["id"]] = doc

    query = """
      SELECT DISTINCT i.uuid AS id, i.display_name AS name,
        i.host AS host, host_ip AS ip_address,
        network_info, project_id,
        IF(p.name IS NULL, "Unknown", p.name) AS project
      FROM nova.instances i
        LEFT JOIN keystone.project p ON p.id = i.project_id
        JOIN nova.instance_info_caches ic ON i.uuid = ic.instance_uuid
        JOIN nova.compute_nodes cn ON i.node = cn.hypervisor_hostname
      WHERE i.deleted = 0
    """
    results = self.get_objects_list(query, "instance")
    for result in results:
      id = result["id"]
      if not id in instances_hash:
        continue
      self.build_instance_details(result)
      doc = instances_hash[id]
      doc.update(result)
  
  def build_instance_details(self, result):
    network_info_str = result.pop("network_info", None)
    result["network_info"] = json.loads(network_info_str)

    # add network as an array to allow constraint checking when building clique
    networks = []
    for net in result["network_info"]:
      if "network" not in net or "id" not in net["network"]:
        continue
      networks.append(net["network"]["id"])
    result["network"] = networks

    result["type"] = "instance"
    result["parent_type"] = "instances_folder";
    result["parent_id"] = result["host"] + "-instances";
    result["in_project-" + result.pop("project", None)] = "1"
  
