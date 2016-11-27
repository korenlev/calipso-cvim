from singleton import Singleton
from scanner import Scanner

class ScanNetworksRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetworksRoot, self).__init__([
#      {
      # TBD
#        "type": "network",
#        "fetcher": DbNetworkFetcher("network", "host"),
#        "children_scanner": ScanNetwork()
#      }
    ])
