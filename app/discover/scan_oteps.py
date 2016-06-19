from singleton import Singleton
from scanner import Scanner
from db_fetch_oteps import DbFetchOteps

class ScanOteps(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super().__init__([
      {
        "type": "otep",
        "fetcher": DbFetchOteps()
      }
    ])
