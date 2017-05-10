from abc import abstractmethod, ABC

from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class EventResult:
    def __init__(self,
                 result: bool, retry: bool = False, message: str = None,
                 related_object: str = None,
                 display_context: str = None):
        self.result = result
        self.retry = retry
        self.message = message
        self.related_object = related_object
        self.display_context = display_context


class EventBase(Fetcher, ABC):

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    @abstractmethod
    def handle(self, env, values) -> EventResult:
        pass
