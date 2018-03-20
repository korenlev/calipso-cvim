from unittest.mock import MagicMock, patch

from discover.fetchers.kube.kube_fetch_nodes import KubeFetchNodes
from test.fetch.kube_fetch.kube_test_base import KubeTestBase
from test.fetch.kube_fetch.test_data.kube_access import KUBE_CONFIG
from test.fetch.kube_fetch.test_data.kube_fetch_nodes import EMPTY_RESPONSE, \
    NODES_RESPONSE


class TestKubeFetchNodes(KubeTestBase):

    def setUp(self):
        super().setUp()

        self.conf_patcher = patch(
            'utils.cli_access.Configuration'
        )
        self.conf_class = self.conf_patcher.start()

        self.fetcher = KubeFetchNodes(KUBE_CONFIG)

    def test_get(self):
        # TODO: add cli commands emulation
        response = self._get_response(payload=NODES_RESPONSE,
                                      response_type='V1NodeList')
        self.api.list_node = MagicMock(return_value=response)
        self.fetcher.run_fetch_lines = MagicMock(return_value=[])
        nodes = self.fetcher.get(None)
        self.assertEqual(3, len(nodes))

    def test_get_no_nodes(self):
        response = self._get_response(payload=EMPTY_RESPONSE,
                                      response_type='V1NodeList')
        self.api.list_node = MagicMock(return_value=response)
        nodes = self.fetcher.get(None)
        self.assertEqual(0, len(nodes))

    def tearDown(self):
        self.conf_patcher.stop()
        super().tearDown()
