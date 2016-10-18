from discover.api_fetch_project_hosts import ApiFetchProjectHosts
from test.fetch.api_fetch.test_fetch import TestFetch
from test.fetch.test_data.project import PROJECT


class TestApiFetchProjectHosts(TestFetch):

    def test_get(self):
        fetcher = ApiFetchProjectHosts()
        self.set_regions_for_fetcher(fetcher)

        hosts = fetcher.get(PROJECT['name'])
        self.assertNotEqual(hosts, [], "Can't get hosts information with project name")