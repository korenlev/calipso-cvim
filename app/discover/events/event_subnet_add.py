from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


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

        # build subnet document for adding network
        subnet_name = subnet['name']
        subnet_document = {subnet_name: subnet}
        network_document['cidrs'] = [subnet['cidr']]
        network_document['subnets'] = subnet_document

        # update network document.
        self.inv.set(network_document)
