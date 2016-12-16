from discover.singleton import Singleton
from discover.scanner import Scanner
from discover.cli_fetch_host_vservices import CliFetchHostVservices

class ScanVservicesRoot(Scanner, metaclass=Singleton):

  def __init__(self):
    super(ScanVservicesRoot, self).__init__([
      {
        "type": "vservice",
        "fetcher": CliFetchHostVservices()
      }
    ])
