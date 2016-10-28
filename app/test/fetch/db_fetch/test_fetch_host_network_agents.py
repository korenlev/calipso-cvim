from discover.db_fetch_host_network_agents import DbFetchHostNetworkAgents
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_fetch_host_network_agents import *
from unittest.mock import MagicMock


class TestFetchHostNetworkAgents(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchHostNetworkAgents()
        self.fetcher.set_env(self.env)

    def test_get(self):
        # store original methods
        original_get_single = self.fetcher.inv.get_single
        original_get_objects_list_for_id = self.fetcher.get_objects_list_for_id
        # mock methods
        self.fetcher.inv.get_single = MagicMock(return_value=HOST)
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=NETWORK_AGENT)

        result = self.fetcher.get(NETWORK_AGENT_FOLDER['id'])
        # reset methods
        self.fetcher.inv.get_single = original_get_single
        self.fetcher.get_objects_list_for_id = original_get_objects_list_for_id
        self.assertNotEqual(result, [], "Can't get network agent")

