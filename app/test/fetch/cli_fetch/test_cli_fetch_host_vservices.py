from discover.cli_fetch_host_vservices import CliFetchHostVservices
from test.fetch.test_fetch import TestFetch


class TestCliFetchHostVservices(TestFetch):

    def test_get(self):
        fetcher = CliFetchHostVservices()
        fetcher.set_env(self.env)
        host = self.get_test_data({'type': 'host', 'host_type': {"$in": ["Network"]}})
        if not host:
            self.fail("No testing host in the database")

        result = fetcher.get(host['id'])
        print(result)
