#!/usr/bin/env ruby

# scan a host for instances

require 'singleton'
require_relative 'db_fetch_host_instances'
require_relative 'scanner'

class ScanHost < Scanner
  include Singleton
  
  def initialize()
    super([
      {:fetcher => DbFetchHostInstances.new()}
    ])
  end
  
end