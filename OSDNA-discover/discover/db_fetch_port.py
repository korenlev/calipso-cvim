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
        return self.get_objects_list_for_id(query, "port", id)

    def get_id(self, id=None):
        query = """SELECT id FROM neutron.ports where network_id = %s"""
        result = self.get_objects_list_for_id(query, "port", id)
        return result[0]['id'] if result != [] else None

    def get_id_by_field(self, id, search=''):
        query = """SELECT id FROM neutron.ports where network_id = %s AND """ + search
        result = self.get_objects_list_for_id(query, "port", id)
        return result[0]['id'] if result != [] else None