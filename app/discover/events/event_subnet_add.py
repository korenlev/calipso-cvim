from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr
from discover.scan_network import ScanNetwork
from discover.scan_networks_root import ScanNetworksRoot


class EventSubnetAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        # check for network document.
        subnet = notification['payload']['subnet']
        network_id = subnet['network_id']
        network_document = self.inv.get_by_id(env, network_id)
        if not network_document:
            self.log.info('network document does not exist, aborting subnet add')
            return None

        # Check DHCP enable, if true, scan network.
        if subnet['enable_dhcp'] == True:
            network_scanner = ScanNetwork()
            network_scanner.set_env(env)
            # network_root_doc = self.inv.get_by_id(env, network_document['parent_id'])
            # print(network_root_doc)
            network_scanner.scan(network_document)
            network_scanner.scan_from_queue()
            network_scanner.scan_links()
            network_scanner.scan_cliques()
        else:
            # build subnet document for adding network
            subnet_name = subnet['name']
            subnet_document = {subnet_name: subnet}
            network_document['cidrs'] = [subnet['cidr']]
            network_document['subnets'] = subnet_document

            # update network document.
            self.inv.set(network_document)
