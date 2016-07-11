from singleton import Singleton
from scanner import Scanner

class ScanPnicsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanPnicsRoot, self).__init__([
      {
        "type": "pnic",
        "environment_condition": {"network_plugins": "OVS"},
        "fetcher": "CliFetchHostPnicsOvs"
      }
