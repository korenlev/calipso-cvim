import datetime

from discover.cli_fetch_vservice_vnics import CliFetchVserviceVnics
from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventPortAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get_name_by_id(self, id):
        item = self.inv.get_by_id(self.env, id)
        if item:
            return item['name']
        return None

    def add_port_document(self, env, project_name, project_id, network_name, network_id, port):
        # add other data for port document
        port['type'] = 'port'
        port['environment'] = env

        port['parent_id'] = port['network_id'] + '-ports'
        port['parent_text'] = 'Ports'
        port['parent_type'] = 'ports_folder'

        port['name'] = port['mac_address']
        port['object'] = port['name']
        port['project'] = project_name

        port['id_path'] = "%s/%s-projects/%s/%s-networks/%s/%s-ports/%s" % \
                             (env, env, project_id, project_id, network_id, network_id, port['id'])
        port['name_path'] = "/%s/Projects/%s/Networks/%s/Ports/%s" % \
                                (env, project_name, network_name, port['id'])

        port['show_in_tree'] = True
        port['last_scanned'] = datetime.datetime.utcnow()
        self.inv.set(port)

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
            "children_url": "/osdna_dev/discover.py?type=tree&id=qdhcp-"+network_id,
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

    def add_vnics_folder(self, env, host_id, host_id_path, host_name_path,
                         network_id, network_name, type="dhcp", router_name=''):
        type_map = {"dhcp": ('DHCP servers', 'dhcp-'+network_name),
                    "router": ('Gateways', router_name)}

        vnics_folder = {
            "environment": env,
            "id": "q%s-%s-vnics" % (type, network_id),
            "id_path": host_id_path + "/%s-vservices/%s-vservices-%ss/q%s-%s/q%s-%s-vnics" %
                                      (host_id, host_id, type, type, network_id, type, network_id),
            "last_scanned": datetime.datetime.utcnow(),
            "name": "q%s-%s-vnics" % (type, network_id),
            "name_path": host_name_path + "/Vservices/%s/%s/vNICs" % (type_map[type][0], type_map[type][1]),
            "object_name": "vNICs",
            "parent_id": "q%s-%s" %(type, network_id),
            "parent_type": "vservice",
            "show_in_tree": True,
            "text": "vNICs",
            "type": "vnics_folder"
        }
        print("vnics folder", vnics_folder)
        self.inv.set(vnics_folder)

    def add_vnic_document(self, env, host_id, host_id_path, host_name_path, network_id, network_name,
                          type='dhcp', router_name=''):
        type_map = {"dhcp": ('DHCP servers', 'dhcp-'+network_name),
                    "router": ('Gateways', router_name)}

        fetcher = CliFetchVserviceVnics()
        namespace = 'q%s-%s' % (type, network_id)
        vnic_document = fetcher.handle_service(host_id, namespace)

        for doc in vnic_document:
            doc["environment"] = env
            doc["id_path"] = host_id_path + "/%s-vservices/%s-vservices-%ss/%s/%s-vnics/%s" % \
                             (host_id, host_id, type, namespace, namespace, doc["id"]),
            doc["name_path"] = host_name_path + "/Vservices/%s/%s/vNICs/%s" %\
                                                (type_map[type][0],type_map[type][1], doc["id"])

            self.inv.set(doc)
            print("vnic", doc)

    def handle_dhcp_device(self, env, notification, network_id, network_name):
        # add dhcp vservice document.
        host_id = notification["publisher_id"].replace("network.", "", 1)
        host = self.inv.get_by_id(env, host_id)

        self.add_dhcp_document(env, host["id"], host["id_path"], host["name_path"], network_id, network_name)

        # add vnics folder.
        self.add_vnics_folder(env, host["id"], host["id_path"], host["name_path"], network_id, network_name)

        # add vnic docuemnt.
        self.add_vnic_document(env, host["id"], host["id_path"], host["name_path"], network_id, network_name)


    def handle(self, env, notification):
        self.project = notification['_context_project_name']
        self.project_id = notification['_context_project_id']
        self.payload = notification['payload']
        self.port = self.payload['port']
        self.network_id = self.port['network_id']
        self.network_name = self.get_name_by_id(self.network_id)
        self.port_name = self.port['mac_address']
        self.port_id = self.port['id']

        # check ports folder document.
        ports_folder = self.inv.get_by_id(self.env, self.port_id+'-ports')
        if not ports_folder:
            print("not folder")
            self.add_ports_folder(self.env, self.project_id, self.network_id, self.network_name)
        self.add_port_document(self.env, self.project, self.project_id, self.network_name, self.network_id, self.port)

        port_device_owner_handler = {
            "network:router_gateway": None,
            "network:floatingip": None,
            "network:dhcp": self.handle_dhcp_device,
            "network:router_interface": None,
            # other type will be handled by instance scanning.
        }

        if self.port['device_owner']:pass

        print("\n Todo: add port for network")
