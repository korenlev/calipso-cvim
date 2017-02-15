from discover.db_fetch_host_network_agents import DbFetchHostNetworkAgents
from discover.scanner import Scanner
from utils.singleton import Singleton

class ScanNetworkAgentsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetworkAgentsRoot, self).__init__([
      {
        "type": "network_agent",
        "fetcher": DbFetchHostNetworkAgents()
      }
    ])
