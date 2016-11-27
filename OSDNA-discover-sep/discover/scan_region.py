# scan a region for availability zones and aggregates

from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_aggregates_root import ScanAggregatesRoot
from scan_availability_zones_root import ScanAvailabilityZonesRoot

class ScanRegion(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegion, self).__init__([
      {
        "type": "region_object_type",
        "fetcher": FolderFetcher("aggregates", "region"),
        "children_scanner": ScanAggregatesRoot()
      },
      {
        "type": "region_object_type",
        "fetcher": FolderFetcher("availability_zones", "region"),
        "children_scanner": ScanAvailabilityZonesRoot()
      }
    ])
