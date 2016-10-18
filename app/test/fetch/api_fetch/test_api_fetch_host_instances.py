from discover.api_fetch_host_instances import ApiFetchHostInstances
from test.fetch.api_fetch.test_fetch import TestFetch
from test.fetch.test_data.instance_folder import INSTANCE_FOLDER


class TestApiFetchHostInstance(TestFetch):

    def test_get(self):
        fetcher = ApiFetchHostInstances()
        fetcher.set_env(self.env)

        instances = fetcher.get(INSTANCE_FOLDER['id'])
        self.assertNotEqual(instances, [], "Compute node doesn't contain any instance information")
