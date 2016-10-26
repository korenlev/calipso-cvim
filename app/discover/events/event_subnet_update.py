from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventSubnetUpdate(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        # check for network document.
        subnet = notification['payload']['subnet']
        subnet_id = subnet['id']
        network_id = subnet['network_id']
        network_document = self.inv.get_by_id(env, network_id)
        if not network_document:
            self.log.info('network document does not exist, aborting subnet update')
            return None

        # update network document.
        subnets = network_document['subnets']
        for key in subnets.keys():
            if subnets[key]['id'] == subnet_id:
                if subnet['name'] == subnets[key]['name']:
                    subnets[key] = subnet
                    break
                else:
                    subnets[subnet['name']] = subnet
                    break

        self.inv.set(network_document)
