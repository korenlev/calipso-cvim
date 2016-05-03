from singleton import Singleton
from scanner import Scanner
from cli_fetch_vconnectors import CliFetchVconnectors

class ScanVconnectorsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVconnectorsRoot, self).__init__([
      {
        "type": "vconnector",
        "fetcher": CliFetchVconnectors()
      }
    ])
