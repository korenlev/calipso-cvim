from db_access import DbAccess

class DbFetchAZHosts(DbAccess):
  
  def get(self, id):
    query = """
      SELECT DISTINCT host, host AS id, host_ip AS ip_address
      FROM nova.instances i
        JOIN nova.compute_nodes n ON i.node = n.hypervisor_hostname
      WHERE availability_zone = %s
        AND host IS NOT NULL
        AND i.deleted = 0
    """
    results = self.get_objects_list_for_id(query, "host", id)
    for r in results:
      r["id"] = r["host"]
      r["host_type"] = "Compute node"
    return results
