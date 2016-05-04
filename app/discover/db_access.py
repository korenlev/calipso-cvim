import mysql.connector
from util import Util
from configuration import Configuration
from fetcher import Fetcher

class DbAccess(Fetcher, Util):
  
  conn = None
  
  def __init__(self):
    super().__init__()
    self.config = Configuration()
    self.conf = self.config.get("mysql")
    self.connect_to_db()


  def db_connect(self, _host, _port, _user, _password, _database):
    if DbAccess.conn:
      return
    DbAccess.conn = mysql.connector.connect(host=_host, port=_port, \
      user=_user, password=_password, database=_database)
    if not DbAccess.conn:
      raise EnvironmentError("failed to connect to MySQL DB")
  
  
  def connect_to_db(self):
    if DbAccess.conn:
      return
    cnf = self.conf
    self.db_connect(cnf["host"], cnf["port"], cnf["user"], cnf["password"], cnf["schema"])
    
  
  def get_objects_list_for_id(self, query, object_type, id):
    self.connect_to_db()
    
    cursor = DbAccess.conn.cursor(dictionary=True)
    if id:
      cursor.execute(query, [str(id)])
    else:
      cursor.execute(query)
      
    rows = []
    for row in cursor:
      rows.append(row)
    return rows
    
    if isinstance(object_type, String):
      ret = {"type": object_type, "rows": rows}
    else:
      # object_type is a hash of parameters, just add "rows" to it
      ret = object_type
      ret["rows"] = rows
    
    return ret

  def get_objects_list(self, query, object_type):
    return self.get_objects_list_for_id(query, object_type, None)
  
  def get_objects(self, qry, type, id):
    return self.jsonify(self.get_objects_list(qry, type))


  def get(self, id):
    # return list of available fetch types
    ret = {
      "description": "List of available fetch calls for this interface",
      "types": {
        "regions": "Regions of this environment",
        "projects": "Projects (tenants) of this environment",
        "availability_zones": "Availability zones",
        "aggregates": "Host aggregates",
        "aggregate_hosts": "Hosts in aggregate X (parameter: id)",
        "az_hosts": "Host in availability_zone X (parameter: id)"
      }
    }
    return jsonify(ret)
