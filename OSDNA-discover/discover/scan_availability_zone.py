# scan an availability zone for hosts

from discover.singleton import Singleton
from discover.db_fetch_az_hosts import DbFetchAZHosts
from discover.db_fetch_az_network_hosts import DbFetchAZNetworkHosts
from discover.scanner import Scanner
from discover.scan_host import ScanHost
from discover.scan_network_host import ScanNetworkHost

class ScanAvailabilityZone(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAvailabilityZone, self).__init__([
      {
        "type": "host",
        "fetcher": DbFetchAZHosts(),
        "children_scanner": ScanHost()
      },
      {
        "type": "host",
        "fetcher": DbFetchAZNetworkHosts(),
        "children_scanner": ScanNetworkHost()
      }
    ])
