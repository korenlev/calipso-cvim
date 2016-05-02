from singleton import Singleton
from scanner import Scanner
from db_fetch_host_vservices import DbFetchHostVservices

class ScanHostVservicesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanHostVservicesRoot, self).__init__([
      {
        "type": "vservice",
        "fetcher": DbFetchHostVservices()
      }
    ])
