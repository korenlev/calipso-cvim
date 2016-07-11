from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher

class ScanVedgesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVedgesRoot, self).__init__([
      {
        "type": "vedge",
        "fetcher": "DbFetchVedgesOvs",
        "environment_condition": {"network_plugins": "OVS"},
        "children_scanner": "ScanOteps"
      },
      {
        "type": "vedge",
        "fetcher": "DbFetchVedgesVpp",
        "environment_condition": {"network_plugins": "VPP"},
        "children_scanner": "ScanVedgePnicsRoot"
      }
    ])
