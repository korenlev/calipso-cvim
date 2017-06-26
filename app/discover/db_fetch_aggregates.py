########################################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others #
#                                                                                      #
# All rights reserved. This program and the accompanying materials                     #
# are made available under the terms of the Apache License, Version 2.0                #
# which accompanies this distribution, and is available at                             #
# http://www.apache.org/licenses/LICENSE-2.0                                           #
########################################################################################
from discover.db_access import DbAccess


class DbFetchAggregates(DbAccess):
    def get(self, id):
        return self.get_objects_list(
            """
              SELECT id, name
              FROM nova.aggregates
              WHERE deleted = 0
            """,
            "host aggregate")
