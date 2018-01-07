from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class KubeFetchVedges(Fetcher):

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, host_id) -> list:
        ret = []
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error('failed to find host: {}'.format(host_id))
            return ret
        search_condition = {
            'environment': self.get_env(),
            'type': 'pod',
            'host': host['name'],
            'labels.app': 'flannel'
        }
        vedges = self.inv.find_items(search_condition)
        for o in vedges:
            o['id'] = '{}-vedge'.format(host_id)
            o['host'] = host_id
            o['agent_type'] = 'Flannel agent'
            self.set_folder_parent(o,
                                   object_type='vedge',
                                   master_parent_type='host',
                                   master_parent_id=host_id,
                                   parent_objects_name='vedges',
                                   parent_text='vEdges')
            ret.append(o)
        return ret