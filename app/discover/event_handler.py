from discover.events.event_base import EventResult
from discover.events.event_instance_add import EventInstanceAdd
from discover.events.event_instance_delete import EventInstanceDelete
from discover.events.event_instance_update import EventInstanceUpdate
from discover.events.event_interface_add import EventInterfaceAdd
from discover.events.event_interface_delete import EventInterfaceDelete
from discover.events.event_network_add import EventNetworkAdd
from discover.events.event_network_delete import EventNetworkDelete
from discover.events.event_network_update import EventNetworkUpdate
from discover.events.event_port_add import EventPortAdd
from discover.events.event_port_delete import EventPortDelete
from discover.events.event_port_update import EventPortUpdate
from discover.events.event_router_add import EventRouterAdd
from discover.events.event_router_delete import EventRouterDelete
from discover.events.event_router_update import EventRouterUpdate
from discover.events.event_subnet_add import EventSubnetAdd
from discover.events.event_subnet_delete import EventSubnetDelete
from discover.events.event_subnet_update import EventSubnetUpdate
from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class EventHandler(Fetcher):
    def __init__(self, env, inventory_collection):
        super().__init__()
        self.inv = InventoryMgr()
        self.inv.set_collections(inventory_collection)
        self.env = env

    def instance_add(self, notification) -> EventResult:
        self.log.info("instance_add")
        handler = EventInstanceAdd()
        return handler.handle(self.env, notification)

    def instance_update(self, notification) -> EventResult:
        self.log.info("instance_update")
        handler = EventInstanceUpdate()
        return handler.handle(self.env, notification)

    def instance_delete(self, notification) -> EventResult:
        self.log.info("instance_delete")
        handler = EventInstanceDelete()
        return handler.handle(self.env, notification)

    def instance_down(self, notification) -> EventResult:
        pass

    def instance_up(self, notification) -> EventResult:
        pass

    def region_add(self, notification) -> EventResult:
        pass

    def region_update(self, notification) -> EventResult:
        pass

    def region_delete(self, notification) -> EventResult:
        pass

    def network_create(self, notification) -> EventResult:
        self.log.info("network_add")
        handler = EventNetworkAdd()
        return handler.handle(self.env, notification)

    def network_update(self, notification) -> EventResult:
        self.log.info("network_update")
        handler = EventNetworkUpdate()
        return handler.handle(self.env, notification)

    def network_delete(self, notification) -> EventResult:
        self.log.info("network_delete")
        handler = EventNetworkDelete()
        return handler.handle(self.env, notification)

    def subnet_create(self, notification) -> EventResult:
        self.log.info("subnet_add")
        handler = EventSubnetAdd()
        return handler.handle(self.env, notification)

    def subnet_update(self, notification) -> EventResult:
        self.log.info("subnet_update")
        handler = EventSubnetUpdate()
        return handler.handle(self.env, notification)

    def subnet_delete(self, notification) -> EventResult:
        self.log.info("subnet_delete")
        handler = EventSubnetDelete()
        return handler.handle(self.env, notification)

    def port_create(self, notification) -> EventResult:
        self.log.info("port_add")
        handler = EventPortAdd()
        return handler.handle(self.env, notification)

    def port_update(self, notification) -> EventResult:
        self.log.info("port_update")
        handler = EventPortUpdate()
        return handler.handle(self.env, notification)

    def port_delete(self, notification) -> EventResult:
        self.log.info("port_delete")
        handler = EventPortDelete()
        return handler.handle(self.env, notification)

    def router_create(self, notification) -> EventResult:
        self.log.info("router_add")
        handler = EventRouterAdd()
        return handler.handle(self.env, notification)

    def router_update(self, notification) -> EventResult:
        self.log.info("router_update")
        handler = EventRouterUpdate()
        return handler.handle(self.env, notification)

    def router_delete(self, notification) -> EventResult:
        self.log.info("router_delete")
        handler = EventRouterDelete()
        return handler.handle(self.env, notification)

    def router_interface_create(self, notification) -> EventResult:
        self.log.info("router_interface_add")
        handler = EventInterfaceAdd()
        return handler.handle(self.env, notification)

    def router_interface_delete(self, notification) -> EventResult:
        self.log.info("router_interface_delete")
        handler = EventInterfaceDelete()
        return handler.handle(self.env, notification)
