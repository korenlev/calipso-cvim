#!/usr/bin/env ruby

# scan an availability zone for hosts

require 'singleton'
require_relative 'db_fetch_az_hosts'
require_relative 'scan_host'

class ScanAvailabilityZone < Scanner
  include Singleton
  
  def initialize()
    super([
      {
        :type => "host",
        :fetcher => DbFetchAZHosts.new(),
        :children_scanner => ScanHost.instance
      }
    ])
  end
  
end