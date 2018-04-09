from discover.fetcher import Fetcher
from utils.inventory_mgr import InventoryMgr


class KubeFetchPodAggregates(Fetcher):

    AGGREGATE_ID_PREFIX = 'pod-aggregate-'

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, aggregate_id):
        aggregate = self.inv.get_by_id(self.env, aggregate_id)
        namespace = self.inv.get_by_id(self.env, aggregate['parent_id'])
        return [{
            'id': '{}{}'.format(self.AGGREGATE_ID_PREFIX, namespace['name']),
        }]
