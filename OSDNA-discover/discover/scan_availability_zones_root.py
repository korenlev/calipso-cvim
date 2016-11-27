# scan a region for availability zones and aggregates

from singleton import Singleton
from db_fetch_availability_zones import DbFetchAvailabilityZones
from scanner import Scanner
from scan_availability_zone import ScanAvailabilityZone

class ScanAvailabilityZonesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAvailabilityZonesRoot, self).__init__([
      {
        "type": "availability_zone",
        "fetcher": DbFetchAvailabilityZones(),
        "children_scanner": ScanAvailabilityZone()
      }
    ])
