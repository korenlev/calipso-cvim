from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class FindLinks(Fetcher):
    def __init__(self):
        super().__init__()
        self.inv = InventoryMgr()

    def create_link(self, env, host, source, source_id, target, target_id,
                    link_type, link_name, state, link_weight,
                    source_label="", target_label="",
                    extra_attributes=None):
        if extra_attributes is None:
            extra_attributes = {}
        link = self.inv.create_link(env, host,
                                    source, source_id, target, target_id,
                                    link_type, link_name, state, link_weight,
                                    extra_attributes)
        if self.inv.monitoring_setup_manager:
            self.inv.monitoring_setup_manager.create_setup(link)
