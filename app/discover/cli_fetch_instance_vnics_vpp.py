###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from discover.cli_fetch_instance_vnics_base import CliFetchInstanceVnicsBase


class CliFetchInstanceVnicsVpp(CliFetchInstanceVnicsBase):
    def __init__(self):
        super().__init__()

    def get_vnic_name(self, v, instance):
        return instance["name"] + "-" + v["@type"] + "-" + v["mac"]["@address"]
