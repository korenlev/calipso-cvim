from singleton import Singleton
from scanner import Scanner
# his is old pnic handler , new handler @ (removed) now with pci stuff for vpp specifics (user space)
class ScanPnicsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanPnicsRoot, self).__init__([
#      {
      # TBD
#        "type": "pnic",
#        "fetcher": XXX(),
#        "children_scanner": XXX()
#      }
    ])
