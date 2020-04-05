###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from typing import Optional

from api.responders.responder_base import ResponderBase
from base.utils.constants import GraphType


class Query(ResponderBase):
    DEFAULT_PROJECTIONS = {
        "scans": ["id", "status", "submit_timestamp", "start_timestamp", "end_timestamp"],
        "scheduled_scans": ["id", "recurrence", "scheduled_timestamp"]
    }

    def on_post(self, req, resp):
        if req.content_type == "application/json":
            error, request_data = self.get_content_from_request(req)
            if error:
                return self.bad_request("Failed to get json content from request")

            targets = request_data.get("targets")
            if not targets:
                return self.bad_request("Missing query targets")
            target = targets[0]  # TODO: multi-target requests?
            endpoint = target.get("type")
            if not endpoint:
                return self.bad_request("Missing target type")
        else:
            return self.bad_request("Unsupported content type: {}".format(req.content_type))

        date_range = request_data.get("range")
        date_filter = self._build_datetime_filter(date_range=date_range) if date_range else {}

        scoped_vars = request_data.get("scopedVars", {})
        type_fields = target.get("typeFields", {})
        env_container = scoped_vars.get("environment_configs", scoped_vars.get("environment"))  # TODO: field name
        environment = env_container["value"] if isinstance(env_container, dict) else env_container
        if not environment:
            return self.bad_request("Missing environment filter")

        objects = []
        if target["type"] == "inventory":
            object_type = target.get("objectType")
            table = self.get_inventory_table(environment=environment, object_type=object_type,
                                             type_fields=type_fields, date_filter=date_filter)
            objects = [table]
        elif target["type"] == "inventoryCount":
            table = self.get_inventory_count_table(environment=environment)
            objects = [table]
        elif target["type"] == "scans":
            scans_table = self.get_scans_table(environment=environment, date_filter=date_filter)
            scheduled_scans_table = self.get_scheduled_scans_table(environment=environment)
            objects = [scans_table, scheduled_scans_table]
        elif target["type"] == "tree":
            tree_table = self.get_inventory_tree_table(environment=environment)
            objects = [tree_table]
        else:
            return self.bad_request("Unsupported target type")

        return self.set_ok_response(resp, objects)

    # #### Target handlers

    def get_projection_for_object_type(self, object_type: Optional[str]):
        # Get default projection for object type and fallback projection
        if object_type:
            default_fields = self.get_single_object(collection="attributes_for_hover_on_data",
                                                    query={"type": object_type})
            if default_fields:
                return default_fields["attributes"]

        common_default_fields = self.get_single_object(collection="attributes_for_hover_on_data",
                                                       query={"type": "ALL"})
        if common_default_fields:
            return common_default_fields["attributes"]

        return []

    def get_inventory_table(self, environment: str, object_type: Optional[str],
                            type_fields: dict, date_filter: dict) -> dict:

        default_fields = self.get_projection_for_object_type(object_type=object_type)
        additional_fields = type_fields[object_type].split(",") if object_type in type_fields else []

        projection = {f: True for f in (default_fields + additional_fields)}

        query = self.build_inventory_query(environment=environment, object_type=object_type,
                                           date_filter=date_filter)

        objects = self.get_objects_list(collection="inventory", query=query, projection=projection)
        return self._build_grafana_table(columns=projection, objects=objects)

    def get_inventory_count_table(self, environment: str):
        query = self.build_inventory_count_query(environment=environment)
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

        objects = self.get_objects_list(collection="scans", query=query, projection=projection)
        return self._build_grafana_table(columns=projection, objects=objects, target="scans")

    def get_scheduled_scans_table(self, environment: str) -> dict:
        projection = {f: True for f in self.DEFAULT_PROJECTIONS["scheduled_scans"]}
        query = self.build_scheduled_scans_query(environment=environment)

        objects = self.get_objects_list(collection="scheduled_scans", query=query, projection=projection)
        return self._build_grafana_table(columns=projection, objects=objects, target="scheduled_scans")

    def get_inventory_tree_table(self, environment: str) -> dict:
        query = self.build_tree_query(environment=environment)

        tree = self.get_single_object(collection="graphs", query=query)  # TODO: graphs
        objects = [{"results": tree}] if tree else []
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

    def build_inventory_count_query(self, environment: str) -> dict:
        return self.build_base_query(environment=environment)

    def build_scans_query(self, environment: str, date_filter: Optional[dict] = None) -> dict:
        query = self.build_base_query(environment=environment)
        if date_filter:
            query['submit_timestamp'] = date_filter

        return query

    def build_scheduled_scans_query(self, environment: str) -> dict:
        return self.build_base_query(environment=environment)

    def build_tree_query(self, environment: str) -> dict:
        query = self.build_base_query(environment=environment)
        query["type"] = GraphType.INVENTORY.value
        return query

    @staticmethod
    def _build_grafana_table(columns: dict, objects: list, target: Optional[str] = None):
        def get_nested_field(o: dict, field_parts: list):
            return (
                o.get(field_parts[0]) if len(field_parts) == 1
                else get_nested_field(o.get(field_parts[0], {}), field_parts[1:]) if len(field_parts) > 1
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
