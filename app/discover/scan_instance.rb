#!/usr/bin/env ruby

# scan an instance

require 'singleton'
require_relative 'db_fetch_instance_details'
require_relative 'scanner'

class ScanInstance < Scanner
  include Singleton
  
  def initialize()
    super([
      {:fetcher => DbFetchHostInstances.new()}
    ])
  end
  
end