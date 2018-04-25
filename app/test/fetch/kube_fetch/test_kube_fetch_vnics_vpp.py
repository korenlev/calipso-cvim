from unittest.mock import patch, MagicMock

from discover.fetchers.kube.kube_fetch_vnics_vpp import KubeFetchVnicsVpp
from test.fetch.kube_fetch.test_data.kube_fetch_vnics_vpp import HOST_DOC, \
    EXPECTED_VNIC
from test.fetch.logger_patcher import LoggerPatcher
from utils.mongo_access import MongoAccess


class TestKubeFetchVnicsVpp(LoggerPatcher):

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.kube.kube_fetch_vnics_vpp.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.old_mongo_connect = MongoAccess.mongo_connect
        MongoAccess.mongo_connect = MagicMock()

        self.fetcher = KubeFetchVnicsVpp()

    def test_get(self):
        self.skipTest('TBD')
        self.inv.get_by_id.return_value = HOST_DOC
        vnics = self.fetcher.get(HOST_DOC['id'])
        self.assertEqual(1, len(vnics))
        self.assertDictContains(EXPECTED_VNIC, vnics[0])

    def tearDown(self):
        MongoAccess.mongo_connect = self.old_mongo_connect
        self.inv_patcher.stop()
        super().tearDown()
