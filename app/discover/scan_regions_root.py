#!/usr/bin/env python3

from scanner import Scanner
from singleton import Singleton


class ScanRegionsRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanRegionsRoot, self).__init__([
            {
                "type": "region",
                "fetcher": "ApiFetchRegions",
                "children_scanner": "ScanRegion"
            }
        ])
