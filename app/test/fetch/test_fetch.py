import unittest

from discover.configuration import Configuration
from discover.inventory_mgr import InventoryMgr
from test.fetch.config.local_config import ENV_CONFIG, MONGODB_CONFIG, COLLECTION_CONFIG
from test.fetch.regions import REGIONS
from test.fetch.configurations import CONFIGURATIONS


class TestFetch(unittest.TestCase):
    def configure_environment(self):
        self.mongo_config = MONGODB_CONFIG
        self.env = ENV_CONFIG
        self.inv = COLLECTION_CONFIG

        self.conf = Configuration(self.mongo_config)
        self.conf.config = CONFIGURATIONS
        self.conf.use_env(self.env)
        self.inventory = InventoryMgr()
        self.inventory.set_inventory_collection(self.inv)

    def set_regions_for_fetcher(self, fetcher):
        fetcher.regions = REGIONS

    def get_test_data(self, filter):
        # get inventory collection from database
        inventory = self.inventory.coll['inventory']

        filter.update({'environment': self.env})

        if "type" in filter:
            if filter['type'] == "instances_folder":
                excluded_folders = []
                while True:
                    filter.update({'id': {'$nin': excluded_folders}})
                    instance_folder = inventory.find_one(filter)
                    if not instance_folder:
                        return None
                    id = instance_folder['id']
                    host_id = id[:id.rindex("-")]
                    host = self.inventory.get_by_id(self.env, host_id)
                    if "Compute" not in host["host_type"]:
                        excluded_folders.append(id)
                    else:
                        return instance_folder
            elif filter['type'] == "vnics_folder":
                excluded_folders = []
                while True:
                    filter.update({'id': {'$nin': excluded_folders}})
                    vnics_folder = inventory.find_one(filter)
                    if not vnics_folder:
                        return None
                    id = vnics_folder['id']
                    instance_uuid = id[:id.rindex('-')]
                    instance = self.inventory.get_by_id(self.env, instance_uuid)
                    if not instance:
                        return None
                    host = self.inventory.get_by_id(self.env, instance["host"])
                    if "Compute" not in host["host_type"]:
                        excluded_folders.append(id)
                    else:
                        return vnics_folder

        # get test data from inventory collection
        result = inventory.find_one(filter)

        return result

    # def test_get(self):
    #     # self.set_regions_for_fetcher(fetcher="a")
    #     # self.get_test_data({"environment": "Mirantis-Liberty-Xiaocong", "id": "Mirantis-Liberty-Xiaocong-regions"})
    #     self.get_test_data('regions')
