#!/usr/bin/env ruby

require 'json'
require_relative 'fetch_regions'
require_relative 'fetch_projects'

url = "http://10.56.20.74:5000"
token = "vIhNb1l2b"
user = "admin"
password = "admin"
regionFetcher = FetchRegions.new(url)
regionFetcher.v2_auth_pwd(user, password, nil)
regionFetcher.set_v2_admin_token(token)
projectFetcher = FetchProjects.new(url)

# print regionFetcher.get_catalog(true)
print "\n"
print "projects:\n"
print "=========\n"
print projectFetcher.get_projects("RegionOne", true)


