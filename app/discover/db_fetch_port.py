import json

from discover.db_access import DbAccess
from discover.inventory_mgr import InventoryMgr


class DbFetchPort(DbAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()
        self.env_config = self.config.get_env_config()

    def get(self, id=None):
        query = """SELECT * FROM neutron.ports where network_id = %s"""
        results = self.get_objects_list_for_id(query, "port", id)
        return results
