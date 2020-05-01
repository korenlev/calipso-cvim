###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.utils.configuration import Configuration
from base.utils.origins import Origin
from scan.link_finders.find_links import FindLinks


class FindLinksForDisks(FindLinks):

    def __init__(self):
        super().__init__()
        self.environment_type = None

    def setup(self, env, origin: Origin = None):
        super().setup(env, origin)
        self.configuration = Configuration()
        self.environment_type = self.configuration.get_env_type()

    def add_links(self):
        self.log.info("adding links of types: host-osd, osd-partition, partition-disk")
        self.hosts = self.inv.find_items({
            "environment": self.configuration.env_name,
            "type": "host"
        })
        self.osds = self.inv.find_items({
            "environment": self.get_env(),
            "type": "osd"
        })
        self.partitions = self.inv.find_items({
            "environment": self.get_env(),
            "type": "partition"
        })
        self.disks = self.inv.find_items({
            "environment": self.get_env(),
            "type": "disk"
        })
        for d in self.disks:
            self.add_link_for_hosts(d)
        for o in self.osds:
            self.add_link_for_osds(o)
        for p in self.partitions:
            self.add_link_for_partitions(p)

    @staticmethod
    def match_host_and_osd(host, osd):
        return (
            "{}|{}".format(host["host"], osd["devname"]) == osd["id"]
            or
            host["mac_address"] == osd["address"]
        )

    def add_link_for_hosts(self, d):
        # link_type: "host-osd"
        print(None)

    def add_link_for_osds(self, d):
        # link_type: "osd-partition"
        print(None)

    def add_link_for_partitions(self, d):
        # link_type: "partition-disk"
        print(None)
