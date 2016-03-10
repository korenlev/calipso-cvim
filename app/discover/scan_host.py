from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_instances_root import ScanInstancesRoot
from scan_networks_root import ScanNetworksRoot
from scan_pnics_root import ScanPnicsRoot
from scan_vservices_root import ScanVservicesRoot

class ScanHost(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanHost, self).__init__([
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("instances", "host"),
        "children_scanner": ScanInstancesRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("networks", "host"),
        "children_scanner": ScanNetworksRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("pnics", "host", "pNICs"),
        "children_scanner": ScanPnicsRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("vservices", "host", "vServices"),
        "children_scanner": ScanVservicesRoot()
      }
    ])
