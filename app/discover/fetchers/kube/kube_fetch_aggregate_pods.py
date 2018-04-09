import bson

from discover.fetcher import Fetcher
from discover.fetchers.kube.kube_fetch_pod_aggregates import \
    KubeFetchPodAggregates
from utils.inventory_mgr import InventoryMgr


class KubeFetchAggregatePods(Fetcher):

    REF_SUFFIX = '-ref'

    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def get(self, aggregate_id):
        id_prefix = KubeFetchPodAggregates.AGGREGATE_ID_PREFIX
        namespace = aggregate_id.split(id_prefix)[-1]

        pods = self.inv.get_by_field(environment=self.env,
                                     item_type="pod",
                                     field_name="namespace",
                                     field_value=namespace)

        return [{
            'id': "{}{}".format(pod['id'], self.REF_SUFFIX),
            'name': pod['name'],
            'ref_id': bson.ObjectId(pod['_id'])
        } for pod in pods]
