###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from scan.fetchers.cli.cli_fetch_instance_vnics_base import CliFetchInstanceVnicsBase


class CliFetchInstanceVnics(CliFetchInstanceVnicsBase):
    def __init__(self):
        super().__init__()

    def set_vnic_names(self, v, instance):
        v["object_name"] = "|".join((instance["name"], v["mac_address"]))
        v["id"] = "|".join((instance["host"], v["object_name"]))
        v["name"] = "|".join((v["object_name"], v["target"]["@dev"]))

    def set_vnic_properties(self, v, instance):
        super().set_vnic_properties(v, instance)
        v["source_bridge"] = v["source"]["@bridge"]
