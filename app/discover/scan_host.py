# scan a host for instances

from singleton import Singleton
from db_fetch_host_instances import DbFetchHostInstances
from scanner import Scanner

class ScanHost(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanHost, self).__init__([
      {
        "type": "instance",
        "fetcher": DbFetchHostInstances()
      }
    ])
