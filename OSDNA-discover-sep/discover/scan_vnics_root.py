from singleton import Singleton
from scanner import Scanner
from cli_fetch_instance_vnics import CliFetchInstanceVnics

class ScanVnicsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVnicsRoot, self).__init__([
      {
        "type": "vnic",
        "fetcher": CliFetchInstanceVnics()
      }
    ])
