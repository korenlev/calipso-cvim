#!/usr/bin/env ruby

# scan a host aggregate for hosts

require 'singleton'
require_relative 'db_fetch_aggregate_hosts'
require_relative 'scan_host'

class ScanAggregate < Scanner
  include Singleton
  
  def initialize()
    super([
      {:fetcher => DbFetchAggregateHosts.new(), :children_scanner => ScanHost.instance}
    ])
  end
  
end