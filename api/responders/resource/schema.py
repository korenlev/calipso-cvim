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
from base.utils.mongo_access import MongoAccess


class Schema(ResponderBase):
    COLLECTION = "schemas"

    def __init__(self):
        super().__init__()
        self.object_types = self.get_constants_by_name("object_types")

    def on_get(self, req, resp) -> None:
        filters = self.parse_query_params(req)

        filters_requirements = {
            'type': self.require(str, validate=DataValidate.LIST, requirement=self.object_types, mandatory=True),
        }

        self.validate_query_data(filters, filters_requirements)
        query = self.build_query(filters)
        response_doc = self.get_single_object(collection=self.COLLECTION, query=query)

        self.set_ok_response(resp, MongoAccess.decode_mongo_keys(response_doc))

    def build_query(self, filters) -> dict:
        query = {}
        self.update_query_with_filters(filters, ['type'], query)
        return query

