#!/usr/bin/ruby

require 'cgi'
require_relative 'fetch_regions'
require_relative 'fetch_projects'

cgi = CGI.new
what_to_fetch = cgi.params["type"][0]

id = cgi.params["id"] || ""

fetcher = nil
case what_to_fetch
  when "regions"
    fetcher = FetchRegions.new()
  when "projects"
    fetcher = FetchProjects.new()
  else
    fetcher = DbAccess.new()
end
fetcher.set_prettify(true)
fetcher.connect("10.56.20.74", 13306, "root", "BsfYNGxi", "nova")
response = fetcher.get()
cgi.out("application/json") { response }
