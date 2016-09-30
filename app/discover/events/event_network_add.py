from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class EventNetworkAdd(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def handle(self, env, notification):
        # build network document for adding network
        project_name = notification['_context_project_name']
        project_id = notification['_context_project_id']
        parent_id = project_id + '-networks'
        network = notification['payload']['network']
        network_id = network['id']
        network_name = network['name']

        network['environment']  = env
        network['type'] = 'network'
        network['id_path'] = "/%s/%s-projects/%s/%s/%s" % (env, env, project_id, parent_id, network_id)
        network['cidrs'] = []
        network['last_scanned'] = notification['timestamp']
        network['name_path'] = "/%s/Projects/%s/Networks/%s" % (env, project_name, network_name)
        network['network'] = network_id
        network['object_name'] = network_name
        network['parent_id'] = parent_id
        network['parent_text'] = "Networks"
        network['parent_type'] = "networks_folder"
        network['project'] = project_name
        network["show_in_tree"] = True

        network_document = self.inv.get_by_id(env, network_id)
        if network_document:
            self.log.info('network has existed, aborting network add')
            return None

        self.inv.set(network)
