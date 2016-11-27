#!/usr/bin/env python3

from singleton import Singleton
from scanner import Scanner
from db_fetch_regions import DbFetchRegions
from scan_region import ScanRegion

class ScanRegionsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanRegionsRoot, self).__init__([
      {
        "type": "region",
        "fetcher": DbFetchRegions(),
        "children_scanner": ScanRegion()
      }
    ])
