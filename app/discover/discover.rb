#!/usr/bin/ruby

require 'cgi'
require_relative 'fetch_regions'
require_relative 'fetch_projects'
require_relative 'fetch_aggregates.rb'
require_relative 'fetch_availability_zones.rb'
require_relative 'fetch_aggregate_hosts.rb'
require_relative 'fetch_az_hosts.rb'
require_relative 'fetch_instances.rb'

debug = false
cgi = CGI.new
what_to_fetch = cgi.params["type"][0]

id = cgi.params["id"][0] || ""

fetcher = nil
case what_to_fetch
  when "regions"
    fetcher = FetchRegions.new()
  when "projects"
    fetcher = FetchProjects.new()
  when "availability_zones"
    fetcher = FetchAvailabilityZones.new()
  when "aggregates"
    fetcher = FetchAggregates.new()
  when "aggregate_hosts"
    fetcher = FetchAggregateHosts.new()
  when "az_hosts"
    fetcher = FetchAZHosts .new()
  when "instances"
    fetcher = FetchInstances .new()
  else
    fetcher = DbAccess.new()
end
fetcher.set_prettify(true)
fetcher.connect("10.56.20.74", 13306, "root", "BsfYNGxi", "nova")
escaped_id = @@sql_client.escape(id)
response = fetcher.get(escaped_id)
!debug || response = %Q|{"type": #{what_to_fetch}, "id": #{id}}|
cgi.out("application/json") { response + "\n" }
