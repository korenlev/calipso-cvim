###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate
from base.utils.constants import GraphType


class Graph(ResponderBase):
    COLLECTION = "graphs"

    def on_get(self, req, resp):
        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
            'type': self.require(str, mandatory=True, validate=DataValidate.LIST, requirement=GraphType.members_list()),
            'focal_point_id': self.require(str, convert_to_type=True)
        }

        if filters['type'] == GraphType.CLIQUE.value and not filters.get('focal_point_id'):
            self.bad_request("Request for clique graphs requires focal_point_id")
        elif filters['type'] == GraphType.INVENTORY_FORCE.value and filters.get('focal_point_id'):
            self.bad_request("Request for inventory graph doesn't support focal_point_id")

        self.validate_query_data(filters, filters_requirements)
        query = self.build_query(filters)

        graph = self.get_single_object(collection=self.COLLECTION, query=query)
        self.set_ok_response(resp, graph)

    def build_query(self, filters):
        query = super().build_query(filters=filters)
        filters_keys = ["type", "focal_point_id"]
        self.update_query_with_filters(filters=filters, filters_keys=filters_keys, query=query)
        return query
