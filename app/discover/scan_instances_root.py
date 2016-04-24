from singleton import Singleton
from api_fetch_host_instances import ApiFetchHostInstances
from scanner import Scanner
from scan_instance import ScanInstance

class ScanInstancesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanInstancesRoot, self).__init__([
      {
        "type": "instance",
        "fetcher": ApiFetchHostInstances(),
        "children_scanner": ScanInstance()
      }
    ])
