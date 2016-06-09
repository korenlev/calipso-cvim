# scan a region for availability zones and aggregates

from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_aggregates_root import ScanAggregatesRoot
from scan_network import ScanNetwork
from api_fetch_networks import ApiFetchNetworks
from api_fetch_ports import ApiFetchPorts

class ScanRegion(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegion, self).__init__([
      {
        "type": "aggregates_folder",
        "fetcher": FolderFetcher("aggregates", "region"),
        "children_scanner": ScanAggregatesRoot()
      },
      {
        "type": "network",
        "fetcher": ApiFetchNetworks(),
        "children_scanner": ScanNetwork()
      },
      {
        "type": "port",
        "fetcher": ApiFetchPorts()
      }
    ])
