from discover.cli_access import CliAccess
from discover.inventory_mgr import InventoryMgr


class CliFetchOtepsLxb(CliAccess):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, parent_id):
        vconnector = self.inv.get_by_id(self.get_env(), parent_id)
        if not vconnector:
            return []
        configurations = vconnector['configurations']
        tunneling_ip = configurations['tunneling_ip']
        tunnel_types_used = configurations['tunnel_types']
        if not tunnel_types_used:
            return []
        tunnel_type = tunnel_types_used[0]
        if not tunnel_type:
            return []
        ret = [i for i in vconnector['interfaces'].values()
               if i['name'].startswith(tunnel_type + '-')]
        for doc in ret:
            doc['ip_address'] = tunneling_ip
            doc['host'] = vconnector['host']
            doc['tunnel_type'] = tunnel_type
            doc['id'] = vconnector['id'] + '-otep-' + doc['name']
        return ret
