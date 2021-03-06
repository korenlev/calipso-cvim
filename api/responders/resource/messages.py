###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from bson import ObjectId

from api.responders.responder_base import ResponderWithOnDelete
from api.validation.data_validate import DataValidate


class Messages(ResponderWithOnDelete):

    COLLECTION = 'messages'
    ID = "_id"
    PROJECTION = {
        ID: True,
        "environment": True,
        "source_system": True,
        "level": True
    }

    def on_get(self, req, resp):
        self.log.debug("Getting messages from messages")
        filters = self.parse_query_params(req)
        messages_severity = self.get_constants_by_name("messages_severity")
        object_types = self.get_constants_by_name("object_types")
        filters_requirements = {
            'env_name': self.require(str, mandatory=True),
            'source_system': self.require(str),
            'id': self.require(ObjectId, convert_to_type=True),
            'level': self.require(str,
                                  validate=DataValidate.LIST,
                                  requirement=messages_severity),
            'related_object': self.require(str),
            'related_object_type': self.require(str,
                                                validate=DataValidate.LIST,
                                                requirement=object_types),
            'start_time': self.require(str),
            'end_time': self.require(str),
            'page': self.require(int, convert_to_type=True),
            'page_size': self.require(int, convert_to_type=True)
        }
        self.validate_query_data(filters, filters_requirements)
        page, page_size = self.get_pagination(filters)
        self.check_and_convert_datetime('start_time', filters)
        self.check_and_convert_datetime('end_time', filters)

        query = self.build_get_query(filters)
        if self.ID in query:
            message = self.get_single_object(collection=self.COLLECTION, query=query)
            self.set_ok_response(resp, message)
        else:
            objects_ids = self.get_objects_list(collection=self.COLLECTION, query=query,
                                                page=page, page_size=page_size, projection=self.PROJECTION)
            self.set_ok_response(resp, {'messages': objects_ids})

    def build_get_query(self, filters):
        query = super().build_query(filters)
        filters_keys = ['source_system', 'level', 'related_object', 'related_object_type']
        self.update_query_with_filters(filters, filters_keys, query)
        start_time = filters.get('start_time')
        if start_time:
            query['timestamp'] = {"$gte": start_time}
        end_time = filters.get('end_time')
        if end_time:
            if 'timestamp' in query:
                query['timestamp'].update({"$lte": end_time})
            else:
                query['timestamp'] = {"$lte": end_time}
        return query
