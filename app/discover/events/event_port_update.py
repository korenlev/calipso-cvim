from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventPortUpdate(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        # check port document.
        port = notification['payload']['port']
        port_id = port['id']
        port_document = self.inv.get_by_id(env, port_id)
        if not port_document:
            self.log.info('port document does not exist, aborting port update')
            return None

        # build port document
        port_document['name'] = port['name']
        port_document['admin_state_up'] = port['admin_state_up']
        port_document['binding:vnic_type']  = port['binding:vnic_type']


        # update port document.
        self.inv.set(port_document)
