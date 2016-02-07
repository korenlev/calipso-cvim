#!/usr/bin/env ruby

# scan a region for projects, availability zones and aggregates

require 'singleton'
require_relative 'db_fetch_projects'
require_relative 'db_fetch_aggregates'
require_relative 'db_fetch_availability_zones'
require_relative 'db_fetch_availability_zones'
require_relative 'scan_aggregate'
require_relative 'scan_availability_zone'

class ScanRegion < Scanner
  include Singleton
  
  def initialize()
    super([
      {
        :type => "aggregate",
        :fetcher => DbFetchAggregates.new(),
        :children_scanner => ScanAggregate.instance
      },
      {
        :type => "availability zone",
        :fetcher => DbFetchAvailabilityZones.new(),
        :children_scanner => ScanAvailabilityZone.instance
      }
    ])
  end
  
end