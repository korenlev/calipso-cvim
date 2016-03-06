#!/usr/bin/env python3
# scan an environment for projects

from singleton import Singleton
from scanner import Scanner
from api_fetch_projects import ApiFetchProjects
from db_fetch_regions import DbFetchRegions
from scan_project import ScanProject
from scan_region import ScanRegion

class ScanEnvironment(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanEnvironment, self).__init__([
      {
        "type": "project",
        "fetcher": ApiFetchProjects(),
        "object_id_to_use_in_child": "name",
        "children_scanner": ScanProject()
      },
      {
        "type": "region",
        "fetcher": DbFetchRegions(),
        "children_scanner": ScanRegion()
      }
    ])
