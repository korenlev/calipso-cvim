import datetime

from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_base import EventBase
from discover.events.event_port_add import EventPortAdd
from discover.events.event_subnet_add import EventSubnetAdd
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.scan_network import ScanNetwork


class EventRouterAdd(EventBase):

    def add_router_document(self, env, network_id, router_doc, host):
        router_doc["children_url"] = "/osdna_dev/discover.py?type=tree&id=%s" % router_doc['id']
        router_doc["environment"] = env
        router_doc["id_path"] = host['id_path'] + "/%s-vservices/%s-vservices-routers/%s" % (host['id'], host['id'],
                                                                                             router_doc['id'])
        router_doc['last_scanned'] = datetime.datetime.utcnow()
        router_doc['name_path'] = host['name_path'] + "/Vservices/Gateways/%s" % router_doc['name']
        router_doc['network'] = []
        if network_id != None:
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
        add_port_return = subnet_handler.add_port_document(env, router_doc['gw_port_id'], network_name=network_name)

        # add vnics folder and vnic document
        port_handler = EventPortAdd()
        port_handler.add_vnics_folder(env, host, id=router_id, network_name=network_name, type="router",
                                      router_name=router_doc['name'])

        if add_port_return != False:
            add_vnic_return = port_handler.add_vnic_document(env, host, id=router_id, network_name=network_name,
                                                             type="router", router_name=router_doc['name'])
            if add_vnic_return == False:
                self.inv.log.info("Try to add vnic document again.")
                port_handler.add_vnic_document(env, host, id=router_id, network_name=network_name,
                                               type="router", router_name=router_doc['name'])
        else:
            # in some cases, port has been created, but port doc can not be fetched by OpenStack API
            self.inv.log.info("Try to add port document again.")
            add_port_return = port_handler.add_vnics_folder(env, host, id=router_id, network_name=network_name,
                                                            type="router", router_name=router_doc['name'])
            if add_port_return == False:
                self.inv.log.info("Try to add vnic document again.")
                port_handler.add_vnic_document(env, host, id=router_id, network_name=network_name,
                                               type="router", router_name=router_doc['name'])

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
        self.add_router_document(env, None, router_doc, host)

        # scan links and cliques
        FindLinksForVserviceVnics().add_links(search={"parent_id": router_id})
        ScanNetwork().scan_cliques()
        self.log.info("Finished router added.")
