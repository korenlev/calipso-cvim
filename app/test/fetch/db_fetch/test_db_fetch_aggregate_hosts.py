from discover.db_fetch_aggregate_hosts import DbFetchAggregateHosts
from test.fetch.test_fetch import TestFetch
from test.fetch.db_fetch.test_data.db_fetch_aggregate_hosts import *
from unittest.mock import MagicMock


class TestDbFetchAggregateHosts(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchAggregateHosts()

    def test_get(self):
        # store original method
        original_get_objects_list_for_id = self.fetcher.get_objects_list_for_id
        # mock method
        self.fetcher.get_objects_list_for_id = MagicMock(return_value=HOSTS)
        result = self.fetcher.get(AGGREGATE["id"])

        # reset method
        self.fetcher.get_objects_list_for_id = original_get_objects_list_for_id

        self.assertNotEqual(result, [], "Can't get aggregate info")