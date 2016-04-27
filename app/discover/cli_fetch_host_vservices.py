import re
from cli_access import CliAccess
from network_agents_list import NetworkAgentsList
from db_access import DbAccess

class CliFetchHostVservices(CliAccess, DbAccess):

  def __init__(self):
    super(CliFetchHostVservices, self).__init__()
    # match only DHCP agent and router (L3 agent)
    self.type_re = re.compile("^q(dhcp|router)-")

  def get(self, id):
    services_ids = self.run_fetch_lines("source openrc; ip netns")
    results = [{"id": s} for s in services_ids if self.type_re.match(s)]
    for r in results:
      self.set_details(r)
    return results

  def set_details(self, r):
    # keep the index without prefix
    id_full = r["id"]
    prefix = id_full[1:id_full.index('-')]
    id_clean = id_full[id_full.index('-')+1:]
    r["id"] = id_clean
    r["service_type"] = prefix
    if prefix == "router":
      self.set_router_name(r)

  def set_router_name(self, r):
    query = """
      SELECT *
      FROM neutron.routers
      WHERE id = %s
    """
    results = self.get_objects_list_for_id(query, "router", r["id"])
    for db_row in results:
      r.update(db_row)
