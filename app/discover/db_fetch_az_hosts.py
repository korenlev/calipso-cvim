from db_access import DbAccess

class DbFetchAZHosts(DbAccess):
  
  def get(self, id):
    query = """
      SELECT DISTINCT host, host AS id
      FROM nova.instances
      WHERE availability_zone = %s
        AND host IS NOT NULL
        AND availability_zone IS NOT NULL
        AND deleted = 0
    """
    return self.get_objects_list_for_id(query, "host", id)
