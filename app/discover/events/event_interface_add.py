import time

from discover.api_access import ApiAccess
from discover.api_fetch_regions import ApiFetchRegions
from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_base import EventBase, EventResult
from discover.events.event_port_add import EventPortAdd
from discover.events.event_subnet_add import EventSubnetAdd
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.scan_network import ScanNetwork
from utils.util import decode_router_id, encode_router_id


class EventInterfaceAdd(EventBase):
    def __init__(self):
        super().__init__()
        self.delay = 2

    def add_gateway_port(self, env, project, network_name, router_doc, host_id):
        fetcher = CliFetchHostVservice()
        fetcher.set_env(env)
        router_id = router_doc['id']
        router = fetcher.get_vservice(host_id, router_id)
        device_id = decode_router_id(router_id)
        router_doc['gw_port_id'] = router['gw_port_id']

        # add gateway port documents.
        port_doc = EventSubnetAdd().add_port_document(env, router_doc['gw_port_id'], project_name=project)

        mac_address = port_doc['mac_address'] if port_doc else None

        # add vnic document
        host = self.inv.get_by_id(env, host_id)
        ret = EventPortAdd().add_vnic_document(env, host, id=device_id, network_name=network_name, type="router",
                                               router_name=router_doc['name'], mac_address=mac_address)
        if not ret:
            time.sleep(self.delay)
            self.inv.log.info("Wait %s second, and then fetch vnic document again." % self.delay)
            EventPortAdd().add_vnic_document(env, host, id=device_id, network_name=network_name, type="router",
                                             router_name=router_doc['name'], mac_address=mac_address)

    def update_router(self, env, project, network_id, network_name, router_doc, host_id):
        if router_doc:
            if 'network' in router_doc:
                if network_id not in router_doc['network']:
                    router_doc['network'].append(network_id)
            else:
                router_doc['network'] = [network_id]

            # if gw_port_id is None, add gateway port first.
            if not router_doc.get('gw_port_id'):
                self.add_gateway_port(env, project, network_name, router_doc, host_id)
            else:
                # check the gateway port document, add it if document does not exist.
                port = self.inv.get_by_id(env, router_doc['gw_port_id'])
                if not port:
                    self.add_gateway_port(env, project, network_name, router_doc, host_id)
            self.inv.set(router_doc)
        else:
            self.inv.log.info("router document not found, aborting interface adding")

    def handle(self, env, values):
        interface = values['payload']['router_interface']
        project = values['_context_project_name']
        host_id = values["publisher_id"].replace("network.", "", 1)
        port_id = interface['port_id']
        subnet_id = interface['subnet_id']
        router_id = encode_router_id(host_id, interface['id'])

        network_document = self.inv.get_by_field(env, "network", "subnet_ids", subnet_id, get_single=True)
        if not network_document:
            self.inv.log.info("network document not found, aborting interface adding")
            return EventResult(result=False, retry=True)
        network_name = network_document['name']
        network_id = network_document['id']

        # add router-interface port document.
        if len(ApiAccess.regions) == 0:
            fetcher = ApiFetchRegions()
            fetcher.set_env(env)
            fetcher.get(None)
        port_doc = EventSubnetAdd().add_port_document(env, port_id, network_name=network_name)

        mac_address = port_doc['mac_address'] if port_doc else None

        # add vnic document
        host = self.inv.get_by_id(env, host_id)
        router_doc = self.inv.get_by_id(env, router_id)
        ret = EventPortAdd().add_vnic_document(env, host, id=interface['id'], network_name=network_name, type="router",
                                               router_name=router_doc['name'], mac_address=mac_address)

        if ret is False:
            # try it again to fetch vnic document, vnic will be created a little bit late before CLI fetch.
            time.sleep(self.delay)
            self.inv.log.info("Wait %s second, and then fetch vnic document again." % self.delay)
            EventPortAdd().add_vnic_document(env, host, id=interface['id'], network_name=network_name, type="router",
                                             router_name=router_doc['name'], mac_address=mac_address)
        # update the router document: gw_port_id, network.
        self.update_router(env, project, network_id, network_name, router_doc, host_id)

        # update vservice-vnic, vnic-network,
        FindLinksForVserviceVnics().add_links(search={"parent_id": router_id})
        ScanNetwork().scan_cliques()
        self.log.info("Finished router-interface added.")
        return EventResult(result=True)
