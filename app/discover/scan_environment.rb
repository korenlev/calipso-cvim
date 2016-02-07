#!/usr/bin/env ruby

# scan a environment for projects and regions

require 'singleton'
require_relative 'db_fetch_regions'
require_relative 'api_fetch_projects'
require_relative 'api_fetch_regions'
require_relative 'scan_project'

class ScanEnvironment < Scanner
  include Singleton
  
  def initialize()
    super([
      {
        :type => "project",
        :fetcher => ApiFetchProjects.new(),
        :object_id_to_use_in_child => "name",
        :children_scanner => ScanProject.instance
      }
    ])
  end
  
end