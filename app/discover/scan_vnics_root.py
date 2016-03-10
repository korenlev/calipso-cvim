from singleton import Singleton
from scanner import Scanner

class ScanVnicsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanVnicsRoot, self).__init__([
#      {
      # TBD
#        "type": "vnic",
#        "fetcher": XXX(),
#        "children_scanner": XXX()
#      }
    ])
