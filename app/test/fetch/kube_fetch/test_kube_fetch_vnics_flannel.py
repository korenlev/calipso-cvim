import unittest
from unittest.mock import patch

from discover.fetchers.kube.kube_fetch_vnics_flannel \
    import KubeFetchVnicsFlannel
from test.fetch.kube_fetch.test_data.kube_fetch_vnics_flannel import HOST_DOC, \
    EXPECTED_VNIC
from test.fetch.logger_patcher import LoggerPatcher


class TestKubeFetchVnicsFlannel(LoggerPatcher):

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.kube.kube_fetch_vnics_flannel.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.fetcher = KubeFetchVnicsFlannel()

    def test_get(self):
        self.inv.get_by_id.return_value = HOST_DOC
        vnics = self.fetcher.get(HOST_DOC['id'])
        self.assertEqual(1, len(vnics))
        self.assertDictContains(EXPECTED_VNIC, vnics[0])

    def tearDown(self):
        self.inv_patcher.stop()
        super().tearDown()
