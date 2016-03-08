#!/usr/bin/env python3

import cgi
import json
import re

from fetch_region_object_types import FetchRegionObjectTypes
from fetch_host_object_types import FetchHostObjectTypes
from inventory_mgr import InventoryMgr

prettify = True

class CgiFetcher:
    def __init__(self):
        pass
    

    def get_fetch_type(self, form):
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
        if what_to_fetch == "region object type":
          fetcher = FetchRegionObjectTypes()
          fetcher.set_prettify(prettify)
          response = fetcher.jsonify(fetcher.get(id))
        else:
          self.inventory = InventoryMgr()
          self.inventory.set_prettify(prettify)
          if what_to_fetch == "instance detail":
            response = self.inventory.getSingle(env_name, "instance", id)
          else:
            if what_to_fetch == "host_object_type":
              response = self.inventory.get_children(env_name, None, id)
            else:
              response = self.inventory.get_children(env_name, what_to_fetch, id)
            response = {"type": what_to_fetch, "rows": response}
          response = self.inventory.jsonify(response)
        return response
          

if __name__ == '__main__':
    fetch_manager = CgiFetcher()
    response = fetch_manager.get()
    
    print("Content-type: application/json\n\n")
    print(response)
    print("\n")
