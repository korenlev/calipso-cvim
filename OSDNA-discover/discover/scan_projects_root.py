#!/usr/bin/env python3
# scan an environment for projects
from discover.scanner import Scanner
from discover.singleton import Singleton


class ScanProjectsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanProjectsRoot, self).__init__([
            {
                "type": "project",
                "fetcher": "ApiFetchProjects",
                "object_id_to_use_in_child": "name",
                "children_scanner": "ScanProject"
            }
        ])
