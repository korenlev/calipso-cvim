# scan an availability zone for hosts

from singleton import Singleton
from db_fetch_az_hosts import DbFetchAZHosts
from cli_fetch_host_network_agents import CliFetchHostNetworkAgents
from scanner import Scanner
from scan_host import ScanHost

class ScanAvailabilityZone(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanAvailabilityZone, self).__init__([
      {
        "type": "host",
        "fetcher": DbFetchAZHosts(),
        "children_scanner": ScanHost()
      },
      {
        "type": "vservice",
        "fetcher": CliFetchHostNetworkAgents()
      }
    ])
