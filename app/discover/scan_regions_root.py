#!/usr/bin/env python3

from singleton import Singleton
from scanner import Scanner
from api_fetch_regions import ApiFetchRegions
from scan_region import ScanRegion

class ScanRegionsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegionsRoot, self).__init__([
      {
        "type": "region",
        "fetcher": "ApiFetchRegions",
        "children_scanner": "ScanRegion"
      }
    ])
