from singleton import Singleton
from scanner import Scanner

class ScanInstancesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanInstancesRoot, self).__init__([
      {
        "type": "instance",
        "fetcher": "ApiFetchHostInstances",
        "children_scanner": "ScanInstance"
      }
    ])
