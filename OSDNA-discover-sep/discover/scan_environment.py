#!/usr/bin/env python3
# scan an environment for projects

from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher
from scan_projects_root import ScanProjectsRoot
from scan_regions_root import ScanRegionsRoot

class ScanEnvironment(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanEnvironment, self).__init__([
      {
        "type": "environment_object_type",
        "fetcher": FolderFetcher("regions", "environment"),
        "children_scanner": ScanRegionsRoot()
      },
      {
        "type": "environment_object_type",
        "fetcher": FolderFetcher("projects", "environment"),
        "children_scanner": ScanProjectsRoot()
      }
    ])
