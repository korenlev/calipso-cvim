from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_instances_root import ScanInstancesRoot
from scan_pnics_root import ScanPnicsRoot
from scan_host_vervices_root import ScanHostVservicesRoot
from scan_vconnectors_root import ScanVconnectorsRoot

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
        "fetcher": FolderFetcher("pnics", "host", "pNICs"),
        "children_scanner": ScanPnicsRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("vconnectors", "instance", "vConnectors"),
        "children_scanner": ScanVconnectorsRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("host_vservices", "host", "Vservices"),
        "children_scanner": ScanHostVservicesRoot()
      }
    ])
