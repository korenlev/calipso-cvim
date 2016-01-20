#!/usr/bin/env ruby

# scan a region for projects, availability zones and aggregates

require 'singleton'
require_relative 'db_fetch_regions'
require_relative 'scan_region'

class ScanEnvironment < Scanner
  include Singleton
  
  def initialize()
    super([
      {:fetcher => DbFetchRegions.new(), :children_scanner => ScanRegion.instance}
    ])
  end
  
end