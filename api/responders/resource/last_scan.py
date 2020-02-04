###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from datetime import datetime, timedelta, date

from bson.objectid import ObjectId

from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate


class LastScan(ResponderBase):

    COLLECTION = "scans"
    ID = "_id"
    PROJECTION = {
        ID: True,
        "environment": True,
        "status": True,
        "end_timestamp": True
    }

    def on_get(self, req, resp):
        self.log.debug("Getting last_scan")
        filters = self.parse_query_params(req)
        scan_statuses = self.get_constants_by_name("scans_statuses")
        filters_requirements = {
            "env_name": self.require(str, mandatory=True),
            "id": self.require(ObjectId, convert_to_type=True),
            "base_object": self.require(str),
            "status": self.require(str,
                                   validate=DataValidate.LIST,
                                   requirement=scan_statuses),
            "page": self.require(int, convert_to_type=True),
            "page_size": self.require(int, convert_to_type=True)
        }

        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        query = self.build_query(filters)
        scans_ids = self.get_objects_list(collection=self.COLLECTION, query=query,
                                          page=page, page_size=page_size, projection=self.PROJECTION)
        now = datetime.now()
        years_ago = datetime.strptime('1948-01-01T12:35:05.032', '%Y-%m-%dT%H:%M:%S.%f')
        best_delta = now - years_ago
        last_scan = ''
        last_time = years_ago
        for scan_doc in scans_ids:
            scan_doc_id = scan_doc['id']
            filters.update({'id': ObjectId(scan_doc_id)})
            query = self.build_query(filters)
            scan = self.get_object_by_id(collection=self.COLLECTION, query=query, id_field=self.ID)
            scan_end_time = datetime.strptime(scan['end_timestamp'], '%Y-%m-%dT%H:%M:%S.%f')
            if (now - scan_end_time) < best_delta:
                best_delta = now - scan_end_time
                last_time = scan_end_time
                last_scan = scan
        self.set_ok_response(resp, {"last_scan": last_scan, "date": str(last_time.date()),
                                    "time": str(last_time.time())})

    def build_query(self, filters):
        query = {}
        filters_keys = ["status"]
        self.update_query_with_filters(filters, filters_keys, query)
        base_object = filters.get("base_object")
        if base_object:
            query['object_id'] = base_object
        _id = filters.get("id")
        if _id:
            query['_id'] = _id
        query['environment'] = filters['env_name']
        return query
