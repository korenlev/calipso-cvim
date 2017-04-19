from discover.events.constants import INTERFACE_OBJECT_TYPE
from discover.events.event_base import EventResult
from discover.events.event_delete_base import EventDeleteBase
from discover.events.event_port_delete import EventPortDelete
from utils.util import encode_router_id


class EventInterfaceDelete(EventDeleteBase):

    OBJECT_TYPE = INTERFACE_OBJECT_TYPE

    def handle(self, env, values):
        interface = values['payload']['router_interface']
        port_id = interface['port_id']
        host_id = values["publisher_id"].replace("network.", "", 1)
        router_id = encode_router_id(host_id, interface['id'])

        # update router document
        port_doc = self.inv.get_by_id(env, port_id)
        if not port_doc:
            self.log.info("Interface deleting handler: port document not found.")
            return self.construct_event_result(result=False, retry=False, object_id=interface['id'])
        network_id = port_doc['network_id']

        router_doc = self.inv.get_by_id(env, router_id)
        if router_doc and network_id in router_doc.get('network', []):
            router_doc['network'].remove(network_id)
            self.inv.set(router_doc)

        # delete port document
        result = EventPortDelete().delete_port(env, port_id)
        result.object_id = interface['id']
        # TODO: related document_id?
        return result
