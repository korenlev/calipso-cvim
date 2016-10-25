from discover.cli_fetch_vconnectors_ovs import CliFetchVconnectorsOvs
from test.fetch.test_fetch import TestFetch
from test.fetch.cli_fetch.test_data.cli_fetch_vconnectors_ovs import *


class TestCliFetchVconnectorsOvs(TestFetch):

    def setUp(self):
        self.configure_environment()
        self.fetcher = CliFetchVconnectorsOvs()
        self.fetcher.set_env(self.env)

    def test_get_vconnectors(self):
        result = self.fetcher.get_vconnectors(NETWORK_NODE)
        self.fetcher.print_json(result)

