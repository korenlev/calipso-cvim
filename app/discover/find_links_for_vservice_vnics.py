from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class FindLinksForVserviceVnics(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def add_links(self):
        self.log.info("adding links of type: vservice-vnic")
        vnics = self.inv.find_items({
            "environment": self.get_env(),
            "type": "vnic",
            "vnic_type": "vservice_vnic"
        })
        for v in vnics:
            self.add_link_for_vnic(v)

    def add_link_for_vnic(self, v):
        host = self.inv.get_by_id(self.get_env(), v["host"])
        if "Network" not in host["host_type"]:
            return
        cidr = v["cidr"]
        network = self.inv.get_by_id(self.get_env(), v["network"])
        vservice_id = v["parent_id"]
        vservice_id = vservice_id[:vservice_id.rindex('-')]
        vservice = self.inv.get_by_id(self.get_env(), vservice_id)
        source = vservice["_id"]
        source_id = vservice_id
        target = v["_id"]
        target_id = v["id"]
        link_type = "vservice-vnic"
        link_name = network["name"]
        state = "up"  # TBD
        link_weight = 0  # TBD
        self.inv.create_link(self.get_env(), v["host"], source, source_id,
                             target, target_id, link_type, link_name, state, link_weight,
                             extra_attributes={'network': v['network']})
