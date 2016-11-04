import datetime

from discover.api_access import ApiAccess
from discover.api_fetch_port import ApiFetchPort
from discover.api_fetch_regions import ApiFetchRegions
from discover.db_fetch_port import DbFetchPort
from discover.events.event_port_add import EventPortAdd
from discover.fetcher import Fetcher
from discover.find_links_for_pnics import FindLinksForPnics
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork


class EventSubnetAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def add_port_document(self, env, project_id, network_id, network_name, port_id):
        fetcher = ApiFetchPort()
        fetcher.set_env(env)
        ports = fetcher.get(port_id)

        for doc in ports:
            doc['type'] = "port"
            doc['environment'] = env
            port_id = doc['id']
            doc['id_path'] = "%s/%s-projects/%s/%s-networks/%s/%s-ports/%s" % \
                             (env, env, project_id, project_id, network_id, network_id, port_id)
            doc['last_scanned'] = datetime.datetime.utcnow()
            doc['name_path'] = "/%s/Projects/%s/Networks/%s/Ports/%s" % \
                               (env, doc['project'], network_name, port_id)
            self.inv.set(doc)

    def add_ports_folder(self, env, project_id, network_id, network_name):
        port_folder = {
            "id": network_id + "-ports",
            "create_object": True,
            "name": "Ports",
            "text": "Ports",
            "type": "ports_folder",
            "parent_id": network_id,
            "parent_type": "network",
            'environment': env,
            'id_path': "%s/%s-projects/%s/%s-networks/%s/%s-ports/" % (env, env, project_id, project_id,
                                                                       network_id, network_id),
            'name_path': "/%s/Projects/%s/Networks/%s/Ports" % (env, project_id, network_name),
            "show_in_tree": True,
            "last_scanned": datetime.datetime.utcnow(),
            "object_name": "Ports",
        }

        self.inv.set(port_folder)

    def add_children_documents(self, env, notification, project_id, network_id, network_name):
        # generate port folder data.
        self.add_ports_folder(env, project_id, network_id, network_name)

        # get ports ID.
        ports_fetcher = DbFetchPort()
        port_id = ports_fetcher.get_id(network_id)

        # add specific ports documents.
        self.add_port_document(env, project_id, network_id, network_name, port_id)

        port_handler = EventPortAdd()

        # add network_services_folder document.
        port_handler.add_network_services_folder(env, project_id, network_id, network_name)

        # add dhcp vservice document.
        host_id = notification["publisher_id"].replace("network.", "", 1)
        host = self.inv.get_by_id(env, host_id)

        port_handler.add_dhcp_document(env, host, network_id, network_name)

        # add vnics folder.
        port_handler.add_vnics_folder(env, host, network_id, network_name)

        # add vnic docuemnt.
        port_handler.add_vnic_document(env, host, network_id, network_name)


    def handle(self, env, notification):
        # check for network document.
        subnet = notification['payload']['subnet']
        project_id = subnet['tenant_id']
        network_id = subnet['network_id']

        network_document = self.inv.get_by_id(env, network_id)
        if not network_document:
            self.log.info('network document does not exist, aborting subnet add')
            return None
        network_name = network_document['name']

        # build subnet document for adding network
        network_document['cidrs'].append(subnet['cidr'])
        if network_document['subnets'] == []:
            network_document['subnets'] = {}

        network_document['subnets'][subnet['name']] = subnet
        network_document['subnets_id'].append(subnet['id'])
        self.inv.set(network_document)

        # Check DHCP enable, if true, scan network.
        if subnet['enable_dhcp'] == True:
            # update network
            if len(ApiAccess.regions) == 0:
                fetcher = ApiFetchRegions()
                fetcher.set_env(env)
                fetcher.get(None)

            self.log.info("add new subnet.")
            self.add_children_documents(env, notification, project_id, network_id, network_name)

        # scan links and cliques
        self.log.info("scanning for links")
        fetcher = FindLinksForPnics()
        fetcher.add_links()
        fetcher = FindLinksForVserviceVnics()
        fetcher.add_links(search={"parent_id": "qdhcp-%s-vnics" % network_id})

        network_scanner = ScanNetwork()
        network_scanner.scan_cliques()
        self.log.info("Finished subnet added.")
