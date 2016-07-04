from singleton import Singleton
from scanner import Scanner

class ScanVconnectorsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVconnectorsRoot, self).__init__([
      {
        "type": "vconnector",
        "fetcher": "CliFetchVconnectors"
      }
    ])
