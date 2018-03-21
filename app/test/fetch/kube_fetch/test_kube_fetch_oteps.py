from unittest.mock import patch

from discover.fetchers.kube.kube_fetch_oteps import KubeFetchOteps
from test.fetch.kube_fetch.test_data.kube_fetch_oteps import HOST_DOC, \
    OTEPS_FOLDER_ID, OTEPS_LIST
from test.fetch.logger_patcher import LoggerPatcher


class TestKubeFetchOteps(LoggerPatcher):

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.kube.kube_fetch_oteps.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.fetcher = KubeFetchOteps()

    def test_get(self):
        self.inv.get_by_id.return_value = HOST_DOC
        self.inv.get_by_field.return_value = OTEPS_LIST
        oteps = self.fetcher.get(OTEPS_FOLDER_ID)
        self.assertEqual(1, len(oteps))

    def test_get_no_vedge(self):
        self.inv.get_by_id.return_value = None
        oteps = self.fetcher.get('wrong_folder')
        self.assertEqual(0, len(oteps))

    def tearDown(self):
        self.inv_patcher.stop()
        super().tearDown()
