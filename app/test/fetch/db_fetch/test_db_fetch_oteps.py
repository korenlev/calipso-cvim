from discover.db_fetch_oteps import DbFetchOteps
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_fetch_oteps import *
from unittest.mock import MagicMock


class TestDbFetchOteps(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchOteps()
        self.fetcher.set_env(self.env)

    def test_get(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id
        original_get_env_config = self.fetcher.config.get_env_config
        original_get_objects_list_for_id = self.fetcher.get_objects_list_for_id
        original_get_vconnector = self.fetcher.get_vconnector
        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(return_value=VEDGE)
        self.fetcher.config.get_env_config = MagicMock(return_value=CONFIGURATIONS)
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=OTEPS)
        self.fetcher.get_vconnector = MagicMock()

        oteps = self.fetcher.get(VEDGE['id'])
        # reset methods
        self.fetcher.inv.get_by_id = original_get_by_id
        self.fetcher.config.get_env_config = original_get_env_config
        self.fetcher.get_objects_list_for_id = original_get_objects_list_for_id
        self.fetcher.get_vconnector = original_get_vconnector

        self.assertNotEqual(oteps, [], "Can't get the oteps with the vedge")

    def test_icehouse_get(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id
        original_get_env_config = self.fetcher.config.get_env_config
        original_get_vconnector = self.fetcher.get_vconnector
        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(side_effect=[VEDGE, HOST])
        self.fetcher.config.get_env_config = MagicMock(return_value=ICEHOUSE_CONFIGURATIONS)
        self.fetcher.get_vconnector = MagicMock()

        oteps = self.fetcher.get(VEDGE['id'])
        # reset methods
        self.fetcher.inv.get_by_id = original_get_by_id
        self.fetcher.config.get_env_config = original_get_env_config
        self.fetcher.get_vconnector = original_get_vconnector

        self.assertNotEqual(oteps, [], "Can't get the oteps with the vedge when the environment is icehouse")

    def test_get_with_vedge_without_configurations(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(return_value=VEDGE_WITHOUT_CONFIGURATIONS)

        oteps = self.fetcher.get(VEDGE['id'])
        # reset methods
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(oteps, [], "Can't get empty array when the vedge doesn't contain configurations")

    def test_get_with_vedge_without_tunnel_types(self):
        # store original methods
        original_get_by_id = self.fetcher.inv.get_by_id
        # mock the methods
        self.fetcher.inv.get_by_id = MagicMock(return_value=VEDGE_WITHOUT_TUNNEL_TYPES)

        oteps = self.fetcher.get(VEDGE['id'])
        # reset methods
        self.fetcher.inv.get_by_id = original_get_by_id

        self.assertEqual(oteps, [], "Can't get empty array when the vedge doesn't contain tunnel types")

    def test_get_vconnectors(self):
        # store original method
        original_run_fetch_lines = self.fetcher.run_fetch_lines
        # mock the method
        self.fetcher.run_fetch_lines = MagicMock(return_value=IFCONFIG_LINES)

        self.fetcher.get_vconnector(OTEPS[0], HOST['id'], VEDGE)

        # reset method
        self.fetcher.run_fetch_lines = original_run_fetch_lines
        self.assertIn("vconnector", OTEPS[0], "Can't get vconnector info")
        self.assertEqual(OTEPS[0]['vconnector'], VCONNECTOR, "Can't get correct vconnector from command line result")
