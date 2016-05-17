from db_access import DbAccess
from cli_access import CliAccess
from singleton import Singleton
from inventory_mgr import InventoryMgr
import json
import re

class DbFetchVedges(DbAccess, CliAccess, metaclass=Singleton):

  def __init__(self):
    super().__init__()
    self.inv = InventoryMgr()
    self.port_re = re.compile("^\s*port (\d+): ([^(]+)( \(internal\))?$")

  def get(self, id):
    host_id = id[:id.rindex('-')]
    results = self.get_objects_list_for_id(
      """
        SELECT *
        FROM neutron.agents
        WHERE host = %s AND agent_type = 'Open vSwitch agent'
      """,
      "vedge", host_id)
    ports = self.fetch_ports(host_id)
    for doc in results:
      doc["name"] = doc["host"] + "-OVS"
      doc["configurations"] = json.loads(doc["configurations"])
      doc["ports"] = ports
    return results

  def fetch_ports(self, host):
    lines = self.run_fetch_lines("ovs-dpctl show", host)
    ports = []
    for l in lines:
      port_matches = self.port_re.match(l)
      if not port_matches:
        continue
      port = {}
      id = port_matches.group(1)
      name = port_matches.group(2)
      is_internal = port_matches.group(3) == " (internal)"
      port["internal"] = is_internal
      port["id"] = id
      port["name"] = name
      ports.append(port)
    return ports
