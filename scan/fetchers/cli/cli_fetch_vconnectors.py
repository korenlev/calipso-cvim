###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from abc import abstractmethod, ABCMeta

from base.utils.constants import HostType
from base.utils.singleton import Singleton
from scan.fetchers.cli.cli_fetcher import CliFetcher
from scan.fetchers.util.validators import HostTypeValidator


class ABCSingleton(ABCMeta, Singleton):
    pass


class CliFetchVconnectors(CliFetcher, HostTypeValidator, metaclass=ABCSingleton):
    ACCEPTED_HOST_TYPES = [HostType.COMPUTE.value, HostType.NETWORK.value]

    @abstractmethod
    def get_vconnectors(self, host_id: str):
        raise NotImplementedError("Subclass must override get_vconnectors()")

    def get(self, parent_id):
        host_id = parent_id[:parent_id.rindex('-')]
        if not self.get_and_validate_host(host_id):
            return []
        return self.get_vconnectors(host_id)
