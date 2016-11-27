from discover.cli_fetch_host_vservice import CliFetchHostVservice
from discover.fetcher import Fetcher
from discover.find_links_for_vservice_vnics import FindLinksForVserviceVnics
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork


class EventRouterUpdate(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, values):
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
            if router_doc['network'] is not None:
                router_doc['network'] = []
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
            # add gw_port_id
            fetcher = CliFetchHostVservice()
            fetcher.set_env(env)
            router_vservice = fetcher.get_vservice(host_id, router_id)
            router_doc['gw_port_id'] = router_vservice['gw_port_id']

            # rescan the vnic links.
            fetcher = FindLinksForVserviceVnics()
            fetcher.add_links(search={'parent_id': router_id + '-vnics'})

        self.inv.set(router_doc)

        # update the cliques.
        scanner = ScanNetwork()
        scanner.scan_cliques()
        self.log.info("Finished router update.")
