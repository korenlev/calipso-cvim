from discover.api_access import ApiAccess
from discover.api_fetch_regions import ApiFetchRegions
from discover.db_fetch_port import DbFetchPort
from discover.events.constants import SUBNET_OBJECT_TYPE
from discover.events.event_base import EventBase, EventResult
from discover.events.event_port_add import EventPortAdd
from discover.events.event_port_delete import EventPortDelete
from discover.events.event_subnet_add import EventSubnetAdd
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.scan_network import ScanNetwork


class EventSubnetUpdate(EventBase):

    OBJECT_TYPE = SUBNET_OBJECT_TYPE

    def handle(self, env, notification):
        # check for network document.
        subnet = notification['payload']['subnet']
        project = notification['_context_project_name']
        host_id = notification['publisher_id'].replace('network.', '', 1)
        subnet_id = subnet['id']
        network_id = subnet['network_id']
        network_document = self.inv.get_by_id(env, network_id)
        if not network_document:
            self.log.info('network document does not exist, aborting subnet update')
            return self.construct_event_result(result=False, retry=True, object_id=subnet_id)

        # update network document.
        subnets = network_document['subnets']
        key = next(filter(lambda k: subnets[k]['id'] == subnet_id, subnets), None)

        if key:
            if subnet['enable_dhcp'] and subnets[key]['enable_dhcp'] is False:
                # scan DHCP namespace to add related document.
                # add dhcp vservice document.
                host = self.inv.get_by_id(env, host_id)
                port_handler = EventPortAdd()
                port_handler.add_dhcp_document(env, host, network_id, network_document['name'])

                # make sure that self.regions is not empty.
                if len(ApiAccess.regions) == 0:
                    fetcher = ApiFetchRegions()
                    fetcher.set_env(env)
                    fetcher.get(None)

                self.log.info("add port binding to DHCP server.")
                port_id = DbFetchPort().get_id_by_field(network_id, """device_owner LIKE "%dhcp" """)
                port = EventSubnetAdd().add_port_document(env, port_id, network_name=network_document['name'],
                                                   project_name=project)
                if port:
                    port_handler.add_vnic_document(env, host, network_id, network_name=network_document['name'],
                                                   mac_address=port['mac_address'])
                    # add link for vservice - vnic
                    FindLinksForVserviceVnics().add_links(search={"id": "qdhcp-%s" % network_id})
                    ScanNetwork().scan_cliques()

            if subnet['enable_dhcp'] is False and subnets[key]['enable_dhcp']:
                # delete existed related DHCP documents.
                self.inv.delete("inventory", {'id': "qdhcp-%s" % subnet['network_id']})
                self.log.info("delete DHCP document: qdhcp-%s" % subnet['network_id'])

                port = self.inv.find_items({'network_id': subnet['network_id'],
                                            'device_owner': 'network:dhcp'}, get_single=True)
                if 'id' in port:
                    EventPortDelete().delete_port(env, port['id'])
                    self.log.info("delete port binding to DHCP server.")

            if subnet['name'] == subnets[key]['name']:
                subnets[key] = subnet
            else:
                # TODO: #AskCheng shouldn't we remove the old one?
                subnets[subnet['name']] = subnet

            self.inv.set(network_document)
            return self.construct_event_result(result=True,
                                               object_id=subnet_id,
                                               document_id=network_document.get('_id'))  # TODO: is this correct?
