from singleton import Singleton
from scanner import Scanner

class ScanNetworksRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetworksRoot, self).__init__([
      {
        "type": "network",
        "fetcher": "ApiFetchNetworks",
        "children_scanner": "ScanNetwork"
      },
      {
        "type": "port",
        "fetcher": "ApiFetchPorts"
      }
    ])
