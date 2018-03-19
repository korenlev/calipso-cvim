from unittest.mock import MagicMock

from discover.fetchers.kube.kube_fetch_namespaces import KubeFetchNamespaces
from test.fetch.kube_fetch.kube_test_base import KubeTestBase
from test.fetch.kube_fetch.test_data.kube_access import KUBE_CONFIG
from test.fetch.kube_fetch.test_data.kube_fetch_namespaces import \
    NAMESPACES_RESPONSE, EMPTY_RESPONSE


class TestKubeFetchNamespaces(KubeTestBase):

    def setUp(self):
        super().setUp()
        self.fetcher = KubeFetchNamespaces(KUBE_CONFIG)

    def test_get(self):
        response = self._get_response(payload=NAMESPACES_RESPONSE,
                                      response_type='V1NamespaceList')
        self.api.list_namespace = MagicMock(return_value=response)
        namespaces = self.fetcher.get(None)
        self.assertEqual(3, len(namespaces))

    def test_get_no_namespaces(self):
        response = self._get_response(payload=EMPTY_RESPONSE,
                                      response_type='V1NamespaceList')
        self.api.list_namespace = MagicMock(return_value=response)
        namespaces = self.fetcher.get(None)
        self.assertEqual(0, len(namespaces))