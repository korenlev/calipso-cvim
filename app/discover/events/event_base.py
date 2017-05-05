from abc import abstractmethod, ABC
from bson import ObjectId

from discover.events.constants import DEFAULT_OBJECT_TYPE
from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class EventResult:
    def __init__(self,
                 result: bool, retry: bool = False, message: str = None,
                 related_object: str = None,
                 related_object_type: str = DEFAULT_OBJECT_TYPE,
                 display_context: str = None):
        self.result = result
        self.retry = retry
        self.message = message
        self.related_object = related_object
        self.related_object_type = related_object_type
        self.display_context = display_context


class EventBase(Fetcher, ABC):

    OBJECT_TYPE = DEFAULT_OBJECT_TYPE

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    @abstractmethod
    def handle(self, env, values) -> EventResult:
        pass

    def construct_event_result(self, result: bool, retry: bool = False,
                               related_object: str = None, display_context: str = None):
        return EventResult(result=result, retry=retry,
                           related_object=related_object,
                           related_object_type=self.OBJECT_TYPE,
                           display_context=display_context)

