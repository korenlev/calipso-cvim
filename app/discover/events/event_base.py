from abc import abstractmethod, ABC
from bson import ObjectId

from discover.events.constants import DEFAULT_OBJECT_TYPE
from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class EventResult:
    def __init__(self,
                 result: bool, retry: bool = False, message: str = None,
                 object_id: str = None, object_type: str = DEFAULT_OBJECT_TYPE,
                 document_id: ObjectId = None):
        self.result = result
        self.retry = retry
        self.message = message
        self.object_id = object_id
        self.object_type = object_type
        self.document_id = document_id


class EventBase(Fetcher, ABC):

    OBJECT_TYPE = DEFAULT_OBJECT_TYPE

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    @abstractmethod
    def handle(self, env, values) -> EventResult:
        pass

    def construct_event_result(self, result: bool, retry: bool = False,
                               object_id: str = None, document_id: str = None):
        document_id = ObjectId(document_id) if ObjectId.is_valid(document_id) else None
        return EventResult(result=result, retry=retry,
                           object_id=object_id, object_type=self.OBJECT_TYPE,
                           document_id=document_id)

