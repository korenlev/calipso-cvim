import datetime

from discover.api_access import ApiAccess
from discover.api_fetch_port import ApiFetchPort
from discover.cli_fetch_vservice_vnics import CliFetchVserviceVnics
from discover.db_fetch_port import DbFetchPort
from discover.fetcher import Fetcher
from discover.find_links_for_pnics import FindLinksForPnics
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork
from discover.scan_regions_root import ScanRegionsRoot


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

    def add_network_services_folder(self, env, project_id, network_id, network_name):
        network_services_folder = {
            "create_object": True,
            "environment": env,
            "id": network_id + "-network_services",
            "id_path": "%s/%s-projects/%s/%s-networks/%s/%s-network_services/" % (env, env, project_id, project_id,
                                                                                  network_id, network_id),
            "last_scanned": datetime.datetime.utcnow(),
            "name": "Network vServices",
            "name_path": "/%s/Projects/%s/Networks/%s/Network vServices" % (env, project_id, network_name),
            "object_name": "Network vServices",
            "parent_id": network_id,
            "parent_type": "network",
            "show_in_tree": True,
            "text": "Network vServices",
            "type": "network_services_folder"
        }
        self.inv.set(network_services_folder)

    def add_dhcp_document(self, env, host_id, host_id_path, host_name_path, network_id, network_name):
        dhcp_document = {
            "children_url": "/osdna_dev/discover.py?type=tree&id=qdhcp-99941aaa-7f98-45cc-919d-99bf60936bb1",
            "environment": env,
            "host": host_id,
            "id": "qdhcp-" + network_id,
            "id_path": host_id_path + "/%s-vservices/%s-vservices-dhcps/qdhcp-%s" % (host_id, host_id, network_id),
            "last_scanned": datetime.datetime.utcnow(),
            "local_service_id": "qdhcp-" + network_id,
            "name": "dhcp-" + network_name,
            "name_path": host_name_path + "/Vservices/DHCP servers/dhcp-" + network_name,
            "network": [network_id],
            "object_name": "dhcp-" + network_name,
            "parent_id": host_id + "-vservices-dhcps",
            "parent_text": "DHCP servers",
            "parent_type": "vservice_dhcps_folder",
            "service_type": "dhcp",
            "show_in_tree": True,
            "type": "vservice"
        }

        self.inv.set(dhcp_document)

    def add_vnics_folder(self, env, host_id, host_id_path, host_name_path, network_id, network_name):
        vnics_folder = {
            "environment": env,
            "id": "qdhcp-%s-vnics" % network_id,
            "id_path": host_id_path + "/%s-vservices/%s-vservices-dhcps/qdhcp-%s/qdhcp-%s-vnics" % (host_id, host_id,
                                                                                                    network_id,
                                                                                                    network_id),
            "last_scanned": datetime.datetime.utcnow(),
            "name": "qdhcp-%s-vnics" % network_id,
            "name_path": host_name_path + "/Vservices/DHCP servers/dhcp-%s/vNICs" % network_name,
            "object_name": "vNICs",
            "parent_id": "qdhcp-" + network_id,
            "parent_type": "vservice",
            "show_in_tree": True,
            "text": "vNICs",
            "type": "vnics_folder"
        }
        self.inv.set(vnics_folder)

    def add_vnic_document(self, env, host_id, host_id_path, host_name_path, network_id, network_name, service):
        fetcher = CliFetchVserviceVnics()
        vnic_document = fetcher.handle_service(host_id, service)
        for doc in vnic_document:
            doc["environment"] = env
            doc["id_path"] = host_id_path + "/%s-vservices/%s-vservices-dhcps/qdhcp-%s/qdhcp-%s-vnics/%s" % \
                             (host_id, host_id, network_id, network_id, doc["id"]),
            doc["name_path"] = host_name_path + "/Vservices/DHCP servers/dhcp-%s/vNICs/%s" % (network_name, doc["id"])

            self.inv.set(doc)

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
        else:
            network_document['subnets'][subnet['name']] = subnet

        self.inv.set(network_document)

        # Check DHCP enable, if true, scan network.
        if subnet['enable_dhcp'] == True:
            # scan network
            if len(ApiAccess.regions) == 0:
                # regions info doesn't exist, scan region.
                self.log.info("Scan regions for adding regions data.")
                regions_root_scanner = ScanRegionsRoot()
                regions_root_scanner.set_env(env)
                regions_root_doc = self.inv.get_by_id(env, env + "-regions")
                if len(regions_root_doc) == 0:
                    self.log.info("Regions_folder is not found.")
                    return None
                else:
                    regions_root_scanner.scan(regions_root_doc)
                    regions_root_scanner.scan_from_queue()
            else:
                # scan new network.
                self.log.info("Scan new network.")

                # generate port folder data.
                self.add_ports_folder(env, project_id, network_id, network_name)

                # get ports ID.
                ports_fetcher = DbFetchPort()
                port_id = ports_fetcher.get_id(network_id)

                # add specific ports documents.
                self.add_port_document(env, project_id, network_id, network_name, port_id)

                # add network_services_folder document.
                self.add_network_services_folder(env, project_id, network_id, network_name)

                # add dhcp vservice document.
                host_id = notification["publisher_id"].replace("network.", "", 1)
                host = self.inv.get_by_id(env, host_id)

                self.add_dhcp_document(env, host["id"], host["id_path"], host["name_path"], network_id, network_name)

                # add vnics folder.
                self.add_vnics_folder(env, host["id"], host["id_path"], host["name_path"], network_id, network_name)

                # add vnic docuemnt.
                self.add_vnic_document(env, host["id"], host["id_path"], host["name_path"],
                                       network_id, network_name, "qdhcp-" + network_id)

        # scan links and cliques
        self.log.info("scanning for links")
        fetchers_implementing_add_links = [
            FindLinksForPnics(),
            FindLinksForVserviceVnics(),
        ]
        for fetcher in fetchers_implementing_add_links:
            fetcher.add_links()

        network_scanner = ScanNetwork()
        network_scanner.scan_cliques()

        self.log.info("Finished subnet added.")
