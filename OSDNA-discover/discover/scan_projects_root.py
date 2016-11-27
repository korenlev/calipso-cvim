#!/usr/bin/env python3
# scan an environment for projects

from singleton import Singleton
from scanner import Scanner
from api_fetch_projects import ApiFetchProjects
from scan_project import ScanProject

class ScanProjectsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanProjectsRoot, self).__init__([
      {
        "type": "project",
        "fetcher": ApiFetchProjects(),
        "object_id_to_use_in_child": "name",
        "children_scanner": ScanProject()
      }
    ])
