###############################################################################
# Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems)   #
# and others                                                                  #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from api.validation.data_validate import DataValidate
from api.responders.responder_base import ResponderBase
from bson.objectid import ObjectId
from datetime import datetime


class ScheduledScans(ResponderBase):
    def __init__(self):
        super().__init__()
        self.COLLECTION = "scheduled_scans"
        self.ID = "_id"
        self.PROJECTION = {
            self.ID: True,
            "environment": True,
            "scheduled_timestamp": True,
            "freq": True
        }
        self.SCAN_FREQ = [
            "YEARLY",
            "MONTHLY",
            "WEEKLY",
            "DAILY",
            "HOURLY"
        ]

    def on_get(self, req, resp):
        self.log.debug("Getting scheduled scans")
        filters = self.parse_query_params(req)

        filters_requirements = {
            "environment": self.require(str, mandatory=True),
            "id": self.require(ObjectId, True),
            "freq": self.require(str, False,
                                 DataValidate.LIST, self.SCAN_FREQ),
            "page": self.require(int, True),
            "page_size": self.require(int, True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_query(filters)
        if self.ID in query:
            scheduled_scan = self.get_object_by_id(self.COLLECTION, query,
                                                   [ObjectId, datetime],
                                                   self.ID)
            self.set_successful_response(resp, scheduled_scan)
        else:
            scheduled_scan_ids = self.get_objects_list(self.COLLECTION, query,
                                                       page, page_size,
                                                       self.PROJECTION,
                                                       [datetime])
            self.set_successful_response(resp,
                                         {"scheduled_scans": scheduled_scan_ids})

    def build_query(self, filters):
        query = {}
        filters_keys = ["freq", "environment"]
        self.update_query_with_filters(filters, filters_keys, query)

        _id = filters.get("id")
        if _id:
            query["_id"] = _id
        return query
