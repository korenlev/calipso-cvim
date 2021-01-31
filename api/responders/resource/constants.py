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
            "env_name": self.require(str),
            "env_type": self.require(str, validate=DataValidate.LIST, requirement=self.environment_types)
        }
        self.validate_query_data(filters, filters_requirements)

        env_name = filters.get("env_name")
        if env_name:
            environment = self.get_single_object(collection="environments_config",
                                                 query={"name": env_name})
            if not environment:
                self.bad_request("Unknown environment: {}".format(env_name))
            filters["env_type"] = environment["environment_type"]

        query = self.build_query(filters)
        constant = self.get_single_object(collection=self.COLLECTION, query=query)
        self.set_ok_response(resp, constant)

    def validate_query_data(self, data: dict, data_requirements: dict,
                            additional_key_reg=None,
                            can_be_empty_keys=None):
        super().validate_query_data(data=data, data_requirements=data_requirements,
                                    additional_key_reg=additional_key_reg, can_be_empty_keys=can_be_empty_keys)
        if "env_name" in data and "env_type" in data:
            self.bad_request("Only up to one of (env_name, env_type) can be specified")

    def build_query(self, filters: dict) -> dict:
        query = {"name": filters["name"]}
        environment_type = filters.get("env_type")
        if environment_type:
            query["environment_type"] = {"$in": [None, environment_type]}
        else:
            query["environment_type"] = {"$in": [None, "OpenStack"]}
        return query
