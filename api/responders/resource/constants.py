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


class Constants(ResponderBase):

    COLLECTION = 'constants'
    ID = '_id'

    def __init__(self):
        super().__init__()
        self.environment_types = self.get_constants_by_name("environment_types")

    def on_get(self, req, resp):
        self.log.debug("Getting constants with name")
        filters = self.parse_query_params(req)
        filters_requirements = {
            "name": self.require(str, mandatory=True),
            "env_type": self.require(str, validate=DataValidate.LIST, requirement=self.environment_types)
        }
        self.validate_query_data(filters, filters_requirements)
        query = self.build_query(filters)
        constant = self.get_single_object(collection=self.COLLECTION, query=query)
        self.set_ok_response(resp, constant)

    def build_query(self, filters: dict) -> dict:
        query = {"name": filters["name"]}
        environment_type = filters.get("env_type")
        if environment_type:
            query["environment_type"] = {"$in": [None, environment_type]}
        else:
            query["environment_type"] = {"$in": [None, "OpenStack"]}
        return query
