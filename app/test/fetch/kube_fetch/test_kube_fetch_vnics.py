import unittest
from pprint import pprint
from unittest.mock import patch

from discover.fetchers.kube.kube_fetch_vnics import KubeFetchVnics
from test.fetch.kube_fetch.test_data.kube_fetch_vnics import HOST_DOC, \
    EXPECTED_VNIC
from test.fetch.logger_patcher import LoggerPatcher


class TestKubeFetchVnics(LoggerPatcher):

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.kube.kube_fetch_vnics.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.fetcher = KubeFetchVnics()

    def test_get(self):
        self.inv.get_by_id.return_value = HOST_DOC
        vnics = self.fetcher.get(HOST_DOC['id'])
        self.assertEqual(1, len(vnics))
        self.assertDictContains(EXPECTED_VNIC, vnics[0])

    def test_get_no_host(self):
        self.inv.get_by_id.return_value = None
        vnics = self.fetcher.get('wrong_host')
        self.assertEqual(0, len(vnics))

    def tearDown(self):
        self.inv_patcher.stop()
        super().tearDown()
