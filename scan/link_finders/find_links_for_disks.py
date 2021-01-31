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
    # per future ceph releases this might need revisions
    DB_PARTITION_PATH_ATT = 'bluefs_db_partition_path'
    BLK_PARTITION_PATH_ATT = 'bluestore_bdev_partition_path'

    def __init__(self):
        super().__init__()
        self.environment_type = None
        self.hosts = []
        self.osds = []
        self.disks = []
        self.partitions = []

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
        for osd in self.osds:
            self.add_link_for_hosts(osd)
        for partition in self.partitions:
            self.add_link_for_osds(partition)
        for disk in self.disks:
            self.add_link_for_partitions(disk)

    def add_link_for_hosts(self, osd):
        # link_type: "host-osd"
        metadata = osd.get('metadata', '')
        for host in self.hosts:
            if host.get('id', 'None') == osd.get('host', ''):
                self.add_links_with_specifics(host, osd,
                                              extra_att={"osd_data": metadata.get('osd_data', '')})

    def add_link_for_osds(self, partition):
        # link_type: "osd-partition"
        for osd in self.osds:
            metadata = osd.get('metadata', '')
            if ((metadata.get(self.DB_PARTITION_PATH_ATT, 'None') == partition.get('device', '')) and (
                    osd.get('host', 'None') == partition.get('host', ''))) or ((
                    metadata.get(self.BLK_PARTITION_PATH_ATT, 'None') == partition.get('device', '')) and (
                    osd.get('host', 'None') == partition.get('host', ''))) or (
                    metadata.get('osd_data', 'None') == partition.get('mount_point', '')):
                self.add_links_with_specifics(osd, partition,
                                              extra_att={"osd_objectstore": metadata.get('osd_objectstore', '')})

    def add_link_for_partitions(self, disk):
        # link_type: "partition-disk"
        for partition in self.partitions:
            if (partition.get('master_disk', 'None') == disk.get('name', '')) and (
                    partition.get('host', 'None') == disk.get('host', 'None')):
                self.add_links_with_specifics(partition, disk,
                                              extra_att={"partition_type": partition.get('label', '')})

    def add_links_with_specifics(self, source, target, extra_att=None):
        link_name = '{}-{}'.format(source.get('name', 'None'), target.get('name', ''))
        source_label = '{}-{}-{}'.format(source.get('cvim_region', ''), source.get('cvim_metro', ''),
                                         source.get('id', ''))
        target_label = target.get('id', '')
        extra = {"source_label": source_label, "target_label": target_label}
        if extra_att:
            extra.update(extra_att)
        self.link_items(source, target, link_name=link_name, extra_attributes=extra)
