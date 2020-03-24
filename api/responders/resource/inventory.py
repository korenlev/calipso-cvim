###############################################################################
# Copyright (c) 2017-2019 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from api.responders.responder_base import ResponderBase
from api.validation.data_validate import DataValidate


class Inventory(ResponderBase):

    COLLECTION = 'inventory'
    ID = 'id'
    PROJECTION = {
        ID: True,
        "name": True,
        "name_path": True,
        "type": True,
        "environment": True
    }

    def __init__(self):
        super().__init__()
        self.object_types = self.get_constants_by_name("object_types")

    def on_get(self, req, resp):
        self.log.debug("Getting objects from inventory")

        filters = self.parse_query_params(req)
        filters_requirements = {
            'env_name': self.require(str),
            'id': self.require(str),
            'id_path': self.require(str),
            'type': self.require(str, validate=DataValidate.LIST, requirement=self.object_types),
            'parent_id': self.require(str),
            'parent_path': self.require(str),
            'sub_tree': self.require(bool, convert_to_type=True),
            'page': self.require(int, convert_to_type=True),
            'page_size': self.require(int, convert_to_type=True),
            'projection': self.require(str),
            'all': self.require(bool, convert_to_type=True),
            'scanned_after': self.require(str),
            'scanned_before': self.require(str),
        }

        self.validate_query_data(filters, filters_requirements)
        self.check_and_convert_datetime('scanned_after', filters)
        self.check_and_convert_datetime('scanned_before', filters)

        page, page_size = (0, 0) if filters.get('all') is True else self.get_pagination(filters)
        query = self.build_query(filters)

        if self.ID in query:
            obj = self.get_single_object(collection=self.COLLECTION, query=query)
            self.set_ok_response(resp, obj)
        else:
            # TODO: sanitize projection?
            projection = {f: True for f in filters['projection'].split(',')} if 'projection' in filters else {}
            objects = self.get_objects_list(collection=self.COLLECTION, query=query,
                                            page=page, page_size=page_size,
                                            projection=projection if projection else self.PROJECTION)
            self.set_ok_response(resp, {"objects": objects})

    def build_query(self, filters):
        query = {}
        filters_keys = ['parent_id', 'id_path', 'id', 'type']
        self.update_query_with_filters(filters, filters_keys, query)

        parent_path = filters.get('parent_path')
        if parent_path:
            regular_expression = parent_path
            if filters.get('sub_tree', False):
                regular_expression += "[/]?"
            else:
                regular_expression += "/[^/]+$"
            query['id_path'] = {"$regex": regular_expression}

        scanned_filter = {}
        scanned_after = filters.get('scanned_after')
        if scanned_after:
            scanned_filter["$gte"] = scanned_after
        scanned_before = filters.get('scanned_before')
        if scanned_before:
            scanned_filter["$lte"] = scanned_before
        if scanned_filter:
            query['last_scanned'] = scanned_filter

        if 'env_name' in filters:
            query['environment'] = filters['env_name']

        return query
