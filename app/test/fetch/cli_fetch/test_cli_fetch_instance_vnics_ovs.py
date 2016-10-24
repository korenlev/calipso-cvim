from discover.cli_fetch_instance_vnics_ovs import CliFetchInstanceVnicsOvs
from test.fetch.test_fetch import TestFetch
from test.fetch.test_data.vnics_folder import VNICS_FOLDER


class TestCliFetchInstanceVnicsOvs(TestFetch):

    def test_get(self):
        fetcher = CliFetchInstanceVnicsOvs()
        fetcher.set_env(self.env)

        vnics_folder = self.inventory.get_by_id(self.env, VNICS_FOLDER['id'])
        if not vnics_folder:
            vnics_folder = self.get_test_data({'type': 'vnics_folder'})
            if not vnics_folder:
                self.fail("No testing vnics folder in the database")

        result = fetcher.get(vnics_folder['id'])

        self.assertNotEqual(result, [], "Can't get vnics info with instance vnics_folder id")
        # print(json.dumps(result,sort_keys=True, indent=4))


