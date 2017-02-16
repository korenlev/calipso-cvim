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
        self.inv.set_inventory_collection(inventory_collection)
        self.env = env

    def instance_add(self, notification):
        self.log.info("instance_add")
        handler = EventInstanceAdd()
        handler.handle(self.env, notification)

    def instance_delete(self, notification):
        self.log.info("instance_delete")
        handler = EventInstanceDelete()
        handler.handle(self.env, notification)

    def instance_update(self, notification):
        self.log.info("instance_update")
        handler = EventInstanceUpdate()
        handler.handle(self.env, notification)

    def instance_down(self, notification):
        pass

    def instance_up(self, notification):
        pass

    def region_add(self, notification):
        pass

    def region_delete(self, notification):
        pass

    def region_update(self, notification):
        pass

    def network_create(self, notification):
        self.log.info("network_add")
        handler = EventNetworkAdd()
        handler.handle(self.env, notification)

    def network_update(self, notification):
        self.log.info("network_update")
        handler = EventNetworkUpdate()
        handler.handle(self.env, notification)

    def network_delete(self, notification):
        self.log.info("network_delete")
        handler = EventNetworkDelete()
        handler.handle(self.env, notification)

    def subnet_create(self, notification):
        self.log.info("subnet_add")
        handler = EventSubnetAdd()
        handler.handle(self.env, notification)

    def subnet_update(self, notification):
        self.log.info("subnet_update")
        handler = EventSubnetUpdate()
        handler.handle(self.env, notification)

    def subnet_delete(self, notification):
        self.log.info("subnet_delete")
        handler = EventSubnetDelete()
        handler.handle(self.env, notification)

    def port_create(self, notification):
        self.log.info("port_add")
        handler = EventPortAdd()
        handler.handle(self.env, notification)

    def port_update(self, notification):
        self.log.info("port_update")
        handler = EventPortUpdate()
        handler.handle(self.env, notification)

    def port_delete(self, notification):
        self.log.info("port_delete")
        handler = EventPortDelete()
        handler.handle(self.env, notification)

    def router_create(self, notification):
        self.log.info("router_add")
        handler = EventRouterAdd()
        handler.handle(self.env, notification)

    def router_update(self, notification):
        self.log.info("router_update")
        handler = EventRouterUpdate()
        handler.handle(self.env, notification)

    def router_delete(self, notification):
        self.log.info("router_delete")
        handler = EventRouterDelete()
        handler.handle(self.env, notification)

    def router_interface_create(self, notification):
        self.log.info("router_interface_add")
        handler = EventInterfaceAdd()
        handler.handle(self.env, notification)

    def router_interface_delete(self, notification):
        self.log.info("router_interface_delete")
        handler = EventInterfaceDelete()
        handler.handle(self.env, notification)
