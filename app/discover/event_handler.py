from typing import List, Tuple

from discover.events.event_base import EventBase, EventResult
from utils.inventory_mgr import InventoryMgr
from utils.logger import Logger
from utils.util import ClassResolver


class EventHandler(Logger):

    def __init__(self, env: str, inventory_collection: str,
                 event_handlers: List[Tuple[str, str]],
                 handlers_package: str = "discover.events"):
        super().__init__()
        self.inv = InventoryMgr()
        self.inv.set_collections(inventory_collection)
        self.env = env
        self.handlers = {}
        self._discover_handlers(handlers_package, event_handlers)

    # Extract (event_name, handler_class_name) pairs
    # from custom data structure
    @staticmethod
    def _extract_handlers(event_handlers) -> iter:
        return iter(event_handlers)

    def _discover_handlers(self, handlers_package, event_handlers):
        if not event_handlers:
            raise TypeError("Event handlers list is empty")

        for event_name, handler_name in self._extract_handlers(event_handlers):
            handler = ClassResolver.get_instance_of_class(handler_name, handlers_package)
            if not issubclass(handler.__class__, EventBase):
                raise TypeError("Event handler '{}' is not a subclass of EventBase"
                                .format(handler_name))
            if event_name in self.handlers:
                self.log.warn("A handler is already registered for this event type")
            self.handlers[event_name] = handler

    def handle(self, event_name: str, notification: dict) -> EventResult:
        if event_name not in self.handlers:
            raise ValueError("No handler is able to process event of type '{}'"
                             .format(event_name))
        return self.handlers[event_name].handle(self.env, notification)

