from discover.fetcher import Fetcher
from discover.inventory_mgr import InventoryMgr


class FindLinks(Fetcher):
    def __init__(self, monitoring_setup_manager):
        super().__init__()
        self.inv = InventoryMgr()
        self.monitoring_setup = monitoring_setup_manager

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
        if self.monitoring_setup:
            self.monitoring_setup.create_setup(link)
