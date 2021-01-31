###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from base.fetcher import Fetcher


class KubeFetchPodAggregates(Fetcher):

    AGGREGATE_ID_PREFIX = 'pod-aggregate-'

    def get(self, aggregate_id):
        aggregate = self.inv.get_by_id(self.env, aggregate_id)
        namespace = self.inv.get_by_id(self.env, aggregate['parent_id'])
        return [{
            'id': '{}{}'.format(self.AGGREGATE_ID_PREFIX, namespace['name']),
        }]
