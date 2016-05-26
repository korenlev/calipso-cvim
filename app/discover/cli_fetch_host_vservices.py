import re
from cli_access import CliAccess
from network_agents_list import NetworkAgentsList
from db_access import DbAccess
from inventory_mgr import InventoryMgr

class CliFetchHostVservices(CliAccess, DbAccess):

  def __init__(self):
    super(CliFetchHostVservices, self).__init__()
    # match only DHCP agent and router (L3 agent)
    self.type_re = re.compile("^q(dhcp|router)-")
    self.inv = InventoryMgr()
    self.agents_list = NetworkAgentsList()

  def get(self, host_id):
    host = self.inv.getSingle(self.get_env(), "host", host_id)
    if "Network" not in host["host_type"]:
      return []
    host_types = host["host_type"]
    services_ids = self.run_fetch_lines("ip netns", host_id)
    results = [{"local_service_id": s} for s in services_ids if self.type_re.match(s)]
    for r in results:
      self.set_details(host_id, r)
    return results

  def set_details(self, host_id, r):
    # keep the index without prefix
    id_full = r["local_service_id"]
    prefix = id_full[1:id_full.index('-')]
    id_clean = id_full[id_full.index('-')+1:]
    r["service_type"] = prefix
    name = self.get_router_name(r, id_clean) if prefix == "router" \
      else self.get_network_name(id_clean)
    r["name"] = prefix + "-" + name
    r["host"] = host_id
    r["id"] = id_full
    self.set_agent_type(r)

  def get_network_name(self, id):
    query = """
      SELECT name
      FROM neutron.networks
      WHERE id = %s
    """
    results = self.get_objects_list_for_id(query, "router", id)
    if not list(results):
      return id
    for db_row in results:
      return db_row["name"]

  def get_router_name(self, r, id):
    query = """
      SELECT *
      FROM neutron.routers
      WHERE id = %s
    """
    results = self.get_objects_list_for_id(query, "router", id)
    for db_row in results:
      r.update(db_row)
    return r["name"]

  # dynamically create sub-folder for vService by type
  def set_agent_type(self, o):
    o["master_parent_id"] = o["host"] + "-vservices"
    o["master_parent_type"] = "host_object_type"
    atype = o["service_type"]
    agent = self.agents_list.get_type(atype)
    o["parent_type"] = "vservice_object_type"
    try:
      o["parent_id"] = o["master_parent_id"] + "-" + agent["type"] + "s"
      o["parent_text"] = agent["folder_text"]
    except KeyError:
      o["parent_id"] = o["master_parent_id"] + "-" + "miscellenaous"
      o["parent_text"] = "Misc. services"
