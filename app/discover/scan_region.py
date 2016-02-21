# scan a region for availability zones and aggregates

from singleton import Singleton
from db_fetch_aggregates import DbFetchAggregates
from db_fetch_availability_zones import DbFetchAvailabilityZones
from scanner import Scanner
from scan_aggregate import ScanAggregate
from scan_availability_zone import ScanAvailabilityZone

class ScanRegion(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegion, self).__init__([
      {
        "type": "aggregate",
        "fetcher": DbFetchAggregates(),
        "children_scanner": ScanAggregate()
      },
      {
        "type": "availability zone",
        "fetcher": DbFetchAvailabilityZones(),
        "children_scanner": ScanAvailabilityZone()
      }
    ])