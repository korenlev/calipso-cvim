from db_access import DbAccess

class DbFetchAggregates(DbAccess):
  
  def get(self, id):
    return self.get_objects_list(
      """
        SELECT id, name
        FROM nova.aggregates
        WHERE deleted = 0
      """,
      "host aggregate")
  
