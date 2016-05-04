from singleton import Singleton
from scanner import Scanner
from db_fetch_vedges import DbFetchVedges

class ScanVedgesRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVedgesRoot, self).__init__([
      {
        "type": "vedge",
        "fetcher": DbFetchVedges()
      }
    ])
