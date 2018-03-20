from unittest.mock import patch

from discover.fetchers.aci.aci_fetch_leaf_to_spine_pnics import \
    AciFetchLeafToSpinePnics
from test.fetch.aci_fetch.aci_test_base import AciTestBase
from test.fetch.aci_fetch.test_data.aci_access import ACI_CONFIG, \
    LOGIN_RESPONSE, EMPTY_RESPONSE
from test.fetch.aci_fetch.test_data.aci_fetch_leaf_to_spine_pnics import \
    HOSTLINK_PNIC, SPINES_RESPONSE, ADJACENT_SPINES_RESPONSE


class TestAciFetchLeafToSpinePnics(AciTestBase):

    RESPONSES = {
        'aaaRefresh.json': LOGIN_RESPONSE,
        'fabricNode.json': SPINES_RESPONSE,
        'sys.json': ADJACENT_SPINES_RESPONSE,
    }

    def setUp(self):
        super().setUp()

        self.inv_patcher = patch(
            'discover.fetchers.aci.aci_fetch_leaf_to_spine_pnics.InventoryMgr'
        )
        self.inv_class = self.inv_patcher.start()
        self.inv = self.inv_class.return_value

        self.fetcher = AciFetchLeafToSpinePnics(config=ACI_CONFIG)

    @staticmethod
    def _get_by_id(environment, item_id):
        if item_id == HOSTLINK_PNIC['id']:
            return HOSTLINK_PNIC
        else:
            return None

    def test_get(self):
        self.inv.get_by_id.side_effect = self._get_by_id

        self.requests.get.side_effect = self._requests_get
        pnics = self.fetcher.get(HOSTLINK_PNIC['id'])

        self.assertEqual(2, len(pnics))

    def test_get_no_spines(self):
        self.inv.get_by_id.side_effect = self._get_by_id

        self.requests.get.side_effect = self._requests_get

        old_responses = self.RESPONSES.copy()
        self.RESPONSES['sys.json'] = EMPTY_RESPONSE
        pnics = self.fetcher.get(HOSTLINK_PNIC['id'])
        self.RESPONSES = old_responses

        self.assertEqual(0, len(pnics))

    def tearDown(self):
        self.aci_access.reset_token()
        self.inv_patcher.stop()
        super().tearDown()