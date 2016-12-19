from discover.db_access import DbAccess

class DbFetchAvailabilityZones(DbAccess):
  
  def get(self, id):
    query = """
      SELECT DISTINCT availability_zone,
        availability_zone AS id, COUNT(DISTINCT host) AS descendants
      FROM nova.instances
      WHERE availability_zone IS NOT NULL
      GROUP BY availability_zone
    """
    return self.get_objects_list(query, "availability zone")
