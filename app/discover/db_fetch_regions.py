from db_access import DbAccess

class DbFetchRegions(DbAccess):
  
  def get(self, id):
    query = "SELECT id, id AS text FROM keystone.region"
    return self.get_objects_list(query, "region")
