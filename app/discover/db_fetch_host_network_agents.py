import json

from discover.db_access import DbAccess
from discover.inventory_mgr import InventoryMgr


class DbFetchHostNetworkAgents(DbAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.env_config = self.config.get_env_config()

    def get(self, id):
        query = """
      SELECT * FROM neutron.agents
      WHERE host = %s
    """
        host_id = id[:-1 * len("-network_agents")]
        host = self.inv.get_single(self.get_env(), "host", host_id)
        results = self.get_objects_list_for_id(query, "network_agent", host_id)
        mechanism_drivers = self.env_config['mechanism_drivers']
        id_prefix = mechanism_drivers[0] if mechanism_drivers else 'network_agent'
        for o in results:
            o["configurations"] = json.loads(o["configurations"])
            o["name"] = o["binary"]
            o['id'] = id_prefix + '-' + o['id']
        return results
