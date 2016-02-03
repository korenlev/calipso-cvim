#!/usr/bin/env ruby

require 'cgi'
require 'json'
require_relative 'configuration'
require_relative 'inventory_mgr'
require_relative 'fetch_region_object_types'

def get_fetch_type(params)
  fetch_types_by_name = {
    "availability zones root" => "availability zone",
    "project" => "instance",
    "availability zone" => "host",
    "aggregates" => "host aggregate",
    "aggregate_hosts" => "host",
    "az_hosts" => "host",
    "project_instances" => "instance",
    "host_instances" => "instance",
    "instance" => "instance"
  }
  type = params["type"]
  !type && (return "")
  type = type[0] || ""
  type = fetch_types_by_name[type] || type.gsub(/[_]/, " ").gsub(/s$/, "")
  (type != "tree") && (return type)
  parent_type = params["parent_type"]
  parent_type = parent_type == nil ? "" : parent_type[0]
  parent_type = parent_type == nil ? "" : parent_type
  if parent_type == "region object type"
    parent_type = params["id"][0]
  end
  
  fetch_types_by_parent = {
    "" => "environment",
    "environment" => "region",
    "region" => "region_object_types",
    "projects root" => "project",
    "aggregates root" => "aggregate",
    "availability zones root" => "availability zone",
    "project" => "instance",
    "availability zone" => "host",
    "aggregate" => "host",
    "host" => "instance",
    "instance" => "instance"
  }
  type = fetch_types_by_parent[parent_type] || ""
  return type
end

debug = false
prettify = true
cgi = CGI.new
what_to_fetch = get_fetch_type(cgi.params)

id = cgi.params["id"][0] || ""

env_name = "WebEX-Mirantis@Cisco"
if what_to_fetch == "region object type"
  fetcher = FetchRegionObjectTypes.new()
  fetcher.set_prettify(prettify)
  response = fetcher.jsonify(fetcher.get(id))
else
  fetcher = InventoryMgr.instance
  fetcher.set_prettify(prettify)

  response = fetcher.get_children(env_name, what_to_fetch, id)
  response = fetcher.jsonify(response)
end
!debug || response = %Q|{"type": #{what_to_fetch}, "id": #{id}}|
cgi.out("application/json") { response + "\n" }
