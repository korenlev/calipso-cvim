import datetime

from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_port_add import EventPortAdd
from discover.events.event_subnet_add import EventSubnetAdd
from discover.fetcher import Fetcher
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork


class EventRouterAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def add_router_document(self, env, network_id, router_doc, host):
        router_doc["children_url"] = "/osdna_dev/discover.py?type=tree&id=%s" % router_doc['id']
        router_doc["environment"] = env
        router_doc["id_path"] = host['id_path'] + "/%s-vservices/%s-vservices-routers/%s" % (host['id'], host['id'],
                                                                                             router_doc['id'])
        router_doc['last_scanned'] = datetime.datetime.utcnow()
        router_doc['name_path'] = host['name_path'] + "/Vservices/Gateways/%s" % router_doc['name']
        router_doc['network'] = [network_id]
        router_doc['object_name'] = router_doc['name']
        router_doc['parent_id'] = host['id'] + "-vservices-routers"
        router_doc['show_in_tree'] = True
        router_doc['type'] = "vservice"

        self.inv.set(router_doc)

    def add_children_documents(self, env, project_id, network_id, host, router_doc):

        network_document = self.inv.get_by_id(env, network_id)
        network_name = network_document['name']
        router_id = router_doc['id'].replace("qrouter-", "", 1)

        # add port for binding to vservice:router
        subnet_handler = EventSubnetAdd()
        ports_folder = self.inv.get_by_id(env, network_id + '-ports')
        if not ports_folder:
            self.log.info("Ports_folder not found.")
            subnet_handler.add_ports_folder(env, project_id, network_id, network_name)
        subnet_handler.add_port_document(env, project_id, network_id, network_name, router_doc['gw_port_id'])

        # add vnics folder and vnic document
        port_handler = EventPortAdd()
        port_handler.add_vnics_folder(env, host, id=router_id, network_name=network_name, type="router",
                                      router_name=router_doc['name'])

        port_handler.add_vnic_document(env, host, id=router_id, network_name=network_name, type="router",
                                       router_name=router_doc['name'])

    def update_links_and_cliques(self, fetchers, scanner):
        for fetcher in fetchers:
            fetcher.add_links()
        scanner.scan_cliques()

    def handle(self, env, values):
        router = values['payload']['router']
        host_id = values["publisher_id"].replace("network.", "", 1)
        project_id = values['_context_project_id']
        router_id = "qrouter-%s" % router['id']
        host = self.inv.get_by_id(env, host_id)

        fetcher = CliFetchHostVservice()
        fetcher.set_env(env)

        router_doc = fetcher.get_vservice(host_id, router_id)
        gateway_info = router['external_gateway_info']
        if gateway_info:
            network_id = router['external_gateway_info']['network_id']
            self.add_router_document(env, network_id, router_doc, host)
            self.add_children_documents(env, project_id, network_id, host, router_doc)

            # scan links and cliques
            self.update_links_and_cliques([FindLinksForVserviceVnics()], ScanNetwork())
            self.log.info("Finished router added.")

        self.add_router_document(env, None, router_doc, host)