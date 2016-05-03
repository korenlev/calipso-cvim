from db_access import DbAccess

class DbFetchAggregateHosts(DbAccess):
  
  def get(self, id):
    query = """
      SELECT host AS id, host AS name
      FROM nova.aggregate_hosts
      WHERE deleted = 0 AND aggregate_id = %s
    """
    return self.get_objects_list_for_id(query, "host", id)
