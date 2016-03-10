from singleton import Singleton
from scanner import Scanner

class ScanNetwork(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetwork, self).__init__([
      {
        "type": "network_object_type",
        "fetcher": FolderFetcher("ports", "host")
      },
      {
        "type": "network_object_type",
        "fetcher": FolderFetcher("vservices", "host", "vServices"),
        "children_scanner": ScanNetworkVservices()
      }
    ])
