from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher

class ScanNetwork(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetwork, self).__init__([
      {
        "type": "network_object_type",
        "fetcher": FolderFetcher("ports", "network")
      },
      {
        "type": "network_object_type",
        "fetcher": FolderFetcher("network_services", "network", "Network vServices")
      }
    ])
