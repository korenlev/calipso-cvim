# scan a region for availability zones and aggregates

from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_aggregates_root import ScanAggregatesRoot
from scan_networks_root import ScanNetworksRoot

class ScanRegion(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegion, self).__init__([
      {
        "type": "region_object_type",
        "fetcher": FolderFetcher("aggregates", "region"),
        "children_scanner": ScanAggregatesRoot()
      },
      {
        # fetching of networks is done per region, to avoid
        # having to repeat the same call multiple times
        "type": "region_object_type",
        "fetcher": FolderFetcher("networks", "region"),
        "children_scanner": ScanNetworksRoot()
      }
    ])
