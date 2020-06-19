from typing import Optional

from base.fetcher import Fetcher
from base.utils.constants import HostType


class HostTypeValidator(Fetcher):
    # To be overridden in subclasses
    ACCEPTED_HOST_TYPES = HostType.members_list()

    def _get_host(self, host_id: str) -> Optional[dict]:
        return self.inv.get_by_id(self.get_env(), host_id)

    def validate_host(self, host: dict) -> bool:
        """
            Check if host exists and has an accepted type
        :param host: host document
        :return: is host accepted for this fetcher
        """
        host_types = host.get("host_type")
        if not host_types:
            self.log.error("Host {} does not have host types".format(host['id']))
            return False

        if not any(t in self.ACCEPTED_HOST_TYPES for t in host_types):
            return False

        return True

    def get_and_validate_host(self, host_id: str) -> Optional[dict]:
        """
            Check if host exists and has an accepted type.
            Return the host document if all conditions are met
        :param host_id: host id
        :return: host document if all conditions are met
        """
        host = self._get_host(host_id)
        if not host:
            self.log.error("{}: host not found: {}".format(self.__class__.__name__, host_id))
            return None
        elif not self.validate_host(host):
            return None
        return host
