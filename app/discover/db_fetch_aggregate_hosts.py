import bson

from discover.db_access import DbAccess
from utils.inventory_mgr import InventoryMgr


class DbFetchAggregateHosts(DbAccess):
    def get(self, id):
        query = """
      SELECT CONCAT('aggregate-', a.name, '-', host) AS id, host AS name
      FROM nova.aggregate_hosts ah
        JOIN nova.aggregates a ON a.id = ah.aggregate_id
      WHERE ah.deleted = 0 AND aggregate_id = %s
    """
        hosts = self.get_objects_list_for_id(query, "host", id)
        if hosts:
            inv = InventoryMgr()
            for host_rec in hosts:
                host = inv.get_by_id(self.get_env(), host_rec['name'])
                host_rec['ref_id'] = bson.ObjectId(host['_id'])
        return hosts
