# scan a region for availability zones and aggregates

from discover.db_fetch_availability_zones import DbFetchAvailabilityZones
from discover.scan_availability_zone import ScanAvailabilityZone
from discover.scanner import Scanner
from utils.singleton import Singleton

class ScanAvailabilityZonesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAvailabilityZonesRoot, self).__init__([
      {
        "type": "availability_zone",
        "fetcher": DbFetchAvailabilityZones(),
        "children_scanner": ScanAvailabilityZone()
      }
    ])
