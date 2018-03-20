from unittest.mock import MagicMock

from discover.fetchers.kube.kube_fetch_pods import KubeFetchPods
from test.fetch.kube_fetch.kube_test_base import KubeTestBase
from test.fetch.kube_fetch.test_data.kube_access import KUBE_CONFIG
from test.fetch.kube_fetch.test_data.kube_fetch_pods import HOST_DOC, \
    PODS_RESPONSE, NAMESPACE_DOC


class TestKubeFetchPods(KubeTestBase):

    def setUp(self):
        super().setUp()
        self.fetcher = KubeFetchPods(KUBE_CONFIG)

    def test_get(self):
        self.inv.get_by_id.return_value = HOST_DOC
        self.inv.find_one.return_value = NAMESPACE_DOC
        response = self._get_response(payload=PODS_RESPONSE,
                                      response_type='V1PodList')

        self.api.list_pod_for_all_namespaces = MagicMock(return_value=response)
        pods = self.fetcher.get(HOST_DOC['id'])
        self.assertEqual(1, len(pods))

    def test_get_no_host(self):
        self.inv.get_by_id.return_value = None
        pods = self.fetcher.get('wrong_host')
        self.assertEqual(0, len(pods))

    def test_get_no_namespace(self):
        self.inv.get_by_id.return_value = HOST_DOC
        self.inv.find_one.return_value = None
        response = self._get_response(payload=PODS_RESPONSE,
                                      response_type='V1PodList')

        self.api.list_pod_for_all_namespaces = MagicMock(return_value=response)
        pods = self.fetcher.get(HOST_DOC['id'])
        self.assertEqual(1, len(pods))
