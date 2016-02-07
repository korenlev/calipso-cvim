# scan a project for endpoints and regions

require 'singleton'
require_relative 'api_fetch_end_points'
require_relative 'scan_region'

class ScanProject < Scanner
  include Singleton
  
  def initialize()
    super([
      {
        :type => "endpoint",
        :fetcher => ApiFetchEndPoints.new(),
        :children_scanner => ScanRegion.instance
      }
    ])
  end
  
end