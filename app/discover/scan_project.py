# scan a project for endpoints and regions

from singleton import Singleton
from api_fetch_end_points import ApiFetchEndPoints
from api_fetch_project_hosts import ApiFetchProjectHosts
from api_fetch_availability_zones import ApiFetchAvailabilityZones
from scanner import Scanner
from scan_region import ScanRegion
from scan_host import ScanHost

class ScanProject(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanProject, self).__init__([
      {
        "type": "endpoint",
        "fetcher": ApiFetchEndPoints()
      },
      {
        "type": "availability_zone",
        "fetcher": ApiFetchAvailabilityZones()
      },
      {
        "type": "host",
        "fetcher": ApiFetchProjectHosts(),
        "children_scanner": ScanHost()
      }
    ])
