from singleton import Singleton
from db_fetch_host_instances import DbFetchHostInstances
from scanner import Scanner
from scan_instance import ScanInstance

class ScanInstancesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanInstancesRoot, self).__init__([
      {
        "type": "instance",
        "fetcher": DbFetchHostInstances(),
        "children_scanner": ScanInstance()
      }
    ])
