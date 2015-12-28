#!/usr/bin/ruby

require 'cgi'
require_relative 'fetch_environments'
require_relative 'fetch_regions'
require_relative 'fetch_region_object_types'
require_relative 'fetch_projects'
require_relative 'fetch_aggregates.rb'
require_relative 'fetch_availability_zones.rb'
require_relative 'fetch_aggregate_hosts.rb'
require_relative 'fetch_az_hosts.rb'
require_relative 'fetch_project_instances.rb'
require_relative 'fetch_host_instances.rb'
require_relative 'fetch_instance_details.rb'

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
    fetcher = FetchEnvironments.new()
  when "regions"
    fetcher = FetchRegions.new()
  when "region_object_types"
    fetcher = FetchRegionObjectTypes.new()
  when "projects"
    fetcher = FetchProjects.new()
  when "availability_zones"
    fetcher = FetchAvailabilityZones.new()
  when "aggregates"
    fetcher = FetchAggregates.new()
  when "aggregate_hosts"
    fetcher = FetchAggregateHosts.new()
  when "az_hosts"
    fetcher = FetchAZHosts.new()
  when "project_instances"
    fetcher = FetchProjectInstances.new()
  when "host_instances"
    fetcher = FetchHostInstances.new()
  when "instance_details"
    fetcher = FetchInstanceDetails.new()
  else
    fetcher = DbAccess.new()
end
fetcher.set_prettify(true)
fetcher.connect("10.56.20.74", 13306, "root", "BsfYNGxi", "nova")
escaped_id = fetcher.escape(id)
response = fetcher.get(escaped_id)
!debug || response = %Q|{"type": #{what_to_fetch}, "id": #{id}}|
cgi.out("application/json") { response + "\n" }
