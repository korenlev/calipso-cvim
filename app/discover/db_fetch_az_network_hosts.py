from db_access import DbAccess
import json

class DbFetchAZNetworkHosts(DbAccess):

  def get(self, id):
    query = """
      SELECT DISTINCT host, host AS id, configurations
      FROM neutron.agents
      WHERE agent_type = 'Metadata agent'
    """
    results = self.get_objects_list(query, "host")
    for r in results:
      self.set_host_details(r)
    return results

  def set_host_details(self, r):
    config = json.loads(r["configurations"])
    r["ip_address"] = config["nova_metadata_ip"]
    r["host_type"] = "Network node"
