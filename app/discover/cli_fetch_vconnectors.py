from cli_access import CliAccess
from inventory_mgr import InventoryMgr
from singleton import Singleton


class CliFetchVconnectors(CliAccess, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, id):
        host_id = id[:id.rindex('-')]
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error("CliFetchVconnectors: host not found: " + host_id)
            return []
        if "host_type" not in host:
            self.log.error("host does not have host_type: " + host_id + \
                           ", host: " + str(host))
            return []
        return self.get_vconnectors(host)
