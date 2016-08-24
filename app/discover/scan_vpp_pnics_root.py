from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher

class ScanVppPnicsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super().__init__([
      {
        "type": "pnic",
        "fetcher": "CliFetchHostPnicsVpp",
        "environment_condition": {"network_plugins": "VPP"},
        "children_scanner": "ScanOteps"
      }
    ])
