from singleton import Singleton
from scanner import Scanner

class ScanVedgePnicsRoot(Scanner, metaclass=Singleton):
  
  
  def __init__(self):
    super().__init__([
      {
        "type": "pnic",
        "environment_condition": {"network_plugins": "VPP"},
        "fetcher": "CliFetchHostPnicsVpp"
      },
      {
        "type": "pnics_folder",
        "fetcher": FolderFetcher("pnics", "vedge", "pNICs"),
        "environment_condition": {"network_plugins": "VPP"},
        "children_scanner": "ScanVppPnicsRoot"
        "fetcher": "CliFetchHostPnicsVpp"
      }
      {
        "type": "pnic",
        "environment_condition": {"network_plugins": "VPP"},
        "children_scanner": "ScanOteps"
      }
      {
        "type": "vedge",
        "fetcher": "DbFetchVedgesVpp",
        "environment_condition": {"network_plugins": "VPP"},
        "children_scanner": "ScanOteps"
      }
    ])
