from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.events.event_port_delete import EventPortDelete
from discover.events.event_router_add import EventRouterAdd
from discover.fetcher import Fetcher
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.scan_network import ScanNetwork
from utils.inventory_mgr import InventoryMgr


class EventRouterUpdate(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
        project_id = values['_context_project_id']
        router = values['payload']['router']
        router_id = "qrouter-%s" % router['id']
        router_doc = self.inv.get_by_id(env, router_id)
        host_id = values["publisher_id"].replace("network.", "", 1)
        if len(router_doc) == 0:
            self.log.info("Router document not found, aborting router updating")
            return None

        router_doc['admin_state_up'] = router['admin_state_up']
        router_doc['name'] = router['name']
        gateway_info = router['external_gateway_info']
        if gateway_info is None:
            # when delete gateway, need to delete the port relate document.
            port_doc = []
            if router_doc['gw_port_id']:
                port_doc = self.inv.get_by_id(env, router_doc['gw_port_id'])
                EventPortDelete().delete_port(env, router_doc['gw_port_id'])

            if router_doc.get('network')is not None:
                if len(port_doc):
                    router_doc['network'].remove(port_doc['network_id'])
                router_doc['gw_port_id'] = None

                # remove related links
                self.inv.delete('links', {'source_id': router_id})
        else:
            if 'network' in router_doc:
                if gateway_info['network_id'] not in router_doc['network']:
                    router_doc['network'].append(gateway_info['network_id'])
            else:
                router_doc['network'] = [gateway_info['network_id']]
            # update static route
            router_doc['routes'] = router['routes']

            # add gw_port_id info and port document.
            fetcher = CliFetchHostVservice()
            fetcher.set_env(env)
            router_vservice = fetcher.get_vservice(host_id, router_id)
            router_doc['gw_port_id'] = router_vservice['gw_port_id']

            host = self.inv.get_by_id(env, host_id)
            EventRouterAdd().add_children_documents(env, project_id, gateway_info['network_id'], host, router_doc)

            # rescan the vnic links.
            FindLinksForVserviceVnics().add_links(search={'parent_id': router_id + '-vnics'})
        self.inv.set(router_doc)

        # update the cliques.
        ScanNetwork().scan_cliques()
        self.log.info("Finished router update.")
