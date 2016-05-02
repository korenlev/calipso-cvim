# scan a host for instances

from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher
from scan_vnics_root import ScanVnicsRoot
from scan_vedges_root import ScanVedgesRoot

class ScanInstance(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanInstance, self).__init__([
      {
        "type": "instance_object_type",
        "fetcher": FolderFetcher("vnics", "instance", "vNICs"),
        "children_scanner": ScanVnicsRoot()
      },
      {
        "type": "instance_object_type",
        "fetcher": FolderFetcher("vedges", "instance", "vEdges"),
        "children_scanner": ScanVedgesRoot()
      }
    ])
