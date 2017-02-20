from abc import abstractmethod, ABC, ABCMeta

from discover.cli_access import CliAccess
from utils.inventory_mgr import InventoryMgr
from utils.singleton import Singleton


class ABCSingleton(ABCMeta, Singleton):
    pass


class CliFetchVconnectors(CliAccess, metaclass=ABCSingleton):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    @abstractmethod
    def get_vconnectors(self, host):
        raise NotImplementedError("Subclass must override get_vconnectors()")

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
