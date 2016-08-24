# scan a host aggregate for hosts

from singleton import Singleton
from scanner import Scanner

class ScanAggregate(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAggregate, self).__init__([
      {
        "type": "host_ref",
        "fetcher": "DbFetchAggregateHosts"
      }
    ])
