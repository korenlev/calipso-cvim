from typing import Optional

from base.utils.constants import HostType
from scan.fetchers.cli.cli_fetch_host_pnics import CliFetchHostPnics

from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.util.validators import HostTypeValidator


class CliFetchExternalHostPnics(CliFetcher, HostTypeValidator):
    ACCEPTED_HOST_TYPES = [HostType.MANAGEMENT.value, HostType.STORAGE.value]

    def __init__(self):
        super().__init__()
        self.fetcher = CliFetchHostPnics()

    def set_env(self, env):
        super().set_env(env=env)
        self.fetcher.set_env(env=env)

    def get_host_id(self, parent_id: str) -> Optional[str]:
        """
            Find host id from the pnics_folder parent id
            If the parent's type is unexpected, return None
        """
        parent = self.inv.get_by_id(environment=self.get_env(), item_id=parent_id)
        if not parent:
            return None

        if parent["type"] != "pnics_folder":
            # Unknown parent hierarchy
            return parent.get("host")

        if parent["parent_type"] == "host":
            return parent["parent_id"]

        # Unknown parent hierarchy
        return None

    def get(self, parent_id):
        host_id = self.get_host_id(parent_id)
        if not host_id:
            self.log.error("Failed to find host id for pnic folder: {}".format(parent_id))
            return []
        if not self.get_and_validate_host(host_id):
            return []
        return self.fetcher.get_by_host_id(host_id)
