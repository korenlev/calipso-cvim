from singleton import Singleton
from folder_fetcher import FolderFetcher
from scanner import Scanner
from scan_instances_root import ScanInstancesRoot
from scan_pnics_root import ScanPnicsRoot
from scan_host_network_agents_root import ScanHostNetworkAgentsRoot
from scan_host_vservices_root import ScanHostVservicesRoot
from scan_vconnectors_root import ScanVconnectorsRoot
from scan_vedges_root import ScanVedgesRoot
from cli_fetch_vservice_vnics import CliFetchVserviceVnics

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
        "fetcher": FolderFetcher("vconnectors", "host", "vConnectors"),
        "children_scanner": ScanVconnectorsRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("vedges", "host", "vEdges"),
        "children_scanner": ScanVedgesRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("network_agents", "host",
          "Network agents"),
        "children_scanner": ScanHostNetworkAgentsRoot()
      },
      {
        "type": "host_object_type",
        "fetcher": FolderFetcher("vservices", "host", "vServices"),
        "children_scanner": ScanHostVservicesRoot()
      },
      {
        "type": "vnic",
        "fetcher": CliFetchVserviceVnics()
      }
    ])
