from unittest.mock import MagicMock
from discover.api_fetch_projects import ApiFetchProjects
from test.fetch.test_fetch import TestFetch
from test.fetch.api_fetch.test_data.api_fetch_projects import *


class TestApiFetchProjects(TestFetch):

    def setUp(self):
        self.configure_environment()
        ApiFetchProjects.v2_auth_pwd = MagicMock(return_value=TOKEN)
        self.fetcher = ApiFetchProjects()
        self.set_regions_for_fetcher(self.fetcher)
        self.region = REGIONS[REGION_NAME]
        self.fetcher.get_region_url_nover = MagicMock(return_value=REGION_URL_NOVER)

    def test_get_for_region(self):
        # mock request endpoint
        self.fetcher.get_region_url_nover = MagicMock(return_value=REGION_URL_NOVER)
        self.fetcher.get_url = MagicMock(return_value=REGION_RESPONSE)

        result = self.fetcher.get_for_region(self.region, TOKEN)
        self.assertNotEqual(result, [], "Can't get projects information with region")

    # find the defect here, need to be fixed
    # def test_get_for_region(self):
    #     # mock request endpiny
    #     self.fetcher.get_region_url_nover = MagicMock(return_value=REGION_URL_NOVER)
    #     self.fetcher.get_url = MagicMock(return_value=REGION_ERROR_RESPONSE)
    #
    #     result = self.fetcher.get_for_region(self.region, TOKEN)
    #     result = self.assertEqual(result, [], "Can't get empty array when the region response is wrong")

    def test_get_projects_for_api_user(self):
        # mock the responses from OpenStack Api
        self.fetcher.get_url = MagicMock(side_effect=[USERS_CORRECT_RESPONSE, PROJECTS_CORRECT_RESPONSE])

        result = self.fetcher.get_projects_for_api_user(self.region, TOKEN)
        self.assertNotEqual(result, [], "Can't get projects for api user")

    def test_get_projects_for_api_user_with_no_users_response(self):
        # the response from OpenStack will not contain users information
        self.fetcher.get_url = MagicMock(return_value=USERS_RESPONSE_WITHOUT_USERS)

        result = self.fetcher.get_projects_for_api_user(self.region, TOKEN)
        self.assertIs(result, None, "Can't get None when the response from OpenStack doesn't contain users info")

    def test_get_projects_for_api_user_without_users_match(self):
        # no users from OpenStack Api match the username of the authentication information
        self.fetcher.get_url = MagicMock(return_value=USERS_RESPONSE_WITHOUT_MATCH)

        result = self.fetcher.get_projects_for_api_user(self.region, TOKEN)
        self.assertIs(result, None, "Can't get None when no users match")

    def test_get_projects_for_api_user_without_projects_response(self):
        # the projects info from OpenStack Api will be None
        self.fetcher.get_url = MagicMock(return_value=[USERS_CORRECT_RESPONSE, None])

        result = self.fetcher.get_projects_for_api_user(self.region, TOKEN)
        self.assertIs(result, None, "Can't get None when the projects info is incorrect")

    def test_get(self):
        # mock the users projects info
        self.fetcher.get_projects_for_api_user = MagicMock(return_value=USERS_PROJECTS)

        # store original method
        original_method = self.fetcher.get_for_region
        # mock the region projects info
        self.fetcher.get_for_region = MagicMock(return_value=REGION_PROJECTS)

        result = self.fetcher.get("fake_id")

        # reset get_for_region_method
        self.fetcher.get_for_region = original_method

        self.assertNotEqual(result, [], "Can't get projects")

    def test_get_without_user_projects(self):
        # no users projects fetched from OpenStack
        self.fetcher.get_projects_for_api_user = MagicMock(return_value=None)

        # store original method
        original_method = self.fetcher.get_for_region
        self.fetcher.get_for_region = MagicMock(return_value=REGION_PROJECTS)

        result = self.fetcher.get("fake_id")

        # reset get_for_region method
        self.fetcher.get_for_region = original_method

        self.assertNotEqual(result, [], "Can't get projects without users projects")

