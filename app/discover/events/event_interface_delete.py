from discover.events.event_delete_base import EventDeleteBase
from discover.events.event_port_delete import EventPortDelete


class EventInterfaceDelete(EventDeleteBase):

    def handle(self, env, values):
        interface = values['payload']['router_interface']
        port_id = interface['port_id']
        router_id = 'qrouter-' + interface['id']

        # update router document
        port_doc = self.inv.get_by_id(env, port_id)
        if port_doc == []:
            self.log.info("Interface deleting handler: port document not found.")
            return None
        network_id = port_doc['network_id']

        router_doc = self.inv.get_by_id(env, router_id)
        if network_id in router_doc['network']:
            router_doc['network'].remove(network_id)
        self.inv.set(router_doc)

        # delete port document
        EventPortDelete().delete_port(env, port_id)
