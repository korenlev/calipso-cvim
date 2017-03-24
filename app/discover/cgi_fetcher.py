#!/usr/bin/env python3

import cgi
import re

from utils.inventory_mgr import InventoryMgr
from utils.string_utils import jsonify

prettify = True


class CgiFetcher:

    @staticmethod
    def get_fetch_type(form):
        fetch_types_by_name = {
            "availability_zones_root": "availability_zone",
            "project": "instance",
            "availability_zone": "host",
            "aggregates": "host_aggregate",
            "aggregate_hosts": "host",
            "az_hosts": "host",
            "project_instances": "instance",
            "host_instances": "instance",
            "instance": "instance"
        }
        type = form.getvalue("type", "")
        if type == "":
            return ""
        if type in fetch_types_by_name:
            type = fetch_types_by_name[type]
        else:
            type = re.sub(r"s$", "", re.sub(r"[_]+", " ", type))
        return type
        # TODO: this code is unreachable!
        if type != "tree":
            return type

        # handle case of tree navigating: find type to fetch by type of parent
        parent_type = form.getvalue("parent_type", "")
        if parent_type == "region object type":
            parent_type = form.getvalue("id")

        fetch_types_by_parent = {
            "": "environment",
            "environment": "environment_object_type",
            "regions_root": "region",
            "region": "region_object_type",
            "projects_root": "project",
            "aggregates_root": "aggregate",
            "availability_zones_root": "availability_zone",
            "project": "instance",
            "availability_zone": "host",
            "aggregate": "host",
            "host": "host_object_type",
            "instances_root": "instance",
            "networks_root": "instance",
            "vservices_root": "vservice",
            "pnics_root": "pnic",
            "instance": "instance"
        }
        type = fetch_types_by_parent[parent_type] if parent_type in fetch_types_by_parent else ""
        return type

    def get(self):
        form = cgi.FieldStorage()
        what_to_fetch = self.get_fetch_type(form)

        id = form.getvalue("id", "")

        env_name = "WebEX-Mirantis@Cisco"
        inventory = InventoryMgr()
        if what_to_fetch == "instance detail":
            # TODO: There's no such method in InventoryMgr
            response = inventory.getSingle(env_name, "instance", id)
        else:
            response = inventory.get_children(env_name, None, id)
        response = {"type": what_to_fetch, "rows": response}
        response = jsonify(response, prettify)
        return response
