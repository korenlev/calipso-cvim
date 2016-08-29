# scan a region for availability zones and aggregates

from scanner import Scanner
from singleton import Singleton


class ScanAggregatesRoot(Scanner, metaclass=Singleton):
    def __init__(self):
        super(ScanAggregatesRoot, self).__init__([
            {
                "type": "aggregate",
                "fetcher": "DbFetchAggregates",
                "children_scanner": "ScanAggregate"
            }
        ])
