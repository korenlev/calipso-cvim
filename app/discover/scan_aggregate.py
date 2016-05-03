# scan a host aggregate for hosts

from singleton import Singleton
from db_fetch_aggregate_hosts import DbFetchAggregateHosts
from scanner import Scanner
from scan_host import ScanHost

class ScanAggregate(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAggregate, self).__init__([
      {
        "type": "host_ref",
        "fetcher": DbFetchAggregateHosts()
      }
    ])
