from singleton import Singleton
from scanner import Scanner
from db_fetch_host_network_agents import DbFetchHostNetworkAgents


class ScanHostNetworkAgentsRoot(Scanner, metaclass=Singleton):

  def __init__(self):
    super(ScanHostNetworkAgentsRoot, self).__init__([
      {
        "type": "network_agent",
        "fetcher": DbFetchHostNetworkAgents()
      }
    ])
