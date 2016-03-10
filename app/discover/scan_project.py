# scan a project for endpoints and regions

from singleton import Singleton
from api_fetch_end_points import ApiFetchEndPoints
from scanner import Scanner
from scan_region import ScanRegion

class ScanProject(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanProject, self).__init__([
      {
        "type": "endpoint",
        "fetcher": ApiFetchEndPoints()
      }
    ])
