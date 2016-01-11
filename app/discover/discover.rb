#!/usr/bin/env ruby

require 'cgi'
require_relative 'fetch_region_object_types'
require_relative 'db_fetch_environments'
require_relative 'db_fetch_regions'
require_relative 'db_fetch_projects'
require_relative 'db_fetch_aggregates.rb'
require_relative 'db_fetch_availability_zones.rb'
require_relative 'db_fetch_aggregate_hosts.rb'
require_relative 'db_fetch_az_hosts.rb'
require_relative 'db_fetch_project_instances.rb'
require_relative 'db_fetch_host_instances.rb'
require_relative 'db_fetch_instance_details.rb'

def get_fetch_type(params)
  type = params["type"]
  !type && (return "")
  type = type[0] || ""
  (type != "tree") && (return type)
  parent_type = params["parent_type"]
  parent_type = parent_type == nil ? "" : parent_type[0]
  parent_type = parent_type == nil ? "" : parent_type
  if parent_type == "region object type"
    parent_type = params["id"][0]
  end
  
  fetch_types_by_parent = {
    "" => "environments",
    "environment" => "regions",
    "region" => "region_object_types",
    "projects root" => "projects",
    "aggregates root" => "aggregates",
    "availability zones root" => "availability_zones",
    "project" => "project_instances",
    "availability zone" => "az_hosts",
    "aggregate" => "aggregate_hosts",
    "host" => "host_instances",
    "instance" => "instance_details"
  }
  type = fetch_types_by_parent[parent_type] || ""
  return type
end

debug = false
cgi = CGI.new
what_to_fetch = get_fetch_type(cgi.params)

id = cgi.params["id"][0] || ""

fetcher = nil
case what_to_fetch
  when "environments"
    fetcher = DbFetchEnvironments.new()
  when "regions"
    fetcher = DbFetchRegions.new()
  when "region_object_types"
    fetcher = FetchRegionObjectTypes.new()
  when "projects"
    fetcher = DbFetchProjects.new()
  when "availability_zones"
    fetcher = DbFetchAvailabilityZones.new()
  when "aggregates"
    fetcher = DbFetchAggregates.new()
  when "aggregate_hosts"
    fetcher = DbFetchAggregateHosts.new()
  when "az_hosts"
    fetcher = DbFetchAZHosts.new()
  when "project_instances"
    fetcher = DbFetchProjectInstances.new()
  when "host_instances"
    fetcher = DbFetchHostInstances.new()
  when "instance_details"
    fetcher = DbFetchInstanceDetails.new()
  else
    fetcher = DbAccess.new()
end
fetcher.set_prettify(true)
fetcher.set_prettify(true)
escaped_id = fetcher.escape(id)
response = fetcher.get(escaped_id)
!debug || response = %Q|{"type": #{what_to_fetch}, "id": #{id}}|
cgi.out("application/json") { response + "\n" }
