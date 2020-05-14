from base.fetcher import Fetcher
from base.utils.constants import HostType


class HostTypeValidator(Fetcher):
    # To be overridden in subclasses
    ACCEPTED_HOST_TYPES = HostType.members_list()

    def validate_host(self, host_id: str) -> bool:
        """
            Check if host exists and has an accepted type
        :param host_id: host id
        :return: is host accepted for this fetcher
        """
        host = self.inv.get_by_id(self.get_env(), host_id)
        if not host:
            self.log.error("{}: host not found: {}".format(self.__class__.__name__, host_id))
            return False

        host_types = host.get("host_type")
        if not host_types:
            self.log.error("Host {} does not have host types".format(host_id))
            return False

        if not any(t in self.ACCEPTED_HOST_TYPES for t in host_types):
            return False

        return True
