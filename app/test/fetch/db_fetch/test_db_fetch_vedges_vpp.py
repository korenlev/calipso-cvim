from discover.db_fetch_vedges_vpp import DbFetchVedgesVpp
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_fetch_vedges_vpp import *
from unittest.mock import MagicMock


class TestDbFetchVedgesVpp(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchVedgesVpp()
        self.fetcher.set_env(self.env)

    def test_get(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock methods
        self.fetcher.run_fetch_lines = MagicMock(side_effect=[VERSION, INTERFACES])
        self.fetcher.inv.get_by_id = MagicMock(return_value=HOST)

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertNotEqual(result, [], "Can't get vedges")

    def test_get_without_host(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock methods
        self.fetcher.run_fetch_lines = MagicMock(side_effect=[VERSION, INTERFACES])
        self.fetcher.inv.get_by_id = MagicMock(return_value=None)

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(result, [], "Can't get empty array when it can't get host from database")

    def test_get_with_wrong_host(self):
        # store original methods
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock methods
        self.fetcher.run_fetch_lines = MagicMock(side_effect=[VERSION, INTERFACES])
        self.fetcher.inv.get_by_id = MagicMock(return_value=WRONG_HOST)

        result = self.fetcher.get(VEDGES_FOLDER['id'])
        # reset methods
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(result, [], "Can't get empty array when the host type is not correct")

    def test_fetch_ports(self):
        ports = self.fetcher.fetch_ports(INTERFACES)
        self.assertEqual(ports, PORTS, "Can't get the correct ports info")