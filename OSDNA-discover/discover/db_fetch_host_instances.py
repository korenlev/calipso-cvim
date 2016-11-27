from db_fetch_instances import DbFetchInstances

class DbFetchHostInstances(DbFetchInstances):
  
  def get(self, id):
    return self.get_instances("host", id)
