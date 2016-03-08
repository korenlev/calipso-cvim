from db_access import DbAccess

class DbFetchAggregates(DbAccess):
  
  def get(self, id):
    return self.get_objects_list(
      """
        SELECT a.id, a.name, COUNT(*) AS descendants,
          'aggregates_root' AS parent_type
        FROM nova.aggregates a
          LEFT JOIN nova.aggregate_hosts ah ON ah.aggregate_id = a.id AND ah.deleted = 0
        WHERE a.deleted = 0
        GROUP BY a.id  
      """,
      "host aggregate")
  
