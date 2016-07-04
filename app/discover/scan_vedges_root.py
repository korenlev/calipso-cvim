from singleton import Singleton
from scanner import Scanner

class ScanVedgesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVedgesRoot, self).__init__([
      {
        "type": "vedge",
        "fetcher": "DbFetchVedges",
        "children_scanner": "ScanOteps"
      }
    ])
