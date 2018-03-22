import json
from unittest.mock import patch

from kubernetes.client import ApiClient
from kubernetes.client.rest import RESTResponse
from urllib3 import HTTPResponse

from test.fetch.logger_patcher import LoggerPatcher


class KubeTestBase(LoggerPatcher):
    RESPONSES = {}

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.kube.kube_access.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.kube_client_patcher = patch(
            "discover.fetchers.kube.kube_access.kube_client"
        )
        self.kube_client = self.kube_client_patcher.start()
        self.api = self.kube_client.CoreV1Api()
        self.fetcher = None

    @staticmethod
    def _get_response(payload, response_type):
        urllib_response = HTTPResponse(status=200, body=json.dumps(payload))
        kube_response = ApiClient().deserialize(RESTResponse(urllib_response),
                                                response_type)
        return kube_response

    @staticmethod
    def get_dict_subset(expected, actual):
        # TODO: deep check?
        return {k: v for k, v in actual.items() if k in expected}

    def assertDictContains(self, expected, actual):
        self.assertDictEqual(expected, self.get_dict_subset(expected, actual))

    def assertListsContain(self, expected, actual):
        if not expected:
            raise ValueError("Expected list is empty")

        filtered_list = [self.get_dict_subset(expected[0], elem)
                         for elem in
                         actual]
        self.assertListEqual(expected, filtered_list)

    def tearDown(self):
        self.kube_client_patcher.stop()
        self.inv_patcher.stop()
        super().tearDown()
