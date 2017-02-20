from abc import abstractmethod, ABC

from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class EventBase(Fetcher, ABC):

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    @abstractmethod
    def handle(self, env, values):
        pass
