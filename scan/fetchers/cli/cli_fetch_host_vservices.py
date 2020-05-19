###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.constants import HostType
from scan.fetchers.cli.cli_fetch_host_vservice import CliFetchHostVservice
from scan.fetchers.util.validators import HostTypeValidator


class CliFetchHostVservices(CliFetchHostVservice, HostTypeValidator):
    ACCEPTED_HOST_TYPES = [HostType.NETWORK.value]

    def __init__(self):
        super(CliFetchHostVservices, self).__init__()

    def get(self, host_id):
        if not self.validate_host(host_id):
            return []

        services_ids = [l[:l.index(' ')] if ' ' in l else l
                        for l in self.run_fetch_lines("ip netns list", ssh_to_host=host_id)]
        results = [{"local_service_id": s} for s in services_ids if self.type_re.match(s)]
        for r in results:
            self.set_details(host_id, r)
        return results

