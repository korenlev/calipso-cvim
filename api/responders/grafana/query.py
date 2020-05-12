###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from collections import OrderedDict
from typing import Optional, Union, List

from api.responders.responder_base import ResponderBase
from base.utils.constants import GraphType


class Query(ResponderBase):
    DEFAULT_PROJECTIONS = {
        "scans": ["id", "status", "submit_timestamp", "start_timestamp", "end_timestamp"],
        "scheduled_scans": ["id", "recurrence", "scheduled_timestamp"]
    }

    def __init__(self):
        super().__init__()
        self.object_types = self.get_constants_by_name("object_types")

    def on_post(self, req, resp):
        if req.content_type == "application/json":
            error, request_data = self.get_content_from_request(req)
            if error:
                return self.bad_request("Failed to get json content from request")

            scoped_vars = request_data.get("scopedVars")
            if not scoped_vars:
                return self.bad_request("Missing scoped vars")

            targets = request_data.get("targets")
            if not targets:
                return self.bad_request("Missing targets")

            target = targets[0]
            if not target:
                return self.bad_request("Missing target")

            endpoint = target.get("type")
            if not endpoint:
                return self.bad_request("Missing target type")
        else:
            return self.bad_request("Unsupported content type: {}".format(req.content_type))

        date_range = request_data.get("range")
        date_filter = self._build_datetime_filter(date_range=date_range) if date_range else {}

        environment = self._get_value(scoped_vars.get("environment_configs", scoped_vars.get("environment")))
        if not environment:
            return self.bad_request("Missing environment filter")

        if endpoint == "inventory":
            table = self.get_inventory_table(environment=environment, scoped_vars=scoped_vars, date_filter=date_filter)
            objects = [table]
        elif endpoint == "inventoryCount":
            object_types = self._get_value(scoped_vars.get("object_types"))
            table = self.get_inventory_count_table(environment=environment, object_types=object_types)
            objects = [table]
        elif endpoint == "scans":
            scans_table = self.get_scans_table(environment=environment, date_filter=date_filter)
            scheduled_scans_table = self.get_scheduled_scans_table(environment=environment)
            objects = [scans_table, scheduled_scans_table]
        elif endpoint == "tree":
            tree_table = self.get_inventory_tree_table(environment=environment)
            objects = [tree_table]
        else:
            return self.bad_request("Unsupported data type")

        return self.set_ok_response(resp, objects)

    # #### Target handlers

    def get_projection_for_object_type(self, object_type: Optional[str]) -> list:
        # Get default projection for object type and fallback projection

        projection = []
        common_default_fields = self.get_single_object(collection="attributes_for_hover_on_data",
                                                       query={"type": "ALL"})
        if common_default_fields:
            projection += common_default_fields["attributes"]

        if object_type:
            default_fields = self.get_single_object(collection="attributes_for_hover_on_data",
                                                    query={"type": object_type})
            if default_fields:
                projection += default_fields["attributes"]

        return projection

    def get_inventory_table(self, environment: str, scoped_vars: dict,
                            date_filter: dict, type_fields: Optional[dict] = None) -> dict:
        object_type = self._get_value(scoped_vars.get("object_type", scoped_vars.get("object_types")))
        default_fields = self.get_projection_for_object_type(object_type=object_type)
        additional_fields = (
            type_fields[object_type].split(",")
            if type_fields and object_type in type_fields
            else []
        )

        projection = OrderedDict({f: True for f in (default_fields + additional_fields)})

        query = self.build_inventory_query(environment=environment, object_type=object_type,
                                           date_filter=date_filter)

        objects = self.get_objects_list(collection="inventory", query=query, projection=projection)
        return self._build_grafana_table(columns=projection, objects=objects)

    def get_inventory_count_table(self, environment: str, object_types: Optional[List[str]] = None):
        query = self.build_inventory_count_query(environment=environment, object_types=object_types)

        aggregate = [{
            "$group": {
                "_id": "$type",
                "count": {
                    "$sum": 1.0
                }
            }
        }]

        objects = self.get_objects_list(collection="inventory", query=query, aggregate=aggregate)
        columns = {"type": True, "count": True}
        # "_id" values are moved to "id" field by object list fetcher
        counts = [{"type": o["id"], "count": o["count"]} for o in objects]

        return self._build_grafana_table(columns=columns,
                                         objects=counts,
                                         target="inventoryCount")

    def get_scans_table(self, environment: str, date_filter: dict) -> dict:
        projection = {f: True for f in self.DEFAULT_PROJECTIONS["scans"]}
        query = self.build_scans_query(environment=environment, date_filter=date_filter)
        sort = [("submit_timestamp", -1)]

        objects = self.get_objects_list(collection="scans", query=query, projection=projection,
                                        sort=sort)
        return self._build_grafana_table(columns=projection, objects=objects, target="scans")

    def get_scheduled_scans_table(self, environment: str) -> dict:
        projection = {f: True for f in self.DEFAULT_PROJECTIONS["scheduled_scans"]}
        query = self.build_scheduled_scans_query(environment=environment)
        sort = [("scheduled_timestamp", 1)]

        objects = self.get_objects_list(collection="scheduled_scans", query=query, projection=projection,
                                        sort=sort)
        return self._build_grafana_table(columns=projection, objects=objects, target="scheduled_scans")

    def get_inventory_tree_table(self, environment: str) -> dict:
        types = [GraphType.INVENTORY_FORCE.value, GraphType.INVENTORY_TREE.value]
        trees = []
        for t in types:
            query = self.build_tree_query(environment=environment, graph_type=t)
            tree = self.get_single_object(collection="graphs", query=query)
            trees.append(tree)
        objects = [{"results": trees}] if trees else []
        return self._build_grafana_table(columns={"results": True}, objects=objects, target="tree")

    # #### Query builders

    def _build_datetime_filter(self, date_range: Optional[dict] = None) -> dict:
        self.check_and_convert_datetime("from", date_range)
        self.check_and_convert_datetime("to", date_range)
        date_from, date_to = date_range.get("from"), date_range.get("to")

        date_filter = {}
        if date_from:
            date_filter["$gte"] = date_from
        if date_to:
            date_filter["$lte"] = date_to

        return date_filter

    @staticmethod
    def build_base_query(environment: str) -> dict:
        return {"environment": environment}

    def build_inventory_query(self, environment: str, object_type: str,
                              date_filter: Optional[dict] = None) -> dict:

        query = self.build_base_query(environment=environment)

        if object_type:
            query["type"] = object_type
        if date_filter:
            query['last_scanned'] = date_filter

        return query

    def build_inventory_count_query(self, environment: str, object_types: Optional[List[str]] = None) -> dict:
        query = self.build_base_query(environment=environment)

        if object_types and isinstance(object_types, list):
            query["type"] = {"$in": [ot for ot in object_types if ot in self.object_types]}

        return query

    def build_scans_query(self, environment: str, date_filter: Optional[dict] = None) -> dict:
        query = self.build_base_query(environment=environment)
        if date_filter:
            query['submit_timestamp'] = date_filter

        return query

    def build_scheduled_scans_query(self, environment: str) -> dict:
        return self.build_base_query(environment=environment)

    def build_tree_query(self, environment: str, graph_type: str) -> dict:
        query = self.build_base_query(environment=environment)
        query["type"] = graph_type
        return query

    @staticmethod
    def _build_grafana_table(columns: dict, objects: list, target: Optional[str] = None):
        def get_nested_field(o: Union[dict, list], field_parts: list):
            if isinstance(o, dict):
                return (
                    o.get(field_parts[0]) if len(field_parts) == 1
                    else get_nested_field(o.get(field_parts[0], {}), field_parts[1:]) if len(field_parts) > 1
                    else None
                )
            else:
                return (
                    [item.get(field_parts[0]) for item in o] if len(field_parts) == 1
                    else [get_nested_field(item.get(field_parts[0], {}), field_parts[1:]) for item in o] if len(field_parts) > 1
                    else None
                )

        table = {
            "type": "table",
            "columns": [{"text": name} for name in columns],  # TODO: column types
            "rows": [[get_nested_field(o, field.split(".")) for field in columns] for o in objects],
        }
        if target:
            table["target"] = target
        return table

    @staticmethod
    def _get_value(container: Union[dict, str]):
        return container.get("value") if isinstance(container, dict) else container
