from db_access import DbAccess

class DbFetchAggregateHosts(DbAccess):
  
  def get(self, id):
    query = """
      SELECT h.host AS id, h.host AS name, COUNT(*) AS descendants
      FROM nova.aggregate_hosts h
        LEFT JOIN nova.instances i ON h.host = i.hostname
      WHERE h.deleted = 0 AND aggregate_id = %s
      GROUP BY h.id, h.host
    """
    return self.get_objects_list_for_id(query, "host", id)
