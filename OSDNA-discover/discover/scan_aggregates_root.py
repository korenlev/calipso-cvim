# scan a region for availability zones and aggregates

from singleton import Singleton
from db_fetch_aggregates import DbFetchAggregates
from scanner import Scanner
from scan_aggregate import ScanAggregate

class ScanAggregatesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAggregatesRoot, self).__init__([
      {
        "type": "aggregate",
        "fetcher": DbFetchAggregates(),
        "children_scanner": ScanAggregate()
      }
    ])
