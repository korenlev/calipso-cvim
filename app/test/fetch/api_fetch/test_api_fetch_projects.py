from discover.api_fetch_projects import ApiFetchProjects
from test.fetch.api_fetch.test_fetch import TestFetch


class TestApiFetchProjects(TestFetch):

    def test_get(self):
        fetcher = ApiFetchProjects()
        self.set_regions_for_fetcher(fetcher)

        results = fetcher.get("test_id")
        self.assertNotEqual(results, [], "Can't get projects information")