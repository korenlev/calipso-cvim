from discover.api_fetch_host_instances import ApiFetchHostInstances
from test.fetch.test_fetch import TestFetch
from test_data.api_fetch_host_instances import *
from test_data.token import TOKEN
from unittest.mock import MagicMock


class TestApiFetchHostInstances(TestFetch):

    def setUp(self):
        self.configure_environment()
        ApiFetchHostInstances.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.fetcher = ApiFetchHostInstances()
        self.set_regions_for_fetcher(self.fetcher)

    def test_get_projects(self):
        # mock the projects got from the database
        self.fetcher.inv.get = MagicMock(return_value=PROJECT_LIST)

        self.fetcher.get_projects()
        self.assertNotEqual(self.fetcher.projects, None, "Can't get projects info")

    def test_get_instances_from_api(self):
        # mock the projects stored in the database
        self.fetcher.inv.get = MagicMock(return_value=PROJECT_LIST)
        # mock the response from the OpenStack Api
        self.fetcher.get_url = MagicMock(return_value=GET_SERVERS_RESPONSE)

        result = self.fetcher.get_instances_from_api(HOST_NAME)
        self.assertNotEqual(result, [], "Can't get instances info")

    def test_get_instances_from_api_with_wrong_auth(self):
        # mock the invalid token
        self.fetcher.v2_auth_pwd = MagicMock(return_value=None)

        result = self.fetcher.get_instances_from_api(HOST_NAME)
        self.assertEqual(result, [], "Can't get empty array when the token is invalid")

    def test_get_instances_from_api_without_hypervisors_in_res(self):
        # mock the response without hypervisors info from OpenStack Api
        self.fetcher.get_url = MagicMock(return_value=GET_SERVERS_WITHOUT_HYPERVISORS_RESPONSE)

        result = self.fetcher.get_instances_from_api(HOST_NAME)
        self.assertEqual(result, [], "Can't get empty array when the response doesn't contain hypervisors info")

    def test_get_instances_from_api_without_servers_in_res(self):
        # mock the response without servers info from OpenStack Api
        self.fetcher.get_url = MagicMock(return_value=GET_SERVERS_WITHOUT_SERVERS_RESPONSE)

        result = self.fetcher.get_instances_from_api(HOST_NAME)
        self.assertEqual(result, [], "Can't get empty array when the response doesn't contain servers info")

    def test_get(self):
        # mock the projects info stored in database
        self.fetcher.inv.get = MagicMock(return_value=PROJECT_LIST)
        # mock the compute host info stored in database
        self.fetcher.inv.get_by_id = MagicMock(return_value=HOST)

        # because all the test share the same testing object, first remember the method
        original_method = self.fetcher.get_instances_from_api
        # mock th result of get_instances_for api method
        self.fetcher.get_instances_from_api = MagicMock(return_value=GET_INSTANCES_FROM_API)

        # mock fake db fetcher method
        self.fetcher.db_fetcher.get_instance_data = MagicMock()
        result = self.fetcher.get(INSTANCE_FOLDER_ID)
        self.assertNotEqual(result, [], "Can't get instances info")

        # reset original method
        self.fetcher.get_instances_from_api = original_method

    def test_get_with_non_compute_node(self):
        # mock the projects info stored in database
        self.fetcher.inv.get = MagicMock(return_value=PROJECT_LIST)
        # mock the non compute node info stored in database
        self.fetcher.inv.get_by_id = MagicMock(return_value=NON_COMPUTE_HOST)

        # store original method
        original_method = self.fetcher.get_instances_from_api
        # mock the instances info fetched from OpenStack info
        self.fetcher.get_instances_from_api = MagicMock(return_value=GET_INSTANCES_FROM_API)

        # mock fake db fetcher method
        self.fetcher.db_fetcher.get_instance_data = MagicMock()
        result = self.fetcher.get(INSTANCE_FOLDER_ID)
        self.assertNotEqual(result, [], "Can't get empty array when the host is not compute node")

        # reset original method
        self.fetcher.get_instances_from_api = original_method
