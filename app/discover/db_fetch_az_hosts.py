from db_access import DbAccess

class DbFetchAZHosts(DbAccess):
  
  def get(self, id):
    query = """
      SELECT DISTINCT host, host AS id
      FROM nova.instances
      WHERE availability_zone = %s
        AND host IS NOT NULL
        AND deleted = 0
    """
    results = self.get_objects_list_for_id(query, "host", id)
    for r in results:
      r["id"] = r["host"]
      r["host_type"] = "Compute Node"
    return results
