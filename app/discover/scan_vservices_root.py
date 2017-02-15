from discover.cli_fetch_host_vservices import CliFetchHostVservices
from discover.scanner import Scanner
from utils.singleton import Singleton


class ScanVservicesRoot(Scanner, metaclass=Singleton):

  def __init__(self):
    super(ScanVservicesRoot, self).__init__([
      {
        "type": "vservice",
        "fetcher": CliFetchHostVservices()
      }
    ])
