# scan a host for instances

from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher
from scan_vnics_root import ScanVnicsRoot

class ScanInstance(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanInstance, self).__init__([
      {
        "type": "vnics_folder",
        "fetcher": FolderFetcher("vnics", "instance", "vNICs"),
        "children_scanner": ScanVnicsRoot()
      }
    ])
