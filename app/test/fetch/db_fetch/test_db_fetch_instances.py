from discover.db_fetch_instances import DbFetchInstances
from test.fetch.test_fetch import TestFetch
from unittest.mock import MagicMock
from test.fetch.db_fetch.test_data.db_fetch_instances import *


class TestDbFetchInstances(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = DbFetchInstances()

    def test_get(self):
        # store original method
        original_get_objects_list = self.fetcher.get_objects_list
        # mock method
        self.fetcher.get_objects_list = MagicMock(return_value=INSTANCES_FROM_DB)

        self.fetcher.get_instance_data(INSTANCES_FROM_API)

        # reset method
        self.fetcher.get_objects_list = original_get_objects_list

        self.assertIn("name", INSTANCES_FROM_API[0], "Can't set name")
        self.assertIn("network", INSTANCES_FROM_API[0], "Can't set network")

    def test_build_instance_details(self):
        self.fetcher.build_instance_details(INSTANCES_FOR_DETAILS)
        self.assertNotEqual(INSTANCES_FOR_DETAILS['network'], [], "Can't get network info")