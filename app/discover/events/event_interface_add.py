from discover.api_access import ApiAccess
from discover.api_fetch_regions import ApiFetchRegions
from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_port_add import EventPortAdd
from discover.events.event_subnet_add import EventSubnetAdd
from discover.fetcher import Fetcher
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork


class EventInterfaceAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def update_router(self, env, project_id, network_id, network_name, router_id, host_id):
        router_doc = self.inv.get_by_id(env, router_id)
        if router_doc != []:
            router_doc['network'].append(network_id)

            # if gw_port_id is None, add gateway port first.
            if router_doc['gw_port_id'] == None:
                fetcher = CliFetchHostVservice()
                fetcher.set_env(env)

                router = fetcher.get_vservice(host_id, router_id)
                router_doc['gw_port_id'] = router['gw_port_id']

                subnet_handler = EventSubnetAdd()
                subnet_handler.add_port_document(env, project_id, network_id, network_name, router['gw_port_id'])

                # add vnic document
                port_handler = EventPortAdd()
                host = self.inv.get_by_id(env, host_id)
                id = router_id.replace('qrouter-', '', 1)
                port_handler.add_vnic_document(env, host, id=id, network_name=network_name, type="router",
                                               router_name=router['name'])
            self.inv.set(router_doc)
        else:
            self.inv.log.info("router document not found, aborting interface adding")

    def handle(self, env, values):
        interface = values['payload']['router_interface']
        port_id = interface['port_id']
        subnet_id = interface['subnet_id']
        project_id = interface['tenant_id']
        router_id = 'qrouter-' + interface['id']

        network_document = self.inv.get_by_field(env, "network", "subnet_ids", subnet_id, get_single=True)
        if network_document == []:
            self.inv.log.info("network document not found, aborting interface adding")
            return
        network_name = network_document['name']
        network_id = network_document['id']

        # add router-interface port document.
        subnet_handler = EventSubnetAdd()
        if len(ApiAccess.regions) == 0:
            fetcher = ApiFetchRegions()
            fetcher.set_env(env)
            fetcher.get(None)
        subnet_handler.add_port_document(env, project_id, network_id, network_name, port_id)

        # update the router document: gw_port_id, network.
        host_id = values["publisher_id"].replace("network.", "", 1)
        self.update_router(env, project_id, network_id, network_name, router_id, host_id)

        # update vservice-vnic, vnic-network,
        fetcher = FindLinksForVserviceVnics()
        fetcher.add_links(search={"parent_id": router_id})

        scanner = ScanNetwork()
        scanner.scan_cliques()
        self.log.info("Finished router-interface added.")
