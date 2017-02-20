import datetime

from discover.api_fetch_host_instances import ApiFetchHostInstances
from discover.cli_fetch_instance_vnics import CliFetchInstanceVnics
from discover.cli_fetch_instance_vnics_vpp import CliFetchInstanceVnicsVpp
from discover.cli_fetch_vservice_vnics import CliFetchVserviceVnics
from discover.events.event_base import EventBase
from discover.find_links_for_instance_vnics import FindLinksForInstanceVnics
from discover.find_links_for_vedges import FindLinksForVedges
from discover.scan_instances_root import ScanInstancesRoot


class EventPortAdd(EventBase):

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
        self.inv.log.info("add port document for port: %s" % port['id'])

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
        self.inv.log.info("add ports_folder document for network: %s." % network_id)

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
        self.inv.log.info("add network services folder for network:%s" % network_id)

    def add_dhcp_document(self, env, host, network_id, network_name):
        dhcp_document = {
            "children_url": "/osdna_dev/discover.py?type=tree&id=qdhcp-" + network_id,
            "environment": env,
            "host": host['id'],
            "id": "qdhcp-" + network_id,
            "id_path": host['id_path'] + "/%s-vservices/%s-vservices-dhcps/qdhcp-%s" % (
                host['id'], host['id'], network_id),
            "last_scanned": datetime.datetime.utcnow(),
            "local_service_id": "qdhcp-" + network_id,
            "name": "dhcp-" + network_name,
            "name_path": host['name_path'] + "/Vservices/DHCP servers/dhcp-" + network_name,
            "network": [network_id],
            "object_name": "dhcp-" + network_name,
            "parent_id": host['id'] + "-vservices-dhcps",
            "parent_text": "DHCP servers",
            "parent_type": "vservice_dhcps_folder",
            "service_type": "dhcp",
            "show_in_tree": True,
            "type": "vservice"
        }
        self.inv.set(dhcp_document)
        self.inv.log.info("add DHCP document for network:%s." % network_id)

    def add_vnics_folder(self, env, host, id, network_name='', type="dhcp", router_name=''):
        # when vservice is DHCP, id = network_id,
        # when vservice is router, id = router_id
        type_map = {"dhcp": ('DHCP servers', 'dhcp-' + network_name),
                    "router": ('Gateways', router_name)}

        vnics_folder = {
            "environment": env,
            "id": "q%s-%s-vnics" % (type, id),
            "id_path": host['id_path'] + "/%s-vservices/%s-vservices-%ss/q%s-%s/q%s-%s-vnics" %
                                         (host['id'], host['id'], type, type, id, type, id),
            "last_scanned": datetime.datetime.utcnow(),
            "name": "q%s-%s-vnics" % (type, id),
            "name_path": host['name_path'] + "/Vservices/%s/%s/vNICs" % (type_map[type][0], type_map[type][1]),
            "object_name": "vNICs",
            "parent_id": "q%s-%s" % (type, id),
            "parent_type": "vservice",
            "show_in_tree": True,
            "text": "vNICs",
            "type": "vnics_folder"
        }
        self.inv.set(vnics_folder)
        self.inv.log.info("add vnics_folder document for q%s-%s-vnics" % (type, id))

    def add_vnic_document(self, env, host, id, network_name='', type='dhcp', router_name='', mac_address=None):
        # when vservice is DHCP, id = network_id,
        # when vservice is router, id = router_id
        type_map = {"dhcp": ('DHCP servers', 'dhcp-' + network_name),
                    "router": ('Gateways', router_name)}

        fetcher = CliFetchVserviceVnics()
        fetcher.set_env(env)
        namespace = 'q%s-%s' % (type, id)
        vnic_documents = fetcher.handle_service(host['id'], namespace, enable_cache=False)
        if vnic_documents == []:
            self.inv.log.info("Vnic document not found in namespace.")
            return False

        if mac_address != None:
            for doc in vnic_documents:
                if doc['mac_address'] == mac_address:
                    # add a specific vnic document.
                    doc["environment"] = env
                    doc["id_path"] = "%s/%s-vservices/%s-vservices-%ss/%s/%s-vnics/%s" % (host['id_path'], host['id'],
                                                                                          host['id'], type, namespace,
                                                                                          namespace, doc["id"])
                    doc["name_path"] = host['name_path'] + "/Vservices/%s/%s/vNICs/%s" % \
                                                           (type_map[type][0], type_map[type][1], doc["id"])
                    self.inv.set(doc)
                    self.inv.log.info("add vnic document with mac_address: %s." % mac_address)
                    return True

            self.inv.log.info("Can not find vnic document by mac_address: %s" % mac_address)
            return False
        else:
            for doc in vnic_documents:
                # add all vnic documents.
                doc["environment"] = env
                doc["id_path"] = "%s/%s-vservices/%s-vservices-%ss/%s/%s-vnics/%s" % (host['id_path'], host['id'],
                                                                                      host['id'], type, namespace,
                                                                                      namespace, doc["id"])
                doc["name_path"] = host['name_path'] + "/Vservices/%s/%s/vNICs/%s" % \
                                                       (type_map[type][0], type_map[type][1], doc["id"])
                self.inv.set(doc)
                self.inv.log.info("add vnic document with mac_address: %s." % doc["mac_address"])
            return True

    def handle_dhcp_device(self, env, notification, network_id, network_name, mac_address=None):
        # add dhcp vservice document.
        host_id = notification["publisher_id"].replace("network.", "", 1)
        host = self.inv.get_by_id(env, host_id)

        self.add_dhcp_document(env, host, network_id, network_name)

        # add vnics folder.
        self.add_vnics_folder(env, host, network_id, network_name)

        # add vnic docuemnt.
        self.add_vnic_document(env, host, network_id, network_name, mac_address=mac_address)

    def handle(self, env, notification):
        self.project = notification['_context_project_name']
        self.project_id = notification['_context_project_id']
        self.payload = notification['payload']
        self.port = self.payload['port']
        self.network_id = self.port['network_id']
        self.network_name = self.get_name_by_id(self.network_id)
        self.mac_address = self.port['mac_address']
        self.port_id = self.port['id']

        # check ports folder document.
        ports_folder = self.inv.get_by_id(env, self.network_id + '-ports')
        if not ports_folder:
            self.log.info("ports folder not found, add ports folder first.")
            self.add_ports_folder(env, self.project_id, self.network_id, self.network_name)
        self.add_port_document(env, self.project, self.project_id, self.network_name, self.network_id, self.port)

        # update the port related documents.
        if 'compute' in self.port['device_owner']:
            # update the instance related document.
            host_id = self.port['binding:host_id']
            instance_id = self.port['device_id']
            old_instance_doc = self.inv.get_by_id(env, instance_id)
            instances_root_id = host_id + '-instances'
            instances_root = self.inv.get_by_id(env, instances_root_id)
            if not instances_root:
                self.log.info('instance document not found, aborting port adding')
                return None

            # update instance
            instance_fetcher = ApiFetchHostInstances()
            instance_fetcher.set_env(env)
            instance_docs = instance_fetcher.get(host_id + '-')
            for instance in instance_docs:
                if instance_id == instance['id']:
                    old_instance_doc['network_info'] = instance['network_info']
                    old_instance_doc['network'] = instance['network']
                    if 'mac_address' not in old_instance_doc:
                        old_instance_doc['mac_address'] = self.mac_address
                    elif old_instance_doc['mac_address'] == None:
                        old_instance_doc['mac_address'] = self.mac_address

                    self.inv.set(old_instance_doc)
                    self.inv.log.info("update instance document")
                    break

            # add vnic document.
            if self.port['binding:vif_type'] == 'vpp':
                vnic_fetcher = CliFetchInstanceVnicsVpp()
            else:
                # set ovs as default type.
                vnic_fetcher = CliFetchInstanceVnics()

            vnic_fetcher.set_env(env)
            vnic_docs = vnic_fetcher.get(instance_id + '-', enable_cache=False)
            for vnic in vnic_docs:
                if vnic['mac_address'] == self.mac_address:
                    vnic['environment'] = env
                    vnic['type'] = 'vnic'
                    vnic['name_path'] = old_instance_doc['name_path'] + '/vNICs/' + vnic['name']
                    vnic['id_path'] = old_instance_doc['id_path'] + '/%s/%s' % (old_instance_doc['id'], vnic['name'])
                    self.inv.set(vnic)
                    self.inv.log.info("add instance-vnic document, mac_address: %s" % self.mac_address)
                    break

            self.log.info("scanning for links")
            fetchers_implementing_add_links = [FindLinksForInstanceVnics(), FindLinksForVedges()]
            for fetcher in fetchers_implementing_add_links:
                fetcher.add_links()
            ScanInstancesRoot().scan_cliques()
            return True
