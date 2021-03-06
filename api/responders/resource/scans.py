###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from datetime import datetime

from bson.objectid import ObjectId

from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate


class Scans(ResponderBase):

    DEFAULT_STATUS = "pending"
    COLLECTION = "scans"
    ID = "_id"
    PROJECTION = {
        ID: True,
        "environment": True,
        "status": True,
        "end_timestamp": True,
        "start_timestamp": True
    }

    def __init__(self):
        super().__init__()
        self.scan_statuses = self.get_constants_by_name("scans_statuses")

    def on_get(self, req, resp):
        self.log.debug("Getting scans")
        filters = self.parse_query_params(req)

        filters_requirements = {
            "env_name": self.require(str, mandatory=True),
            "id": self.require(ObjectId, convert_to_type=True),
            "base_object": self.require(str),
            "status": self.require(str,
                                   validate=DataValidate.LIST,
                                   requirement=self.scan_statuses),
            "latest": self.require(bool, convert_to_type=True),
            "page": self.require(int, convert_to_type=True),
            "page_size": self.require(int, convert_to_type=True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)
        if self.ID in query:
            scan = self.get_single_object(collection=self.COLLECTION, query=query)
            self.set_ok_response(resp, scan)
        elif filters.get("latest") is True:
            scans = self.get_latest_scan(query)
            self.set_ok_response(resp, scans)
        else:
            scans_ids = self.get_objects_list(collection=self.COLLECTION, query=query,
                                              page=page, page_size=page_size, projection=self.PROJECTION)
            self.set_ok_response(resp, {"scans": scans_ids})

    def on_post(self, req, resp):
        self.log.debug("Posting new scan")
        error, scan = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        log_levels = self.get_constants_by_name("log_levels")

        scan_requirements = {
            "log_level": self.require(str,
                                      validate=DataValidate.LIST,
                                      requirement=log_levels,
                                      mandatory=True),
            "clear": self.require(bool, convert_to_type=True, default=True),
            "scan_only_inventory": self.require(bool, convert_to_type=True, default=False),
            "scan_only_links": self.require(bool, convert_to_type=True, default=False),
            "scan_only_cliques": self.require(bool, convert_to_type=True, default=False),
            "implicit_links": self.require(bool, convert_to_type=True, default=False),
            "env_name": self.require(str, mandatory=True),
            "inventory": self.require(str),
            "object_id": self.require(str),
            "es_index": self.require(bool, convert_to_type=True, default=False)
        }
        self.validate_query_data(scan, scan_requirements)
        scan_only_keys = [k for k in scan if k.startswith("scan_only_") and scan[k] is True]
        if len(scan_only_keys) > 1:
            self.bad_request("Multiple scan_only_* flags are set to true: {0}. "
                             "Only one of them can be set to true at a time."
                             .format(", ".join(scan_only_keys)))

        env_name = scan.pop("env_name")
        env = self.get_single_object(collection="environments_config",
                                     query={"name": env_name})
        if not env:
            self.bad_request("Unknown environment: {}".format(env_name))

        scan.update({
            "environment": env_name,
            "imported": env.get("imported", False),  # Scan manager should ignore this request
            "send_to_remote": env.get("imported", False),  # Discovery manager should send this request to remote
            "status": self.DEFAULT_STATUS,
            "submit_timestamp": datetime.utcnow()
        })

        result = self.write(scan, self.COLLECTION)
        response_body = {
            "message": "Created a new scan for environment {}".format(env_name),
            "id": str(result.inserted_id)
        }
        self.set_created_response(resp, response_body)

    def get_latest_scan(self, query):
        return self.get_objects_list(collection=self.COLLECTION, query=query,
                                     page=0, page_size=1, sort=[("submit_timestamp", -1)])

    def build_query(self, filters):
        query = super().build_query(filters)
        filters_keys = ["status"]
        self.update_query_with_filters(filters, filters_keys, query)
        base_object = filters.get("base_object")
        if base_object:
            query['object_id'] = base_object
        return query
