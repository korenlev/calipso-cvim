require_relative 'fetch_regions'
require_relative 'fetch_projects'

region_fetcher = FetchRegions.new()
region_fetcher.set_prettify(true)
region_fetcher.connect("10.56.20.74", 13306, "root", "BsfYNGxi", "nova")
print "Regions:\n"
print region_fetcher.get_regions()
print "\n"
print "--------\n"
print "Projects:\n"
print "---------\n"
project_fetcher = FetchProjects.new()
print project_fetcher.get_projects()
