from singleton import Singleton
from scanner import Scanner
from db_fetch_host_network_agents import DbFetchHostNetworkAgents
from cli_fetch_host_vservices import CliFetchHostVservices

class ScanVservicesRoot(Scanner, metaclass=Singleton):

  def __init__(self):
    super(ScanVservicesRoot, self).__init__([
      {
        "type": "vservice",
        "fetcher": CliFetchHostVservices(),
        "show_in_tree": False
      }
    ])
