#!/usr/bin/env python3
# scan an environment for projects

from singleton import Singleton
from scanner import Scanner
from folder_fetcher import FolderFetcher

class ScanEnvironment(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanEnvironment, self).__init__([
      {
        "type": "regions_folder",
        "fetcher": FolderFetcher("regions", "environment"),
        "children_scanner": "ScanRegionsRoot"
      },
      {
        "type": "projects_folder",
        "fetcher": FolderFetcher("projects", "environment"),
        "children_scanner": "ScanProjectsRoot"
      }
    ])
