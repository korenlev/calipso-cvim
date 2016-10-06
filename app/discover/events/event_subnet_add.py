from discover.api_access import ApiAccess
from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr
from discover.scan_networks_root import ScanNetworksRoot
from discover.scan_regions_root import ScanRegionsRoot


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
            # scan network
            network_scanner = ScanNetworksRoot()
            network_scanner.set_env(env)

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
                network_root_doc = self.inv.get_by_id(env, network_document['parent_id'])
                network_scanner.scan(network_root_doc, limit_to_child_id=network_id, limit_to_child_type="network")
                network_scanner.scan_from_queue()

                network_scanner.scan_links()
                network_scanner.scan_cliques()
        else:
            # build subnet document for adding network
            self.log.info("Only update network document.")
            network_document['cidrs'].append(subnet['cidr'])
            network_document['subnets'][subnet['name']]= subnet

            # update network document.
            self.inv.set(network_document)
