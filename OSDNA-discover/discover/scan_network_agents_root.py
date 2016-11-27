from singleton import Singleton
from scanner import Scanner
from db_fetch_host_network_agents import DbFetchHostNetworkAgents

class ScanNetworkAgentsRoot(Scanner, metaclass=Singleton):
  
  def __init__(self):
    super(ScanNetworkAgentsRoot, self).__init__([
      {
        "type": "network_agent",
        "fetcher": DbFetchHostNetworkAgents()
      }
    ])
