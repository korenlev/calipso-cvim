from singleton import Singleton
from scanner import Scanner
from api_fetch_networks import ApiFetchNetworks
from api_fetch_ports import ApiFetchPorts
from scan_network import ScanNetwork

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
