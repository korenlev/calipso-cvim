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

from api.responders.responder_base import ResponderWithOnDelete
from api.validation.data_validate import DataValidate
from base.utils.constants import ScheduledScanInterval, ScheduledScanStatus


class ScheduledScans(ResponderWithOnDelete):

    COLLECTION = "scheduled_scans"
    ID = "_id"
    PROJECTION = {
        ID: True,
        "environment": True,
        "scheduled_timestamp": True,
        "recurrence": True
    }

    def on_get(self, req, resp):
        self.log.debug("Getting scheduled scans")
        filters = self.parse_query_params(req)

        filters_requirements = {
            "env_name": self.require(str, mandatory=True),
            "id": self.require(ObjectId, convert_to_type=True),
            "recurrence": self.require(str,
                                       validate=DataValidate.LIST,
                                       requirement=ScheduledScanInterval.members_list()),
            "page": self.require(int, convert_to_type=True),
            "page_size": self.require(int, convert_to_type=True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)

        query = self.build_get_query(filters)
        if self.ID in query:
            scheduled_scan = self.get_single_object(collection=self.COLLECTION, query=query)
            self.set_ok_response(resp, scheduled_scan)
        else:
            scheduled_scan_ids = self.get_objects_list(collection=self.COLLECTION, query=query,
                                                       page=page, page_size=page_size, projection=self.PROJECTION)
            self.set_ok_response(resp, {"scheduled_scans": scheduled_scan_ids})

    def on_post(self, req, resp):
        self.log.debug("Posting new scheduled scan")
        error, scheduled_scan = self.get_content_from_request(req)
        if error:
            self.bad_request(error)

        log_levels = self.get_constants_by_name("log_levels")
        scheduled_scan_requirements = {
            "env_name": self.require(str, mandatory=True),
            "scan_only_inventory": self.require(bool, convert_to_type=True, default=False),
            "scan_only_links": self.require(bool, convert_to_type=True, default=False),
            "scan_only_cliques": self.require(bool, convert_to_type=True, default=False),
            "implicit_links": self.require(bool, convert_to_type=True, default=False),
            "recurrence": self.require(str,
                                       mandatory=True,
                                       validate=DataValidate.LIST,
                                       requirement=ScheduledScanInterval.members_list()),
            "log_level": self.require(str,
                                      validate=DataValidate.LIST,
                                      requirement=log_levels,
                                      mandatory=True),
            "clear": self.require(bool, convert_to_type=True, default=True),
            "scheduled_timestamp": self.require(str),
            "es_index": self.require(bool, convert_to_type=True, default=False)
        }
        self.validate_query_data(scheduled_scan, scheduled_scan_requirements, can_be_empty_keys=["scheduled_timestamp",
                                                                                                 "es_index"])

        self.check_and_convert_datetime("scheduled_timestamp", scheduled_scan)

        submit_timestamp = datetime.now()
        if not scheduled_scan.get("scheduled_timestamp"):
            if scheduled_scan["recurrence"] == ScheduledScanInterval.ONCE:
                self.bad_request("scheduled_timestamp field is mandatory "
                                 "when scheduled scan recurrence is set to 'ONCE'")
            scheduled_scan["scheduled_timestamp"] = submit_timestamp
        elif scheduled_scan["scheduled_timestamp"] < submit_timestamp:
            self.bad_request("scheduled_timestamp should be a datetime in the future")

        scan_only_keys = [
            k for k in scheduled_scan if k.startswith("scan_only_") and scheduled_scan[k] is True
        ]
        if len(scan_only_keys) > 1:
            self.bad_request("multiple scan_only_* flags found: {0}. "
                             "only one of them can be set."
                             .format(", ".join(scan_only_keys)))

        env_name = scheduled_scan.pop("env_name")
        scheduled_scan.update({
            "environment": env_name,
            "submit_timestamp": submit_timestamp,
            "status": ScheduledScanStatus.UPCOMING.value,
        })
        if not self.check_environment_name(env_name):
            self.bad_request("unknown environment: {}".format(env_name))

        result = self.write(scheduled_scan, self.COLLECTION)
        response_body = {
            "message": "created a new scheduled scan for environment {}".format(env_name),
            "id": str(result.inserted_id)
        }
        self.set_created_response(resp, response_body)

    def build_get_query(self, filters):
        query = super().build_query(filters)
        filters_keys = ["recurrence"]
        self.update_query_with_filters(filters, filters_keys, query)
        return query
